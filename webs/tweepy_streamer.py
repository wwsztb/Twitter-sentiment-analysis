#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import sys


CONSUMER_KEY = "9z8OcETOR2XAlFFoiXJaRJdQk"
CONSUMER_SECRET = "Qg6VavLuqaXBTemWob7a9Wvo5w6IdTPlW0e1nEyepe4LvdTg4k"
ACCESS_TOKEN = "1232002559042359298-8tVta4ifiaIPV7Ho0V6XEV21YPsRr5"
ACCESS_TOKEN_SECRET = "b7K0SokRBLQHWnDjV5MhGUvOMRCe8LgEGszwTO1VrYeQg"



class TwitterStreamer():

    def __init__(self):
        pass
    
    
    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        listener = Linstener(fetched_tweets_filename)
        auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        stream = Stream(auth, listener)
        stream.filter(track= hash_tag_list)




class Linstener(StreamListener):

    
    def __init__(self, fetched_tweets_filename,):
        self.fetched_tweets_filename = fetched_tweets_filename

        self.num_tweets = 0
        
    
    def on_data(self,data):
        self.num_tweets += 1
        try:
            print(data)
            print("  ")
            print(self.num_tweets)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)

        except BaseException as e:
            print("Error on_data: s" % str(e))
            pass

        if self.num_tweets < 5000:
            return True
        else:
            return False  # Closes the stream.

    def on_error(self,status):
        print(status)
        
if __name__ == "__main__":

    hash_tag_list1 = ['today']
    fetched_tweets_filename1 = "today.csv"
    
    twitter_streamer1 = TwitterStreamer()
    twitter_streamer1.stream_tweets(fetched_tweets_filename1, hash_tag_list1)

