#!/usr/bin/env python
# coding: utf-8

# In[20]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np


# In[21]:


# Function to extract Product Title
def get_title(soup):

    try:
        # Outer Tag Object
        title = soup.find("h1", attrs={"itemprop":'name'})
        
        # Inner NavigatableString Object
        title_value = title.text

        # Title as a string value
        title_string = title_value.strip()

    except AttributeError:
        title_string = ""

    return title_string

# Function to extract Product Price
def get_price(soup):

    try:
        price = soup.find("span", attrs={'class':'pri'}).string.strip()

    except AttributeError:

        try:
            # If there is some deal price
            price = soup.find("span", attrs={'class':'pri'}).string.strip()

        except:
            price = ""

    return price

# Function to extract Product Code
def get_productcode(soup):

    try:
        productcode = soup.find("span", attrs={'class':'product-code'}).string.strip()

    except AttributeError:

        try:
            # If there is some 
            productcode = soup.find("span", attrs={'class':'product-code'}).string.strip()

        except:
            productcode = ""

    return productcode


# In[22]:


if __name__ == '__main__':

    # add your user agent 
    HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0', 'Accept-Language': 'en-US, en;q=0.5'})

    # The webpage URL
    URL = "https://www.jdsports.ie/men/mens-clothing/"

    # HTTP Request
    webpage = requests.get(URL, headers=HEADERS)

    # Soup Object containing all data
    soup = BeautifulSoup(webpage.content, "html.parser")

    # Fetch links as List of Tag Objects
    links = soup.find_all("a", attrs={'class':'itemImage'})

    # Store the links
    links_list = []

    # Loop for extracting links from Tag Objects
    for link in links:
            links_list.append(link.get('href'))

    d = {"title":[], "price":[], "productcode":[]}
    
    # Loop for extracting product details from each link 
    for link in links_list:
        new_webpage = requests.get("https://www.jdsports.ie/" + link, headers=HEADERS)

        new_soup = BeautifulSoup(new_webpage.content, "html.parser")

        # Function calls to display all necessary product information
        d['title'].append(get_title(new_soup))
        d['price'].append(get_price(new_soup))
        d['productcode'].append(get_productcode(new_soup))
      
    
    webscrape_df = pd.DataFrame.from_dict(d)
    webscrape_df['title'].replace('', np.nan, inplace=True)
    webscrape_df = webscrape_df.dropna(subset=['title'])
    webscrape_df.to_csv("Webscrape_data.csv", header=True, index=False)


# In[25]:


webscrape_df


# In[ ]:




