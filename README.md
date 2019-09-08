#  Python_Search_App
## Simple Search App in Python using Whoosh and RE

The project implements 3 kinds of searches: 

1. Simple string search
2. Regular expression search using RE
3. Indexed search using Whoosh

## Usage
Copy the files indexer.py and searcher.py in the directory of your choice
Make sure the files you want to index and search are placed in the subdirectory names 'sample_files' in the same folder.
Only text files are supported.

For indexing, run indexer.py. The program will index the files present in 'sample_files'
After indexing is finished a folder named indexdir should be created within the parent folder.

To search, run the searcher.py
The program will prompt for search string.
Next, the program will ask the type of search to perform:
1. Simple search
2. Regular expression search
3. Indexed search
To quit simply hit Enter without entering anything.

For option 1: 
Enter the exact search string. The program returns the number of hits found in each document within 'sample_files' directory. It also retursn the time taken to perform the serach. Please note the search is case sensitive and takes the literal string entered to perform the search.

For option 2: 
The program allows regular expression search and is case-insensitive by default.

Some examples:

1 rub[ye]
Match "ruby" or "rube"

2 [0-9]
Match any digit; same as [0123456789]

3 [a-z]
Match any lowercase ASCII letter

4	ruby?
Match "rub" or "ruby": the y is optional

5 ruby*
Match "rub" plus 0 or more y

6 ^Python
Match "Python" at the start of a string or internal line

7 Python$
Match "Python" at the end of a string or line

8 \bPython\b
Match "Python" at a word boundary

For option 3: 
Enter search string or phrase. The app does an 'OR' search for multiple words.
Search is conducted both on file names and the content.
Following is returned:
- Total number of hits across all the documents.
- Top n documents where the search is successful along with the relative score based on relevance.
- Total time taken to perform the search.

Since the serach is indexed, it's not possible to return hits for each individual document as the indexes are cumulative across sample files.

