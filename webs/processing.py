import re
import pandas as pd
import nltk
import numpy as np
import string
from nltk.tokenize import word_tokenize
from string import punctuation
from nltk.corpus import stopwords
import pandas as pd
nltk.download("stopwords")



data = pd.read_csv('today.csv',header=None,index_col= None, usecols=[3])
data.drop_duplicates(inplace=True)
data2 = pd.read_csv('today.csv',header=None,index_col= None, usecols=[0,1])
data2.drop_duplicates(inplace=True)

class PreProcessTweets:
    #text preprocessing
    def __init__(self):
        self._stopwords = set(stopwords.words('english') + list(punctuation) )



    def processTweet(self, tweet):

        try:
            tweet = tweet.lower()  # convert text to lower-case
            tweet = re.sub(r'[a-z]*[:.]+\S+', '', tweet)  # remove URLs
            tweet = re.sub('@[^\s]+', '', tweet)  # remove usernames
            #tweet = re.sub(r'[^\w\s]', '', tweet) #remove punctuation
            tweet = tweet.replace('rt', '', 1) #remove rt
            tweet = tweet.replace('text','',1) #remove 'text' on head
            tweet = re.sub(r'\d +', '', tweet)  #remove number
            tweet = word_tokenize(tweet)  # remove repeated characters (helloooooooo into hello)

            return [word for word in tweet if word not in self._stopwords]
        except:
            return None

tweetProcessor = PreProcessTweets()
processedsample = data.applymap(tweetProcessor.processTweet)
result = pd.concat([data2, processedsample], axis=1)

result.to_csv('result.csv',header= 0,index= 0,encoding='gbk')


