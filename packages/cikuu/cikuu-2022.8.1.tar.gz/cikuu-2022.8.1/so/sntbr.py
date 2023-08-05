# 2023.5.2,  dsk including  sntbr, if not dsk, start standalone sntbr  
import so, requests,time, fire,json, spacy

if not hasattr(spacy, 'nlp'):
	from spacy.lang import en
	spacy.sntbr		= (inst := en.English(), inst.add_pipe("sentencizer"))[0]
	#spacy.nlp		= spacy.load('en_core_web_sm')

def run(idxname, debug:bool=False):
	''' testdoc, 2023.5.2 '''
	so.check(idxname) 
	start = time.time()
	rows = so.cursor_rows(f"select did, doc from {idxname} where type ='doc' and did is not null")
	print (len(rows), flush=True)
	for did, essay in rows: 
		if debug: print ( did, essay[0:20], flush=True) 
		doc = spacy.sntbr(essay) 

		snts = [ sp.text.strip() for sp in doc.sents ]
		if not requests.es.exists(index=idxname, id=f"snts-{did}"):
			requests.es.index(index=idxname, body={"did": f"snts-{did}", 'pid': did, 'type':'snts', 'snts': snts, 'sntnum':len(snts) }, id = f"snts-{did}")

		for sp in doc.sents
			snt = sp.text.strip()
			sntmd5 = so.md5(snt)
			if not requests.es.exists(index=idxname, id=f"snt-{sntmd5}"): # sntbr 
				requests.es.index(index=idxname, body={"did": f"snt-{sntmd5}",'pid': did, 'type':'snt', 'sent': snt, 'tc': len(sp)}, id = f"snt-{sntmd5}")

	print(f"sntbr indexing finished: {idxname}, \t| using: ", time.time() - start) 

if __name__ == '__main__':
	run('testdoc', debug=True)
	fire.Fire(run)

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