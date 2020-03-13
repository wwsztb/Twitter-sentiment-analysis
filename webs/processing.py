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

data = pd.read_csv('today.csv',header=None, usecols=[3])
happylex = pd.read_csv('lex//happyLex.csv',header=None,usecols=[1])
happylex = np.array(happylex)#np.ndarray()
happylex.flatten()

excitlex = pd.read_csv('lex//exticeLex.csv',header=None,usecols=[1])
excitlex = np.array(excitlex)#np.ndarray()
excitlex.flatten()

pleasantlex = pd.read_csv('lex//PleasantLex.csv',header=None,usecols=[1])
pleasantlex = np.array(pleasantlex)#np.ndarray()
pleasantlex.flatten()

fearlex = pd.read_csv('lex//fearLex.csv',header=None,usecols=[1])
fearlex = np.array(fearlex)#np.ndarray()
fearlex.flatten()

surpriselex = pd.read_csv('lex//surpriseLex.csv',header=None,usecols=[1])
surpriselex = np.array(surpriselex)#np.ndarray()
surpriselex.flatten()

angrylex = pd.read_csv('lex//angryLex.csv',header=None,usecols=[1])
angrylex = np.array(angrylex)#np.ndarray()
angrylex.flatten()


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
        if type(tweet) == list:

            for i in range(len(tweet)):

                if tweet[i] in excitlex:
                    self.ecscore += 1
        if type(tweet) == list:

            for i in range(len(tweet)):

                if tweet[i] in happylex:
                    self.hascore += 1
        if type(tweet) == list:

            for i in range(len(tweet)):

                if tweet[i] in pleasantlex:
                    self.plscore += 1
        if type(tweet) == list:

            for i in range(len(tweet)):

                if tweet[i] in surpriselex:
                    self.surscore += 1
        if type(tweet) == list:

            for i in range(len(tweet)):

                if tweet[i] in fearlex:
                    self.fearscore += 1
        if type(tweet) == list:

            for i in range(len(tweet)):

                if tweet[i] in angrylex:
                    self.anscore += 1


    def Nddetection(self,tweet):
        #Cheak hashtag
        try:
            if re.search(' #exciting', tweet) is not None:
                self.ecscore += 2
            if re.search(' #happy', tweet) is not None:
                self.hascore += 2
            if re.search(' #enjoy', tweet) is not None:
                self.plscore += 2
            if re.search(' #surprise', tweet) is not None:
                self.surscore += 2
            if re.search(' #fear', tweet) is not None:
                self.fearscore += 2
            if re.search(' #angry', tweet) is not None:
                self.anscore += 2
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





Tweetclassifier = classifier()

processedsample.applymap(Tweetclassifier.judge)




print(len(excitementlist))
Ecitement=pd.DataFrame(columns=None,data=excitementlist)
Ecitement = Ecitement.applymap(tweetProcessor.processTweet)
Ecitement.to_csv('C:\\Users\\fz\\Documents\\webs\\preprosessing\\Ecitement.csv',header=None,encoding='gbk')

print(len(happylist))
happy=pd.DataFrame(columns=None,data=happylist)
happy = happy.applymap(tweetProcessor.processTweet)
happy.to_csv('C:\\Users\\fz\\Documents\\webs\\preprosessing\\happy.csv',header=None,encoding='gbk')

print(len(pleasantlist))
pleasant=pd.DataFrame(columns=None,data=pleasantlist)
pleasant = pleasant.applymap(tweetProcessor.processTweet)
pleasant.to_csv('C:\\Users\\fz\\Documents\\webs\\preprosessing\\pleasant.csv',header=None,encoding='gbk')

print(len(surpriselist))
surprise=pd.DataFrame(columns=None,data=surpriselist)
surprise = surprise.applymap(tweetProcessor.processTweet)
surprise.to_csv('C:\\Users\\fz\\Documents\\webs\\preprosessing\\surprise.csv',header=None,encoding='gbk')

print(len(fearlist))
fear=pd.DataFrame(columns=None,data=fearlist)
fear = fear.applymap(tweetProcessor.processTweet)
fear.to_csv('C:\\Users\\fz\\Documents\\webs\\preprosessing\\fear.csv',header=None,encoding='gbk')

print(len(angrylist))
angry=pd.DataFrame(columns=None,data=angrylist)
angry = angry.applymap(tweetProcessor.processTweet)
angry.to_csv('C:\\Users\\fz\\Documents\\webs\\preprosessing\\angry.csv',header=None,encoding='gbk')