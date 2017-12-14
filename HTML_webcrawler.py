# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 22:12:39 2017

@author: FURBUTT
"""

import urllib.request , urllib.parse , urllib.error
from bs4 import BeautifulSoup

iv = 0
fiv = 0

def webcrawlrepeat(y):
    global fiv
    if fiv < 8:  #modify here for amount of tags opened
        web = y
        print(fiv)
        print(web)
        webcrawl(web)

        
        
    

def webcrawl(x):
    url = x
    global fiv
    global iv
    
    html = urllib.request.urlopen(url).read()

    soup = BeautifulSoup(html, "html.parser")

    tags = soup('a')

    for tag in tags:
        newrl= tag.get("href",None)
        iv +=1
        
        if iv ==18:   #modify here for which tag you want
            iv = 0   
            fiv += 1
            webcrawlrepeat(newrl)
            

               
    

url = input("enter a URL")

webcrawl(url)