# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 21:34:25 2017

@author: FURBUTT
"""

import re
import urllib.request , urllib.parse , urllib.error
from bs4 import BeautifulSoup

url = input("enter a URL")

html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, "html.parser")

tags = soup('span')
numbs_list = []

for tag in tags:
    tag = tag.decode()
    numbs = re.findall(">([0-9]+)", tag)
    for item in numbs:
        numbs_list.append(int(item))

num_sum = 0

for x in numbs_list:
    num_sum = num_sum + x

print(num_sum)