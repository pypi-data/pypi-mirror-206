# 2023.5.1  .# 2022-2-13  cp from cikuu/bin/es.py 
import so, requests,time

def addfolder(self, folder:str, pattern=".txt", idxname=None): 
	''' folder -> docbase, 2022.1.23 '''
	if idxname is None : idxname=  folder
	print("addfolder started:", folder, idxname, self.es, flush=True)
	if not self.es.indices.exists(index=idxname): self.es.indices.create(index=idxname, body=config)
	for root, dirs, files in os.walk(folder):
		for file in files: 
			if file.endswith(pattern):
				self.add(f"{folder}/{file}", idxname = idxname) 
				print (f"{folder}/{file}", flush=True)
	print("addfolder finished:", folder, idxname, self.es, flush=True)

def add(infile, idxname="testdoc", taglist:str=None):
	''' add doc only , 2023.5.1 '''
	import hashlib
	if not requests.es.indices.exists(index=idxname): requests.es.indices.create(index=idxname, body=so.config)
	start = time.time()
	text = open(infile, 'r').read().strip() 
	did	 = hashlib.md5(text.encode("utf8")).hexdigest()
	requests.es.index(index=idxname, body={"did": f"doc-{did}", "doc":text,  "filename": infile, 'type':'doc', 'tags':[] if taglist is None else taglist.strip().split(',') if isinstance(taglist, str) else taglist }, id = f"doc-{did}")
	print(f"{infile} is finished, \t| using: ", time.time() - start) 

def init(idxname):
	''' init a new index '''
	if requests.es.indices.exists(index=idxname):requests.es.indices.delete(index=idxname)
	requests.es.indices.create(index=idxname, body=so.config) #, body=snt_mapping
	print(">>finished " + idxname )

if __name__ == '__main__':
	#print( requests.eshost)
	import fire
	fire.Fire()

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