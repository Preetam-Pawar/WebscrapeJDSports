#!/usr/bin/env python
# coding: utf-8

# In[7]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[8]:
#Assign URL 

URL ="https://www.jdsports.ie/men/mens-clothing/"


# In[9]:


#Header for request
HEADERS= ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0','Accept-Language':'en-US,en;q=0.5'})


# In[11]:


#http Request
webpage= requests.get(URL, headers= HEADERS)


# In[14]:


type(webpage.content)


# In[17]:


#soup object containing all data
soup= BeautifulSoup(webpage.content, "html.parser")
soup


# In[26]:


#fetch links as list of tag objects
links = soup.find_all("a", attrs={'class':'itemImage'})


# In[27]:


Link=links[0].get('href')


# In[30]:


product_list= "https://www.jdsports.ie/" + Link
product_list


# In[31]:


new_webpage= requests.get(product_list, headers= HEADERS)
new_webpage


# In[32]:


#soup object containing all data
new_soup= BeautifulSoup(new_webpage.content, "html.parser")
new_soup


# In[47]:


new_soup.find('h1', attrs={"itemprop":'name'}).text.strip()


# In[61]:


new_soup.find('span', attrs={"class":'pri'}).text.strip()


# In[62]:


new_soup.find('span', attrs={"class":'product-code'}).text.strip()


# In[68]:





# In[ ]:




