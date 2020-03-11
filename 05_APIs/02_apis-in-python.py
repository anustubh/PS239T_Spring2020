
# coding: utf-8

# # Accessing Databases via Web APIs: Lecture Code
# * * * * *

# In[]:

### GENERAL SET UP 

# Import required libraries
from __future__ import division
import requests
import urllib
import json
import math
import time

# In[]:

### LOAD API KEYS 

# Change working directory to API subfolder  
import os
os.chdir("C:/Users/Julia/OneDrive/Documents/Berkeley/2019-08_Fall/PS239T_Fall2019/05_APIs")

# Julia's computer? 
julia_computer = "TRUE"

# Note: To protect your API keys, you want to avoid uploaded them publicly to a site like GitHub. 
# To avoid this, you can save your API key files in a seperate file and instruct GitHub not to upload
# them. Julia's API keys are stored in a seperate file folder. Look at the gitignore file in this
# API subfolder. Notice how the subfolder 'api_keys_jbc/' is listed in this file but not in the
# files that you see on your computer. 

# Get API key subfolder 
if julia_computer == "TRUE":
    api_key_folder="api_keys_jbc"
else:
    api_key_folder="api_keys"

# Execute .py file with API keys 
exec(open(api_key_folder+"/02_api_keys_nyt_python.py").read())

# In[ ]:

### HOW TO USE APIs 

# In[ ]:

# ## 1. Constructing API GET Request
# 
# In the first place, we know that every call will require us to provide a) a base URL for the API, 
# b) some authorization code or key, and c) a format for the response. So let's put store those in some variables.

# First, set the parameters, starting with your API key
key=nyt_key_1

# Alternatively, you could save the API key string directly in the 'key' variable 
# key="[ADD YOUR KEY HERE]"

# Now, set base url
base_url="http://api.nytimes.com/svc/search/v2/articlesearch"

# And set response format
response_format=".json"

# You often want to send some sort of data in the URL’s query string. This data tells the 
# API what information you want. In our case, we want articles about Prince. Requests 
# allows you to provide these arguments as a dictionary, using the `params` keyword argument. 
# In addition to the search term `q`, we have to put in the `api-key` term.

# Suppose you are interested in article about Trump's impeachment. First, let's try searching 
# for all articles with the search term 'trump'.

# set search parameters
search_params = {"q":"trump",
                 "api-key":key}          

# Now we're ready to make the request. We use the `.get` method from the `requests` 
# library to make an HTTP GET Request.

# make request
r = requests.get(base_url+response_format, params=search_params)

# Now, we have a [response](http://docs.python-requests.org/en/latest/api/#requests.# Response) 
# object called `r`. We can get all the information we need from this object. For instance, 
# we can see that the URL has been correctly encoded by printing the URL. Click on the link 
# to see what happens.

print(r.url)

# Click on that link to see what it returns!

# Hmm - looks like we're getting a lot of junk unrelated to impeachment. Let's make it a little more specific:

# Let's try these search parameters instead...
search_params = {"q":"impeachment+trump",
                 "api-key":key}
r = requests.get(base_url+response_format, params=search_params)
print(r.url)

# Better!

# In[]:

# ### Challenge 1:  Adding a date range
# 
# What if we only want to search within a particular date range? The NYT Article API allows us to specify start and end dates.
# 
# Alter the `search_params` code above so that the request only searches for articles in the year 2005.
# 
# You're gonna need to look at the documentation [here](http://developer.nytimes.com/docs/read/article_search_api_v2) to see how to do this.

search_params = {"q":"impeachment+trump",
                 #YOUR CODE HERE,
                 "api-key":key}

# Uncomment to test
# r = requests.get(base_url+response_format, params=search_params)
# r.url

# In[]:

# ### Challenge 2:  Specifying a results page
# 
# The above will return the first 10 results. To get the next ten, you need to add a "page" parameter. Change the search parameters above to get the second 10 resuls. 

search_params = {"q":"impeachment+trump",
                 #YOUR CODE HERE,
                 "api-key":key}

# Uncomment to test
# r = requests.get(base_url+response_format, params=search_params)
# r.url



# In[]:

# [Challenge Answer below]

# ... 

# ... 

# ... 

# ... 

# ... 

# ... 

# ... 

# ... 

# ... 

# ... 

# ... 

# ... 

search_params = {"q":"impeachment+trump",
                 "begin_date": "20200201", # date must be in YYYYMMDD format
                 "end_date": "20200229",
                 "page": "1",
                 "api-key":key}   
r = requests.get(base_url+response_format, params=search_params)
print(r.url)

# In[]:

# ## 2. Parsing the response text

# We can read the content of the server’s response using `.text`

# Inspect the content of the response, parsing the result as text
response_text= r.text
print(response_text[:1000])

# What you see here is JSON text, encoded as unicode text. JSON stands for "Javascript object notation." It has a very similar structure to a python dictionary -- both are built on key/value pairs. This makes it easy to convert JSON response to a python dictionary.

# Convert JSON response to a dictionary
data=json.loads(response_text)
# data

# That looks intimidating! But it's really just a big dictionary. Let's see what keys we got in there.

data.keys()

# this is boring
data['status']

# so is this
data['copyright']

# this is what we want!
data['response']

data['response'].keys()

data['response']['meta'].keys()

data['response']['meta']['hits'] # whoa - that's a lot of hits!

data['response']['docs']
type(data['response']['docs'])

# That looks what we want! Let's put that in it's own variable.
docs = data['response']['docs']
docs[1]

# In[]:

# ## 3. Putting everything together to get all the articles.

# ### That's great. But we only have 10 items. The original response said we had XXX hits! 
# Which means we have to make XXX /10, or 3053 requests to get them all.*

# #### *Note - in general, most free APIs have limits on how often you can "call" them, 
# i.e., how many requests you can send. For the NYT, the daily limit is 1000, and you are 
# limited to 5 calls/sec. At first, this might sound like plenty--but in general, it's not. 
# You'll want to be creative with your search terms and date restrictions to ensure that 
# you have a manageable number of calls to the API. Going forward, we're just going to look 
# at the 2016 results - a much more manageable 523 (53 calls). 
# 
# ### Sounds like a job for a loop! 
# 
# But first, let's review what we've done so far.

# set base url
base_url="http://api.nytimes.com/svc/search/v2/articlesearch"

# set response format
response_format=".json"

# set search parameters
search_params = {"q":"impeachment+trump",
                 "begin_date": "20200301", # date must be in YYYYMMDD format
                 "end_date": "20200302",
                 "api-key":key}

# make request
rr = requests.get(base_url+response_format, params=search_params)
    
# convert to a dictionary
data=json.loads(rr.text)
    
# get number of hits
hits = data['response']['meta']['hits']
print("number of hits: " + str(hits))
    
# get number of pages
pages = int(math.ceil(hits/10))

# Now, make an empty list where we'll hold all of our docs for every page
all_docs = [] 
    
# now we're ready to loop through the pages
for i in range(pages):
    print("collecting page " + str(i))
        
    # set the page parameter
    search_params['page'] = i
        
    # make request
    rr = requests.get(base_url+response_format, params=search_params)
    
    # get text and convert to a dictionary
    data=json.loads(rr.text)
        
    # get just the docs
    docs = data['response']['docs']
        
    # add those docs to the big list
    all_docs = all_docs + docs
    
    # add pause
    time.sleep(7)

print(data)

len(all_docs)

# In[ ]:

# ## 4. Make a function

# Turn the code above into a function that inputs a search term, and returns all the documents containing that 
# search term between two dates.

def apisearch(q, begin, end, key, pg):
    # set base url
    base_url="http://api.nytimes.com/svc/search/v2/articlesearch"
    # set response format
    response_format=".json" 
    search_params = {"q": q,
                     "begin_date": begin,
                     "end_date": end,
                     "page": pg,
                     "api-key":key}      
    # make request
    r = requests.get(base_url+response_format, params=search_params)
    print(r.url)

# Now, try testing the function... 
apisearch(q="Clinton", begin="20200101", end="20200307", pg="1", key=key)


# In[ ]:

# ## 4. Formatting and Exporting

# Let's take another look at one of these documents.
all_docs[0]

# This is all great, but it's pretty messy. What we’d really like to to have, eventually, 
# is a CSV, with each row representing an article, and each column representing something 
# about that article (header, date, etc). As we saw before, the best way to do this is to 
# make a lsit of dictionaries, with each dictionary representing an article and each dictionary 
# representing a field of metadata from that article (e.g. headline, date, etc.) We can do 
# this with a custom function:

def format_articles(unformatted_docs):
    '''
    This function takes in a list of documents returned by the NYT api 
    and parses the documents into a list of dictionaries, 
    with 'id', 'header', and 'date' keys
    '''
    formatted = []
    for i in unformatted_docs:
        dic = {}
        dic['id'] = i['_id']
        dic['headline'] = i['headline']['main'].encode("utf8")
        dic['date'] = i['pub_date'][0:10] # cutting time of day.
        formatted.append(dic)
    return(formatted) 

# Now, run this function on our dictionary of docs
all_formatted = format_articles(all_docs)

# And look at the result
all_formatted[:5]

# Now, let's export the data to a CSV.
import csv
keys = all_formatted[0].keys()
with open('data_raw/article_API.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(all_formatted)
    
# In[ ]:

# ## Challenge, Part A: Add caption and one or two other fields to the format_articles() function 
    
    
    
# ## Challenge, Part B: Export new dataset as 'article_API_extra_fields.csv' to the same 'data_raw' subfolder
    
    



