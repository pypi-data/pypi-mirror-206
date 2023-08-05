# 2023.4.23 cp from wps-xgec.py  uvicorn wps7000:app --port 7001 --host 0.0.0.0 --reload 
# 2022.11.16, cp from xessay.py  # 2022.4.7 cp from util/xwps.py    2022.5.27, add ratio 
import json, time, traceback, fire,sys, redis, hashlib ,socket,platform,os,requests,re, fastapi, uvicorn, difflib, spacy # 3.4.1 needed
redis.r		= redis.Redis(host=os.getenv('rhost', "172.17.0.1" if 'linux' in sys.platform else 'hw160.jukuu.com' ), port=int( os.getenv('rport', 6626 ) ), decode_responses=True) # local cache only , no gec included
trantab		= str.maketrans("，　。！“”‘’；：？％＄＠＆＊（）［］＋－ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ１２３４５６７８９０ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ", ", .!\"\"'';:?%$@&*()[]+-ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz") #str.translate(trantab)
valid_ratio	= lambda snt: len(re.sub(r'[\u4e00-\u9fa5]', '', snt.translate(trantab) ) ) / ( len(snt) + 0.01)  #<= ratio  # at least 70% is English

if not hasattr(spacy, 'nlp'):
	from spacy.lang import en
	spacy.sntbr		= (inst := en.English(), inst.add_pipe("sentencizer"))[0]
	spacy.sntpid	= lambda essay: (pid:=0, [ ( pid := pid + 1 if "\n" in snt.text else pid,  (snt.text, pid))[-1] for snt in  spacy.sntbr(essay).sents] )[-1]
	spacy.nlp		= spacy.load('en_core_web_sm')

import mkf, score, pingyu, gecv1 # added gecv1 2022.11.21
from en.dims import docs_to_dims

def _get_docs(snts, ttl:int=37200): # it is better where there is a outside xsnt-spacy consumer, but it is not a must 
	reslist = redis.r.mget([f"snt:{snt}" for snt in snts])
	return  [ ( doc:=spacy.nlp(snt), redis.r.setex(f"snt:{snt}", ttl, json.dumps(doc.to_json()) ), doc )[-1] if res is None else  spacy.tokens.Doc(spacy.nlp.vocab).from_json(json.loads(res) ) for snt, res in zip(snts, reslist) ]

from fastapi import FastAPI, File, UploadFile,Form, Body
from fastapi.responses import HTMLResponse
app = fastapi.FastAPI() 
from fastapi.middleware.cors import CORSMiddleware  #https://fastapi.tiangolo.com/zh/tutorial/cors/
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=["*"], allow_headers=["*"],)
@app.get('/')
def home(): return HTMLResponse(content=f"<h2> dsk api for wps, redis6626 is the local cache, spacy 3.4.1 needed</h2><a href='/docs'> docs </a> | <a href='/redoc'> redoc </a><br> 2023.4.23")

dskhost	=	os.getenv('dskhost', "172.17.0.1:7095") #gpu120.wrask.com:7095
gechost =	os.getenv('gechost', 'gpu120.wrask.com:7626') # HTTP api, on top of redis6626, xadd-blpop 

@app.post('/wps-gec-dsk')
def wps_xgec_dsk(arr:dict={"essay":"English is a internationaly language which becomes importantly for modern world. 中文In China, English is took to be a foreigh language which many student choosed to learn. They begin to studying English at a early age. They use at least one hour to learn English knowledges a day. Even kids in kindergarten have begun learning simple words. That's a good phenomenan, for English is essential nowadays. In addition to, some people think English is superior than Chinese. In me opinion, though English is for great significance, but English is after all a foreign language. it is hard for people to see eye to eye. English do help us read English original works, but Chinese helps us learn a true China. Only by characters Chinese literature can send off its brilliance. Learning a country's culture, especial its classic culture, the first thing is learn its language. Because of we are Chinese, why do we give up our mother tongue and learn our owne culture through a foreign language?"}
		, use_gec:bool=True, topk_gec:int=64, gec_local:bool=False, max_snt_len:int=2048, with_score:bool=True, score_snts:int=32, internal_sim_default:float=0.2, ibeg_byte:bool=True, diffmerge:bool=False,  timeout:int=9, ttl:int=39200):  
	''' # wps **ONLY** api, 依赖 dskhost 和 gechost
	# arr = {"essay":"Hello world"}, 用essay存放输入的作文 	# use_gec:bool    为True 时启动gpu的gec翻译 # topk_gec:int = 64 , 只翻译文中 前64 个句子
	# max_snt_len:int=2048, 超过这个长度的句子不分析 # with_score:bool=True,  为False时 不打分 	# score_snts:int=32,  取文中前32个句子进行打分 	# internal_sim_default:float=0.2 , 缺省内相关度，这个维度计算很重，wps不需要，直接取缺省值
	# ibeg_byte:bool=True： 返回偏移， wps前端定位需求 	# diffmerge:bool=False：GEC的合并策略 	# dskhost:str="172.17.0.1:7095"  提供dsk-java分析的api 	# gechost:str="gpu120.wrask.com:7626"  提供gec的翻译服务，基于redis	# timeout:int=9	：  调用gec时的blpop等待时间
	'''
	try:
		start	= time.time()
		essay	= arr.get("essay", arr.get('doc','')) #.strip()
		if not essay: return {"failed":"empty essay"}

		sntpids = spacy.sntpid(essay)  # [(snt,pid) ]
		snts	= [snt for snt,pid in sntpids ] 	
		ratios  = [ valid_ratio(snt) for snt in snts ]
		valids  = [ snt for snt, ratio in zip(snts, ratios) if ratio >= float(arr.get('ratio',0.6)) and len(snt) < max_snt_len ] # at least 60% is English
		[redis.r.xadd('xsnt', {'snt':snt}, maxlen=30000) for snt in valids]  # notify:  spacy/gec , added maxlen 2022.10.15

		#sntdic  = {} if not use_gec else _get_gecs(valids[0:topk_gec], timeout) if not gec_local else gecv1.gecsnts(valids[0:topk_gec])
		sntdic	= requests.post(f"http://{gechost}/xgec-snts?name=xsnts&timeout={timeout}&ttl={ttl}", json=valids).json() if not gec_local else {}
		docs	= _get_docs(valids, ttl) 
		sntmkf = mkf.snt_mkf(valids, docs, sntdic, ibeg_byte=ibeg_byte, diffmerge =diffmerge , batch=0, dskhost=dskhost) 
		
		if valids and with_score: #not 'noscore' in arr: 
			dims = docs_to_dims(valids[0:score_snts], docs[0:score_snts]) # only top [0:score_snts] considered for scoring 
			if not 'internal_sim' in dims: dims['internal_sim'] = internal_sim_default
			arr.update(score.dims_score(dims))
			arr['pingyu'] = pingyu.get_pingyu(dims)

		fds = [ sntmkf.get(snt, {'feedback':{}, 'meta':{'snt':snt}}) for snt in snts ] 
		[ fd['meta'].update({"sid":i}) for i, fd in enumerate(fds) ]
		[ fd['meta'].update({"pid":sntpid[1], "snt_ori": sntpid[0]}) for sntpid, fd in zip(sntpids,fds) ]
		arr["timing"] = time.time() - start

		res = {'snt': fds, "info": arr}
		if 'dims' in dir() and dims: res.update({'doc': dims})
		return res

	except Exception as ex:
		print(">>gecv1_dsk Ex:", ex, "\t|", arr)
		exc_type, exc_value, exc_traceback_obj = sys.exc_info()
		traceback.print_tb(exc_traceback_obj)


@app.post('/dims-score')
def dims_score(doc:dict={"doc_tc": 191.0, "asl": 74.6154, "ttr2": 62.2009, "ttr": 57.0651, "ast": 14.6923, "snt_num": 13.0, "cl_sum": 8.0, "pred_diff_max3": 5.9, "ttr1": 5.5769, "word_diff_avg": 4.7957, "awl": 4.2723, "prmods_tc": 4.2308, "e_snt.fitted": 3.0, "ast_sd": 1.3431, "mwe_pv": 1.0769, "spell_correct_ratio": 1.0, "kp_correct_ratio": 0.8849, "internal_sim": 0.8794574205761223, "mwe_disconj": 0.8462, "simple_sent_ri": 0.7647, "cl_ratio": 0.6162, "snt_correct_ratio": 0.3077, "simple_sent_ratio": 0.3077, "grammar_correct_ri": 0.3077, "prmods_ratio": 0.2763, "word_gt7": 0.2669, "n_ratio": 0.2407, "v_ratio": 0.1884, "jj_ratio": 0.1099, "art_ratio": 0.0523, "comma_ratio": 0.0471, "b3_b1": 0.0411, "rb_ratio": 0.0366, "b3": 0.0262, "cc_ratio": 0.0157, "kp_correct_ri": 0.0},
			formula:dict={ "ast":[9.9, 11.99, 15.3, 18.51, 25.32,				2,0.0882, 0.3241],
				"awl":[3.5, 4.1, 4.56, 5.1, 6.0,					3,0.0882, 0.5],
				"b3":[0, 0.03, 0.08, 0.12, 0.15 ,					1, 0.0956, 0.2096],
				"cl_sum":[1, 6.68, 12, 16, 26,						2,0.0441, 0.1621],
				"grammar_correct_ri":[0.6, 0.85, 0.92, 0.97,1.0,	2,0.0368, 0.1352],
				"internal_sim":[0.0, 0.08, 0.2, 0.3, 0.4,			4, 0.0735, 0.7688],
				"kp_correct_ri":[0.7, 0.9, 0.95, 0.97, 1,			1, 0.0368, 0.0807],
				"mwe_pv":[0.01,8.03, 12, 20.21, 25,					4, 0.0221, 0.2312],
				"pred_diff_max3":[3.84, 5.11, 6.51, 7.9, 10.09 ,	1, 0.0368, 0.0807],
				"prmods_ratio":[0.06, 0.21, 0.3, 0.4, 0.5,			2, 0.0294, 0.108],
				"prmods_tc":[1.1, 2.76, 4.75, 6.76, 10.0,			2, 0.0368, 0.1352],
				"simple_sent_ri":[0.4, 0.65, 0.9, 0.95, 1,			2, 0.0368, 0.1352],
				"snt_correct_ratio":[0.01, 0.2, 0.45, 0.75, 1,		1, 0.0368, 0.0807],
				"spell_correct_ratio":[0.8, 0.9, 0.97, 0.99, 1,		1, 0.1471, 0.3226],
				"ttr1":[3.43, 4.28, 5.2, 6, 6.8,					3, 0.0882, 0.5],
				"word_diff_avg":[4.47, 4.73, 5.25,5.8, 6.6,			1, 0.0441, 0.0967],
				"word_gt7":[0.11, 0.19, 0.3, 0.42, 0.49,			1, 0.0588, 0.1289]} , internal_sim_default:float=0.2): 
	'''  formula is read from mysql config, 2022.11.20 '''
	if not 'internal_sim' in doc : doc['internal_sim'] = internal_sim_default
	return score.dims_score(doc, formula)

@app.get("/spacy-sntbr")
def sntbr(text:str="The quick fox jumped over the lazy dog. The justice delayed is justice denied.", trim:bool=False, with_pid:bool=False):
	''' 2022.8.10 '''
	from spacy.lang import en
	if not hasattr(sntbr, 'inst'): 
		sntbr.inst = en.English()
		sntbr.inst.add_pipe("sentencizer")

	doc = sntbr.inst(text)
	if not with_pid: return [ snt.text.strip() if trim else snt.text for snt in  doc.sents]

	pid = 0 #spacy.sntpidoff	= lambda essay: (pid:=0, doc:=spacy.sntbr(essay), [ ( pid := pid + 1 if "\n" in snt.text else pid,  (snt.text, pid, doc[snt.start].idx))[-1] for snt in  doc.sents] )[-1]
	arr = []
	for snt in  doc.sents:
		if "\n" in snt.text: pid = pid + 1 
		arr.append( (snt.text, pid) ) 
	return arr 

@app.get('/host-info')
def host_info(): return {"host": platform.node(), "hostname": socket.gethostname(), "ip": socket.gethostbyname(socket.gethostname()) }

if __name__ == '__main__':
	uvicorn.run(app, host='0.0.0.0', port=7000)

'''
docker run -d --restart=always -p 7000:8000 --name wps7000 -v /data/cikuu/pypi/dsk:/dsk -e rport=6665 wrask/gecv1 uvicorn wps7000:app --host 0.0.0.0 --app-dir /dsk --reload --workers 2
>>gecv1_dsk Ex: cannot switch to a different thread 	| {'essay': 'The supplier is responsible for any changes or unacceptable conditions of the final looking or practicality that does not match the agreed drawing with the consultant or design. \n'}
>>gecv1_dsk Ex: cannot switch to a different thread 	| {'essay': 'However, there exist main disadvantages of slow fashion.Most people are aware of both potential crisis of fast fashion and the importance of sustainable development. But the priority is personal economic. Without economic freedom. People’s interests are prior to cheap trendy products though taking pressure to environment instead of higher standards of sustainability, except for their true moral heart.(Brewer 2019)In “Perceptions of Fast Fashion and Second Hand Clothing”Sorensen and Johnson Jorgensen point out the natural fibers required by slow fashion is not proper to nowadays washing machines and dryers that means the clothes need to be washed manually and singly even at a low temperature additionally dry-cleaned. Besides,such natural fibers produce through a tedious supply chain ending with little output.These essential problems seem impossible to solve.\n'}
'''