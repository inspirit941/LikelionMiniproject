
# coding: utf-8

# In[7]:

import requests
import pandas as pd
import json
import re
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
get_ipython().magic('matplotlib inline')
from pandas.io.json import json_normalize
requests.packages.urllib3.disable_warnings()
from matplotlib import font_manager,rc
font_location = "C:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
print(font_name)
rc('font',family = font_name)
matplotlib.rcParams['font.family']
matplotlib.matplotlib_fname()
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import datetime
import glob


# In[3]:

response = requests.get('https://kin.naver.com/hall/index.nhn?year=2017&month=0',verify=False)


# In[19]:

response.text


# In[20]:

html = response.text


# In[21]:

soup = bs(html, 'html.parser')


# In[22]:

soup


# In[24]:

soup.select('div.content > ul > li.indicator > p.value > em')


# In[17]:

soup.select('div.content > ul > li.indicator > p.tit')


# In[15]:

temp=soup.select('div.content > ul > li.indicator > p')


# In[16]:

temp


# In[25]:

for idx,i in enumerate(temp):
    print(idx)
    print(i.text)


# In[35]:

title = soup.select('div.content > ul > li.indicator > p.tit')


# In[63]:

5 % 3


# In[36]:

title


# In[38]:

titletext= []
for tit in title:
    titletext.append(tit.text)


# In[39]:

titletext


# In[44]:

valuestext=[]
for value in values:
    valuestext.append(value.text)


# In[27]:

title =[]
value =[]
year = []


# In[28]:

for i in range(2002,2018):
    print(i)
    response = requests.get('https://kin.naver.com/hall/index.nhn?year='+str(i)+'&month=0',verify=False)
    html = response.text
    soup = bs(html, 'html.parser')
    values = soup.select('div.content > ul > li.indicator > p')
    print(values)
    for idx, data in enumerate(values):
        
        if idx % 2 ==0:
            year.append(i)
            title.append(data.text)
        else:
            value.append(data.text)


# In[32]:

dataset= {
    'year':year,
    'title':title,
    'value':value
}


# In[34]:

df = pd.DataFrame(dataset)


# In[31]:

df


# In[35]:

df.value = df.value.map(lambda x:re.sub(',','',x))


# In[37]:

df.value = df.value.astype(float)


# In[38]:

table =pd.pivot_table(df,'value','year','title')


# In[39]:

table


# In[159]:

table.iloc[:,:1].plot(figsize=(14,9))


# In[161]:

table.iloc[:,2:3].plot(figsize=(14,9))


# In[164]:

table.to_excel('지식인데이터크롤링결과.xlsx')


# In[ ]:



