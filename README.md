# SQL.RU-parser written in Python 3.5
get_topics_sqlru.py

Forms a file with a list of all topics from SQL forums in the following format:
Section|Topic|Author|Date|URL
It can be imported to MS Excel as a CSV file

1. Run get_pages_sqlru.py

2. When prompted ented output file name.

get_pages_sqlru.py.

Forms a file with a list of all pages from SQL.RU forums. The list can be filtered by author name and given search string. Unlike built-in SQL.RU search, a separate line is formed for every page, not for every topic. It its move convenient because a topic can contain hundreeds of pages and only one of them contains the information required.
The list is returned in the following format:
Topic name|Page URL.
It can be imported to MS Excel as a CSV file

1. Run get_pages_sqlru.py

2. When prompted enter author name if necessary.

3. When prompted enter search string if necessary.

4. When prompted ented output file name.


