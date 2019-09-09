#  Python_Search_App
## Simple Search App in Python using Whoosh and RE

The project implements 3 kinds of searches: 

1. Simple string search
2. Regular expression search using RE
3. Indexed search using Whoosh

## Usage
Install following libraries using 'pip install': whoosh, re

Copy the files indexer.py and search_engine.py in the directory of your choice
Make sure the files you want to index and search are placed in the subdirectory names 'sample_files' in the same folder.
Only text files are supported.

For indexing, run indexer.py. The program will index the files present in 'sample_files'
After indexing is finished a folder named indexdir should be created within the parent folder.

To search, run the search_engine.py
The program will prompt for search string.
Next, the program will ask the type of search to perform:
1. Simple search
2. Regular expression search
3. Indexed search

To quit, simply hit Enter.

**Option 1:**
Enter the exact search string. The program returns the number of hits found in each document within 'sample_files' directory. It also returns the time taken to perform the serach. Please note the search is case sensitive and takes the literal string entered to perform the search.

**Option 2:**
The program allows regular expression search and is case-insensitive by default.

Some examples:

* rub[ye]
Match "ruby" or "rube"

* [0-9]
Match any digit; same as [0123456789]

* [a-z]
Match any lowercase ASCII letter

* ruby?
Match "rub" or "ruby": the y is optional

* ruby*
Match "rub" plus 0 or more y

* ^Python
Match "Python" at the start of a string or internal line

* Python$
Match "Python" at the end of a string or line

* \bPython\b
Match "Python" at a word boundary

**Option 3:** 
Enter search string or phrase. The app does an 'OR' search for multiple words.
Search is conducted both on file names and the content.
Following information is returned:
- Total number of documents with the string.
- Search score based on string location and occurrence.
- Total time taken to perform the search.

It's not possible to return hits for individual documents as the indexes are stored for the entire set.

## Interface and Output
```
indexing: <file1>
indexing: <file2>
indexing: <file3>
Done!
Total documents indexed: 3
Press any key to exit..


Enter search string:<string>
Select Search method (Press Enter to quit):
1. String Match
2. Regular Expression
3. Indexed
:

Search results: 

X matches of <string> in <filename> 
Elapsed time: xx.xx ms
```

### Overview:

The app has 3 parts:

1st part uses simple Python string seach using string comparison. The search is limited in functionality and can only look for exact word or word matching the substring. the search is limited by physical memory and large documents may throw memory error. It may not be practical for big documents.

2nd part uses Python's RE library to perform regex search. It is more flexible as one can use wildcards and do caseless searches etc. Again, this is limited in size and not scalable.

3rd part uses Whoosh, an open source Python library. Whoosh provides full-indexing and searching library. 
It provides several indexing and searching functions that allows quick retrieval. 

>This is implemented in 2 parts - indexing and searching.
Indexing uses a schema containing the filename and the file content. 
The indexing currently includes stop words for the purpose of the demo. This can be rmoved by deleting the parameter '(stoplist=None)' in the indexer.

Each time new documents are added to the 'sample_files' directory the indexing should be rerun to update the index.

>Once indexed, search is performed by parsing the keywords and matching the keywords within index.

>The app uses TFIDF search algorithm - term frequency over inverse document frequency. This alogorithm, though not as accurate as BM25 is much faster in retrieval. This can be changed based on the specific usecase.
