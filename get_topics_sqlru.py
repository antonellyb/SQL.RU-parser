#!/usr/bin/env python3

import urllib.request as req
import binascii
import datetime
from bs4 import BeautifulSoup

def get_html(url,padding):
    print(url)
    try:
         response = req.urlopen(url)
    except:
        sleep(1)
        get_html(url,padding)
        return
    soup = BeautifulSoup(response.read())
    if padding == '':
         links = soup.find_all("a", class_="forumLink")
         for element in links:
             href = element["href"]            
             if href != url and href !="http://www.sql.ru/forum" and href != "http://www.sql.ru/forum/sqlru-3-days":    
                 get_html(href,element.get_text())         
    else:
         tds_topic = soup.find_all("td", class_="postslisttopic")
         tds_author = soup.find_all("td", class_="altCol", style="")
         tds_date = soup.find_all("td", class_="altCol", style="text-align:center")
         for i in range(len(tds_topic)):

                   topic =tds_topic[i].find_all("a")[0].get_text();
                   if not((tds_topic[i].get_text().find("Важно:") != -1) and (topic.find("Важно:") == -1)):
                        try:
                             if len(tds_author[i].find_all("a"))>0:    
                                  author = tds_author[i].find_all("a")[0].get_text().strip();
                             else:
                                  author = tds_author[i].get_text().strip();
                        except:
                             author = ""
                        try:
                             date = tds_date[i].get_text().strip();
                             date = date.replace(" янв ",'-01-');                         
                             date = date.replace(" фев ",'-02-');
                             date = date.replace(" мар ",'-03-');
                             date = date.replace(" апр ",'-04-');
                             date = date.replace(" май ",'-05-');
                             date = date.replace(" июн ",'-06-');
                             date = date.replace(" июл ",'-07-');
                             date = date.replace(" авг ",'-08-');
                             date = date.replace(" сен ",'-09-');
                             date = date.replace(" окт ",'-10-');
                             date = date.replace(" ноя ",'-11-');
                             date = date.replace(" дек ",'-12-');
                             date = date.replace("сегодня", datetime.date.today().strftime("%d-%m-%y"))                             
                             date = date.replace("вчера"  , (datetime.date.today() - datetime.timedelta(days=1)).strftime("%d-%m-%y"))
                        except:
                             date = '';
                        href = tds_topic[i].find_all("a")[0]["href"]
                        if href != url and href !='http://www.sql.ru/forum':
                            f.write(padding + '|')
                            f.write(topic + '|')
                            f.write(author + '|')
                            f.write(date + '|')
                            f.write(href + '\n')
         links=soup.find_all("a")
         max_page_no = 0;
         for element in links:
              href = element["href"]
              if  (href != url) and (href.find(url + '/') != -1) and (href!=url+'/1'):
                   page_no = int(href.replace(url+'/', ''))
                   if page_no > max_page_no:
                        max_page_no = page_no
         if max_page_no > 0:
              for page_no in range(max_page_no-1):
                   get_html(url+'/'+str(page_no+2),padding)
    return

def main():
    global f

    file_name = input("Output file name: (sqlru.csv by default): ")
    if file_name == '':
         file_name = 'sqlru.csv'
    f = open(file_name, 'w', encoding='utf8')
    print("---------------------------------------------------------")
    f.write('Section|Topic|Author|Date|URL\n');
    get_html('http://www.sql.ru/forum','')

if __name__ == '__main__':
    main()
