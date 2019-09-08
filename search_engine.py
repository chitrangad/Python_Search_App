## Chitrangad Singh - 09/2019 ##

import sys
import time
import re
import os
from os import listdir
from whoosh import highlight
from whoosh import qparser
from whoosh.index import open_dir
from whoosh.scoring import TF_IDF, BM25F

test_dir = os.getcwd()+'/sample_text/'
indexdir = os.getcwd()+'/indexdir/'

def main():
	while True:
		search_input = input('Enter search string:')
		option = input('Select Search method (Hit Enter to quit): \n1. String Match \n2. Regular Expression \n3. Indexed \n: ')
		if option=='1':
		   simple_search(search_input)
		elif option == '2': 
		   reg_search(search_input)
		elif option == '3':	   
		   index_search(search_input)   
		elif option == '':
		   print("Goodbye!")
		   sys.exit()
		else:
		   print("Incorrect option. Try again")
		   pass		   

def simple_search(string):
	start_time = time.time()
	count=0
	for filename in os.listdir(test_dir) :
		with open(test_dir + filename) as currentFile:
			text = currentFile.read()
			if (string in text):
				print(text.count(string),"Matches of '"+string+ "' in:", filename)
				count+=1
	if count==0:
		print("Sorry 0 results found for:",string)
	print("Elapsed time:", str((time.time()-start_time)*1000) + " ms\n")	
	
	
def index_search(string):
	ix = open_dir(indexdir)
	qp = qparser.MultifieldParser(['content','title'], ix.schema,group=qparser.OrGroup) #search in both the indexed fields
	query = qp.parse(string)
	#print(query)
	with ix.searcher(weighting=TF_IDF()) as searcher:
		results = searcher.search(query, terms=True,limit=None)
		results.fragmenter = highlight.ContextFragmenter(maxchars=50, surround=50, ) # allows to return the text snippet and 50 chars before-after
		results.formatter = highlight.UppercaseFormatter() # highlights the string in caps on text found.
		freq = searcher.frequency("content", string)
		print("Total hits across all documents:",int(freq))
		found = results.scored_length()
		run_time = results.runtime
		if found == 0:
			top = "\nSorry " + str(found) + " results Found for "+string
		
		else:
			top = "\nTop " + str(found) + " results Found for "+string+':\n'
				 
		print(top)
		if results:
			for hit in results:
				title = hit['title']
				score = "Score: " + str(hit.score)
				print(str(title), str(score),'',sep='\n')
				print(hit.highlights("content"),'\n')
	print("Total Elapsed Time:" + str(run_time*1000) + " ms\n")

					
def reg_search(string):
	start_time = time.time()
	count=0
	for filename in os.listdir(test_dir) :
		with open(test_dir + filename) as currentFile:
			text = currentFile.read()
			try:
				cnt=len(re.findall('(?i)'+string, text))
			except:
				cnt=0
			if cnt>0:
				print(cnt,"Matches of '"+string+ "' in:", filename)
				count+=1
	if count==0:
		print("Sorry 0 results found for:",string)
	print("Elapsed time:", str((time.time()-start_time)*1000) + " ms\n")					
					
if __name__ == '__main__':
    main()
