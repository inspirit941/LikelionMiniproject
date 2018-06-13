
# coding: utf-8

# In[1]:

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
from bs4 import BeautifulSoup as bs4
import datetime
import glob


# In[2]:

response = requests.get('http://www.enuri.com/lsv2016/ajax/getListGoods_ajax.jsp?random_seq=251&pageNum=1&pageGap=90&tabType=0&cate=240616&keyword=&brand=&factory=&shop_code=&prtmodelno=&gb1=&gb2=&sponsorList=&infoAdList=&IsDeliverySumPrice=N&IsJungoPriceRemove=N&m_price=&start_price=&end_price=')


# In[7]:

data = json.loads(response.text)


# In[13]:

data['lpList'][0]['spec_vip_tag']


# In[98]:

i=0
j=1
dtarray=[]
modelname=[]
y=True
x=True


# In[91]:

response = requests.get('http://www.enuri.com/lsv2016/ajax/getListGoods_ajax.jsp?random_seq=251&pageNum=9&pageGap=90&tabType=0&cate=240616&keyword=&brand=&factory=&shop_code=&prtmodelno=&gb1=&gb2=&sponsorList=&infoAdList=&IsDeliverySumPrice=N&IsJungoPriceRemove=N&m_price=&start_price=&end_price=')
        


# In[94]:

len(json.loads(response.text)['lpList'])


# In[95]:

response = requests.get('http://www.enuri.com/lsv2016/ajax/getListGoods_ajax.jsp?random_seq=251&pageNum=8&pageGap=90&tabType=0&cate=240616&keyword=&brand=&factory=&shop_code=&prtmodelno=&gb1=&gb2=&sponsorList=&infoAdList=&IsDeliverySumPrice=N&IsJungoPriceRemove=N&m_price=&start_price=&end_price=')
        


# In[96]:

len(json.loads(response.text)['lpList'])


# In[106]:

i=0
j=1
dtarray=[]
modelname=[]
x=True


# In[107]:

while True:
        response = requests.get('http://www.enuri.com/lsv2016/ajax/getListGoods_ajax.jsp?random_seq=251&pageNum='+str(j)+'&pageGap=90&tabType=0&cate=240616&keyword=&brand=&factory=&shop_code=&prtmodelno=&gb1=&gb2=&sponsorList=&infoAdList=&IsDeliverySumPrice=N&IsJungoPriceRemove=N&m_price=&start_price=&end_price=')
        data=json.loads(response.text)
        print(str(j)+'번째 response')
        i=0
        j+=1
        x=True
        if len(data['lpList'])==0:
            print('lpList 값이 0이므로 반복문 종료')
            break
        while x is True:
            try:
                dtarray.append(data['lpList'][i]['spec_vip_tag'])
                modelname.append(data['lpList'][i]['strModelName'])
                i+=1
                
            except:
                x=False
                print(len(modelname))
        


# In[102]:

len(modelname)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



