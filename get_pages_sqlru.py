#!/usr/bin/env python3

import urllib.request as req
from bs4 import BeautifulSoup
import binascii

def check_page(url, topic,f):
    print("check page:" + url);        
    auth = req.HTTPBasicAuthHandler()
    response = req.urlopen(url)
    soup = BeautifulSoup(response.read())
    if  search_str !='' and soup.get_text().lower().find(search_str) == -1:
        return
    if author_name == '':
         f.write(topic + '|' + url + '\n')
         print(topic + '|' + url)
         return
    tds_author = soup.find_all("a")    
    for i in range(len(tds_author)):
         current_author_name = tds_author[i].get_text().strip().lower()
         if current_author_name == author_name:
              f.write(topic + '|' + url + '\n')
              print(topic + '|' + url)
              return

def get_page_urls(url,topic,f):
    base_url = url[0 : url.rfind('/')]
    print("Get page URLS: " + topic + " " + base_url)   
    auth = req.HTTPBasicAuthHandler()
    response = req.urlopen(url)
    soup = BeautifulSoup(response.read())
    links=soup.find_all("a")
    max_page_no = 0
    for element in links:
         try:
              link_url = element["href"]
         except:
             continue
         print('Checking link: ' + link_url)
         link_url = link_url[0 : link_url.rfind('/')]
         if  (link_url != base_url) and (link_url.find(base_url + '-') != -1) and (link_url!=url+'-1'):
              try:
                  page_no = int(link_url.replace(base_url+'-', ''))
              except:
                  page_no = 0
              if page_no > max_page_no:
                   max_page_no = page_no
    if max_page_no > 0:
         for page_no in range(max_page_no-1):
              check_page(base_url+'-'+str(page_no+2), topic,f)
    else:
         check_page(base_url, topic,f)
         
def get_topics(url,f):
    print("Get topics:" + url)
    auth = req.HTTPBasicAuthHandler()
    response = req.urlopen(url)
    soup = BeautifulSoup(response.read())    
    tds_topic = soup.find_all("td", class_="postslisttopic")
    for i in range(len(tds_topic)):
         if not((tds_topic[i].get_text().find("Важно:") != -1) and (topic.find("Важно:") == -1)):
              href  = tds_topic[i].find_all("a")[0]["href"]
              topic = tds_topic[i].find_all("a")[0].get_text()
              if href != url:
                   get_page_urls(href,topic,f)
    return

def to_hex(s):
        res = ""
        for i in range(len(s)):
            enc_char = str(str.encode(s[i],'1251'))
            if (enc_char[2:4] == '\\x'):
                enc_char= '%'  + enc_char[4:6]
            else:
                enc_char=enc_char[2:3]
            res = res + enc_char
        return res

def main():
    global author_name
    global search_str
    author_name = input("Enter author name, empty for all authors: ").lower()
    search_str = input("Enter search string, if any: ").lower()
    file_name = input("Output file name: (sqlru.csv by default): ")
    if file_name == '':
         file_name = 'sqlru.csv'
    f = open(file_name, 'w')
    print("---------------------------------------------------------")
    f.write('Topic|URL\n')
    get_topics('http://www.sql.ru/forum/actualsearch.aspx?a=' + to_hex(author_name) + '&search=' + to_hex(search_str) + '&ma=1',f)
    
if __name__ == '__main__':
    main()
