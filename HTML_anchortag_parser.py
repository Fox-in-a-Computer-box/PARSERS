# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 21:01:24 2017

@author: FURBUTT
"""

import urllib.request , urllib.parse , urllib.error
from bs4 import BeautifulSoup

url = input("enter a URL")

html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, "html.parser")

tags = soup('a')

for tag in tags:
    print(tag.get("href",None))
    
    