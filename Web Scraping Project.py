#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import requests
from bs4 import BeautifulSoup
Product_name=[]
Prices=[]
Rating =[]


# In[ ]:


for i in range(1,11):
 url ="https://www.flipkart.com/search?q=mobile+under+30000&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_7_13_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_7_13_na_na_na&as-pos=7&as-type=RECENT&suggestionId=mobile+under+30000&requestId=ee6c8b9b-9b57-4fbe-b4ba-770a30659d12&as-searchtext=mobile+under+30000&page="+str(i)
 r =requests.get(url)
 soup= BeautifulSoup(r.text,"lxml")
 box=soup.find("div",class_="_1YokD2 _3Mn1Gg")

 names =box.find_all("div",class_="_4rR01T")
 for i in names:
    name=i.text
    Product_name.append(name)
 Price =box.find_all("div",class_="_30jeq3 _1_WHN1")
 for i in Price:
    name=i.text
    Prices.append(name)
 desc =box.find_all("ul",class_="_1xgFaf")
 for i in desc:
    name=i.text
    Description.append(name)
 rat =box.find_all("div",class_="_3LWZlK")
 for i in rat:
    name=i.text
    Rating.append(name)

