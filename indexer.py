## Chitrangad Singh - 09/2019 ##

import os
import os.path
from whoosh.index import create_in
from whoosh.index import open_dir
from whoosh.index import exists_in
from whoosh.analysis import StemmingAnalyzer, StandardAnalyzer
from whoosh.fields import *

test_dir = os.getcwd()+'/sample_text/'
indexdir = os.getcwd()+'/indexdir/'
	
def main():
    # Define the schema for indexing. we have only filename(title) and the content
	schema = Schema(
			title=TEXT(stored=True, phrase=True, sortable=True),
			content=TEXT(analyzer=StandardAnalyzer(stoplist=None), stored=False, phrase=True, sortable=True)) # include stopwords for full search
	if not os.path.exists(indexdir):
		os.mkdir(indexdir)

	ix = create_in(indexdir, schema)
	writer = ix.writer()

	number_indexed = 0
	for filename in os.listdir(test_dir):
		print_filename = str(filename.encode('utf-8'))
		if print_filename[0:2] == "b\'" and print_filename.endswith("\'"):
			print_filename = print_filename[2:-1]
		print("indexing: "+print_filename)
		number_indexed += 1
		try:
			f = open(test_dir + "\\" + filename, 'r')
			content = f.read()
			writer.add_document(title=filename, content=content)
		except:
			print("Failed to index",filename)
			continue
	writer.commit()
	print("Done!")
	print("Total documents indexed: "+str(number_indexed))
	dummy = input("Press any key to exit..")
	sys.exit()

if __name__ == "__main__":
	main()

