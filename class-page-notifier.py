#!/bin/python

from bs4 import BeautifulSoup
from urllib2 import urlopen
import json
import sqlite3

class ClassPageNotifier:
    def __init__(self):
        self.urls = {}
        self.email = ''
        f =  open('/home/nerraw/dev/class-page-notifier/config.json')
        configs = json.load(f)
        self.urls = configs['urls']
        self.email = configs['email']
        f.close()
            
            
            


    def web_page_updated(self, url):
        changed = False
        print(len(url))
        conn = sqlite3.connect('/home/nerraw/dev/class-page-notifier/classes.db')
        cursor = conn.cursor()
        cursor.execute("SELECT html from pages where url=?", [url])
        old_page = cursor.fetchone()
        page = urlopen(url).read()
        if(old_page is None or old_page[0] != page):
            cursor.execute('''INSERT OR REPLACE INTO pages (url, html)
            VALUES (?,?)''', [url, page])
            conn.commit()
            changed = True

        conn.close()
        return changed










        
    
    
    
    
    
    
    
    
