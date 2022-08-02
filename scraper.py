#!/usr/bin/env python
# coding: utf-8

# # Scraping news.au.com
# ** Writing a scraper on "news.au.com" that scrapes news every few hours

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[3]:


#pulling in the news.com.au webpage:-

response = requests.get("https://www.news.com.au/")

doc = BeautifulSoup(response.text)


# In[4]:


# now we want to scrape all the headlines on the page.
# Checking the web structure of the page

# Headline here is in h4 with a class of "storyblock_title"


# In[5]:


doc.select(".storyblock_title")


# In[ ]:


#We get the links(that are under "a" tag) that are insde of "storyblock_title"


# In[6]:


titles = doc.select(".storyblock_title a")
titles


# In[7]:


# Now we will pull our headline links along with the text in our headlines:-

for title in titles:
    #title
    print(title.text.strip())
    #links
    print(title['href'])
    
# So we see that our code works here


# In[ ]:


# Now  we want to turn our headlines that we gathered into a csv,into a dataframe.
    
    #In order to turn this into pandas,we will create a list of dictionaries with the heading under title and its url..
        #...under link
    
    # We do this below:-
    
    # 1.First we create an empty dictionary called "row"
    # 2.then we say our row['title'] is the title code for heading and row['url'] is the url code that we wrote above...
        #...in for loop.
    #3.Because what we want is a list of dictionaries, we create a list at the very top called datapoints


# In[8]:


# Start with an empty list:-
datapoints = []

for title in titles:
    #Go through each title, building a dictionary with a 'title' and a 'url'
    row = {}
    #title
    row['title'] = title.text.strip()
    #links
    row['url'] = title['href']
    
    # Then add it to our list of rows:-
    datapoints.append(row)
    
    #append means to add--it works like the plus symbol we had in our for loop at the top

# then we are going to make a dataframe from it!     
datapoints

# We turn this into a dataframe:-

df = pd.DataFrame(datapoints)
df.head()


# In[9]:


#Now we have a dataframe.
# We now save this as csv in our working directory:
df.to_csv("news_au.csv",index = False)


# In[ ]:


# Now we want to scrape the news.au website every few hours to keep track of what they are doing

# We now create a folder called automatic-scraper in our working directory.
# Now we want to run our code every few hours to check the changes.This we want to be done automatically

# We will use python files for this.(ie. py files in VS code) 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




