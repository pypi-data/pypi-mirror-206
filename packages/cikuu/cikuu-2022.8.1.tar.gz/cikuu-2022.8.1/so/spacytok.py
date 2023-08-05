# 2023.5.2,  parse tok using spacy,  after sntbr/dsk,  assume snt is ready, in the index 
import so, requests,time, fire,json, spacy
spacy.nlp = spacy.load('en_core_web_sm')

def run(idxname, debug:bool=False):
	''' testdoc, 2023.5.2 '''
	so.check(idxname) 
	start = time.time()
	rows = so.cursor_rows(f"select did, sent from {idxname} where type ='snt' and did is not null")
	print (len(rows), flush=True)
	for did, snt in rows: 
		if debug : print ( did, snt , flush=True) 
		doc = spacy.nlp(snt) 
		for t in doc: 
			requests.es.index(index=idxname, body={"did": f"tok-{did}-{t.i}", 'pid': did, 'type':'tok', 'lex': t.text, 'lem':t.lemma_, 'pos':t.pos_, 'tag':t.tag_, 'dep':t.dep_, 'govlem': t.head.lemma_, 'govpos': t.head.pos_ }, id = f"tok-{did}-{t.i}")

	print(f"spacytok indexing finished: {idxname}, \t| using: ", time.time() - start) 

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