lang_code="en"
keyword1="dog food"
keyword2="cat food"
keyword3="anything"
keyword4="python"
keyword5="react"

keywords= [keyword1, keyword2, keyword3, keyword4, keyword5]
keywordList = list(filter(None, keywords))

import pandas as pd
import requests
import json
import time
import string
import nltk
from stop_words import get_stop_words
from collections import Counter
from json import loads

letterlist=[""]
letterlist=letterlist+list(string.ascii_lowercase)

keywordsuggestions=[]
for keyword in keywordList:
  for letter in letterlist:
    URL="http://suggestqueries.google.com/complete/search?client=firefox&hl="+str(lang_code)+"&q="+keyword+" "+letter
    headers={'User-agent':'Mozilla/5.0'}
    response = requests.get(URL, headers=headers)
    result = json.loads(response.content.decode('utf-8'))
    keywordsuggest = [keyword, letter]
    for word in result[1]:
      if(word!=keyword):
        keywordsuggest.append(word)
      time.sleep(1)
      keywordsuggestions.append(keywordsuggest)

keywordsuggestions_dataframe = pd.DataFrame(keywordsuggestions)

columnnames = ["Keyword", "Letter"]
for i in range(1, len(keywordsuggestions_dataframe)-1):
  columnnames.append("Suggestion"+str(i))
  keywordsuggestions_dataframe.columns=columnnames

allkeywords = keywordList
for i in range(1,len(keywordsuggestions_dataframe)-1):
  suggestList = keywordsuggestions_dataframe["Suggestion"+str(i)].values.tolist()
  for suggestion in suggestList:
    allkeywords.append(suggestion)


stop_words = get_stop_words(lang_code)
wordlist=[]
seed_words=[]
for keyword in keywords:
  for seed_word in nltk.word_tokenize(str(keyword).lower()):
    if(len(seed_word)>0):
      seed_words.append(seed_word)
for keyword in allkeywords:
  words = nltk.word_tokenize(str(keyword).lower())
  for word in words:
    if(word not in stop_words and word not in seed_words and len(word)>1):
      wordlist.append(word)

most_common_words = [word for word, word_count in Counter(wordlist).most_common(200)]

clusters = []
for common_word in most_common_words:
  for keyword in allkeywords:
    if(common_word in str(keyword)):
      clusters.append([keyword, common_word])
cluster_dataframe = pd.DataFrame(clusters, columns=['Keywords', 'Cluster'])

cluster_dataframe.to_csv("keywords_clustered.csv")
cluster_dataframe