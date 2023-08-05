# 2023.5.1  .# 2022-2-13  cp from cikuu/bin/es.py 
import so, requests,time, gecdsk, fire,json

def run(idxname, debug:bool=False):
	''' testdoc, 2023.5.2 '''
	if not requests.es.indices.exists(index=idxname): requests.es.indices.create(index=idxname, body=so.config)
	start = time.time()
	rows = so.cursor_rows(f"select did, doc from {idxname} where type ='doc' and did is not null")
	print (len(rows), flush=True)
	for did, essay in rows: 
		if debug: print ( did, essay[0:20], flush=True) 
		dsk = gecdsk.parse({"essay":essay})

		snts = [ mkf['meta']['snt'].strip() for mkf in dsk['snt'] ]
		if not requests.es.exists(f"snts-{did}"):
			requests.es.index(index=idxname, body={"did": f"snts-{did}", 'type':'snts', 'snts': snts }, id = f"snts-{did}")

		dims = dsk['doc'] 
		if not requests.es.exists(f"dims-{did}"):
			requests.es.index(index=idxname, body={"did": f"dims-{did}", 'type':'doc-dims', 'dims': json.dumps(dims) }, id = f"dims-{did}")
		
		for mkf in dsk['snt']: 
			snt = mkf['meta']['snt'].strip()
			sntmd5 = so.md5(snt)
			if requests.es.exists(f"sntfeedback-{sntmd5}"): continue
			for k, item in mkf['feedback'].items():
				requests.es.index(index=idxname, body={"did": f"sntfeedback-{sntmd5}-{k}", 'type':'sntfeedback', 'kp': item['kp'], 'cate': item['cate'], 'short_msg':item['short_msg'], 'sent':snt}, id = f"sntfeedback-{sntmd5}-{k}")

	print(f"dsk indexing finished: {idxname}, \t| using: ", time.time() - start) 

if __name__ == '__main__':
	run('testdoc', debug=True)
	#fire.Fire(run)

'''
POST /policy_document/policy_document/222/_update
{
  "doc": {
    "tags":["VIP"]
  }
}

  es.update( # excpetion here 
            index=log['_index'],
            doc_type='_doc',
            id=log['_id'],
            body={'doc':log['_source']} # 
        )

ubuntu@dicvec-scivec-jukuu-com-flair-64-245:~/cikuu/pypi/so/inaugural$ find . -name "*.txt" -exec python ../__main__.py add {} --taglist inau \;
'''