#  Python_Search_App
## Simple Search App in Python using Whoosh and RE

The project implements 3 kinds of searches: 
1.Simple string search
2.Regular expression search using RE
3.Indexed search using Whoosh

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

For option 1, enter the exact search string. The program returns the number of hits found in each document within 'sample_files' directory. It also retursn the time taken to perform the serach. Please note the search is case sensitive and takes the literal string entered to perform the search.

For option 2, the program allows regular expression search and is case-insensitive by default.
Some examples:
1.

