# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 19:31:07 2020

@author: anust
"""

import pandas as pd
import numpy as np
import os
import pandas as pd
import re
from nltk.tokenize import word_tokenize


# 
# Read in some Amazon reviews from earlier into a list called `reviews`. Each element of the list is a string, representing the text of a single review. Try to:
# - Tokenize each review
# - Separate each review into sentences
# - Strip all whitespace
# - Make all characters lower case
# - Replace any URLs and digits
# 
# Then find the most common 50 words.

# In[42]:


DATA_DIR = 'data'

import glob 
fnames = os.path.join(DATA_DIR, 'amazon', '*.csv')
fnames = glob.glob(fnames)
reviews = []
column_names = ['id', 'product_id', 'user_id', 'profile_name', 'helpfulness_num', 'helpfulness_denom',
               'score', 'time', 'summary', 'text']

for fname in fnames[:2]:
    df = pd.read_csv(fname, names=column_names)
    text = list(df['text'])
    reviews.extend(text)


# In[52]:



url_pattern = r'https?:\/\/.*[\r\n]*'
URL_SIGN = ' URL '

digit_pattern = '\d+'
DIGIT_SIGN = ' DIGIT '


lowercase_reviews = [review.lower() for review in reviews]
no_whitespace = [review.strip() for review in lowercase_reviews]
no_urls = [re.sub(url_pattern, URL_SIGN, review) for review in no_whitespace]
no_digits = [re.sub(digit_pattern, DIGIT_SIGN, review) for review in no_urls]
tokenized = [word_tokenize(review) for review in no_digits[:50]]


# In[53]:


tokenized[:2]


reviews[350]

from sklearn.feature_extraction.text import CountVectorizer

count_vect = CountVectorizer(max_df=0.8, min_df=2, stop_words='english')

doc_term_matrix = count_vect.fit_transform(reviews)

doc_term_matrix

len(count_vect.vocabulary_)


dtm = pd.DataFrame(doc_term_matrix.toarray(), columns=count_vect.get_feature_names())
dtm.head()


dtm.sum().sort_values(ascending=False).head(10)

dtm.sum().sort_values(ascending=True).head(10)

dtm.sum().sort_values().head()

dtm.mean().sort_values(ascending=False).head()



#######################TFIDF
from sklearn.feature_extraction.text import TfidfVectorizer

tfidfvec = TfidfVectorizer()
sparse_tfidf = tfidfvec.fit_transform(reviews)
sparse_tfidf


# In[20]:


tfidf = pd.DataFrame(sparse_tfidf.toarray(), columns=tfidfvec.get_feature_names())
tfidf.head()


# Let's look at the 20 words with highest tf-idf weights.

# In[ ]:


tfidf.max().sort_values(ascending=False).head(20)


# ## Topic modeling <a id='topics'></a>
# 
# There are many topic modeling algorithms, but we'll use LDA. This is a standard model to use. Again, the goal is not to learn everything you need to know about topic modeling. Instead, this will provide you some starter code to run a simple model, with the idea that you can use this base of knowledge to explore this further.
# 
# We will run Latent Dirichlet Allocation, the most basic and the oldest version of topic modeling. We will run this in one big chunk of code. Our challenge: use our knowledge of scikit-learn that we gained aboe to walk through the code to understand what it is doing. Your challenge: figure out how to modify this code to work on your own data, and/or tweak the parameters to get better output.
# 


from sklearn.decomposition import LatentDirichletAllocation

LDA = LatentDirichletAllocation(n_components=5, random_state=42)

LDA.fit(doc_term_matrix)

import random

for i in range(10):
    random_id = random.randint(0,len(count_vect.get_feature_names()))
    print(count_vect.get_feature_names()[random_id])
    
    
first_topic = LDA.components_[0]

top_topic_words = first_topic.argsort()[-10:]

for i in top_topic_words:
    print(count_vect.get_feature_names()[i])
    
for i,topic in enumerate(LDA.components_):
    print(f'Top 10 words for topic #{i}:')
    print([count_vect.get_feature_names()[i] for i in topic.argsort()[-10:]])
    print('\n')