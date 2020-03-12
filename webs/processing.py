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
excitementlist = []
happylist = []
pleasantlist = []
surpriselist = []
fearlist = []
angrylist = []

data = pd.read_csv('result.csv',header=None, usecols=[3])



class classifier:
    #Emotion classifier
    def __init__(self):
        self.ecscore = 0
        self.hascore = 0
        self.plscore = 0
        self.surscore = 0
        self.fearscore = 0
        self.anscore = 0


    def Stdetection(self,tweet):
        #Check seedword
        try:
            if re.search('excitement', tweet) is not None:
                self.ecscore += 1
            if re.search('happy', tweet) is not None:
                self.hascore += 1
            if re.search('enjoy', tweet) is not None:
                self.plscore += 1
            if re.search('surprise', tweet) is not None:
                self.surscore += 1
            if re.search('fear', tweet) is not None:
                self.fearscore += 1
            if re.search('angry', tweet) is not None:
                self.anscore += 1

        except:
            pass
    def Nddetection(self,tweet):
        #Cheak hashtag
        try:
            if re.search(' #exciting', tweet) is not None:
                self.ecscore += 1
            if re.search(' #happy', tweet) is not None:
                self.hascore += 1
            if re.search(' #enjoy', tweet) is not None:
                self.plscore += 1
            if re.search(' #surprise', tweet) is not None:
                self.surscore += 1
            if re.search(' #fear', tweet) is not None:
                self.fearscore += 1
            if re.search(' #angry', tweet) is not None:
                self.anscore += 1
        except:
            pass
    def Findetection(self,tweet):
        #Check emoticons
        try:
            if re.search('🤩', tweet) is not None:
                self.ecscore += 1
            if re.search('😀', tweet) is not None:
                self.hascore += 1
            if re.search('😌', tweet) is not None:
                self.plscore += 1
            if re.search('😯', tweet) is not None:
                self.surscore += 1
            if re.search('😨', tweet) is not None:
                self.fearscore += 1
            if re.search('😠', tweet) is not None:
                self.anscore += 1
        except:
            pass
    '''def getword(self,seed,hash,emo,list):
        self.seed = seed
        self.hashtag = hash
        self.emo = emo
        self.list = list'''
    def reset(self):
        self.ecscore = 0
        self.hascore = 0
        self.plscore = 0
        self.surscore = 0
        self.fearscore = 0
        self.anscore = 0


    def judge(self,tweet):
        #Perform classification
        self.Stdetection(tweet)
        self.Nddetection(tweet)
        self.Findetection(tweet)
        if max(self.ecscore, self.hascore,self.plscore,self.surscore,self.fearscore,self.anscore) == self.ecscore and self.ecscore > 0:
            excitementlist.append(tweet)
            self.reset()
        elif max(self.ecscore, self.hascore,self.plscore,self.surscore,self.fearscore,self.anscore) == self.hascore and self.hascore > 0:
            happylist.append(tweet)
            self.reset()
        elif max(self.ecscore, self.hascore,self.plscore,self.surscore,self.fearscore,self.anscore) == self.plscore and self.plscore > 0:
            pleasantlist.append(tweet)
            self.reset()
        elif max(self.ecscore, self.hascore,self.plscore,self.surscore,self.fearscore,self.anscore) == self.surscore and self.surscore > 0:
            surpriselist.append(tweet)
            self.reset()
        elif max(self.ecscore, self.hascore,self.plscore,self.surscore,self.fearscore,self.anscore) == self.fearscore and self.fearscore > 0:
            fearlist.append(tweet)
            self.reset()
        elif max(self.ecscore, self.hascore,self.plscore,self.surscore,self.fearscore,self.anscore) == self.anscore and self.anscore > 0:
            angrylist.append(tweet)
            self.reset()
        else:
            pass


class PreProcessTweets:
    #text preprocessing
    def __init__(self):
        self._stopwords = set(stopwords.words('english') + list(punctuation) + ['AT_USER', 'URL'])



    def processTweet(self, tweet):

        try:
            tweet = tweet.lower()  # convert text to lower-case
            tweet = re.sub(r'[^\w\s]', '', tweet) #remove punctuation
            tweet = tweet.replace('text','',1) #remove 'text' on head
            tweet = re.sub(r'\d +', '', tweet)  #remove number
            tweet = re.sub('@[^\s]+', 'AT_USER', tweet)  # remove usernames
            #tweet = re.sub(r'#([^\s]+)', r'\1', tweet)  # remove the # in #hashtag
            tweet = word_tokenize(tweet)  # remove repeated characters (helloooooooo into hello)

            return [word for word in tweet if word not in self._stopwords]
        except:
            return 0






Tweetclassifier = classifier()

data.applymap(Tweetclassifier.judge)

tweetProcessor = PreProcessTweets()



print(len(excitementlist))
Ecitement=pd.DataFrame(columns=None,data=excitementlist)
Ecitement = Ecitement.applymap(tweetProcessor.processTweet)
Ecitement.to_csv('C:\\Users\\fz\\Documents\\webs\\preprosessing\\Ecitement.csv',encoding='gbk')

print(len(happylist))
happy=pd.DataFrame(columns=None,data=happylist)
happy = happy.applymap(tweetProcessor.processTweet)
happy.to_csv('C:\\Users\\fz\\Documents\\webs\\preprosessing\\happy.csv',encoding='gbk')

print(len(pleasantlist))
pleasant=pd.DataFrame(columns=None,data=pleasantlist)
pleasant = pleasant.applymap(tweetProcessor.processTweet)
pleasant.to_csv('C:\\Users\\fz\\Documents\\webs\\preprosessing\\pleasant.csv',encoding='gbk')

print(len(surpriselist))
surprise=pd.DataFrame(columns=None,data=surpriselist)
surprise = surprise.applymap(tweetProcessor.processTweet)
surprise.to_csv('C:\\Users\\fz\\Documents\\webs\\preprosessing\\surprise.csv',encoding='gbk')

print(len(fearlist))
fear=pd.DataFrame(columns=None,data=fearlist)
fear = fear.applymap(tweetProcessor.processTweet)
fear.to_csv('C:\\Users\\fz\\Documents\\webs\\preprosessing\\fear.csv',encoding='gbk')

print(len(angrylist))
angry=pd.DataFrame(columns=None,data=angrylist)
angry = angry.applymap(tweetProcessor.processTweet)
angry.to_csv('C:\\Users\\fz\\Documents\\webs\\preprosessing\\angry.csv',encoding='gbk')