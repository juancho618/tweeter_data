#Redona Brahimetaj
#Juan Jose Soriano Escobar
#Distributed Computed and Storage Architecture
#DCSA project
#Last updated 24/12/2017

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener, json
from pymongo import MongoClient
from nltk.tokenize import TweetTokenizer
from clean.py import cleanTweet


consumerkey="cnV6zLTpFswKMIgpgvTfbae3g"
consumersecret=	"EwGSB3GQZAMBHp2x883BZfpO3pBWirbVBu2NzhFkVmUOOGEF6Y"
accesskey="804690952271044608-U1HO8J4UDTl5ygbfAhvWAoy4oPlmifM"
accesssecret="xgks2gpw4wZFK7mqr12FcqaamHdXtdnYUabffFVAbThai"

class listener(StreamListener):

    def on_data(self, data):
        #This is the meat of the script...it connects to your mongoDB and stores the tweet
        try:
            client = MongoClient('localhost',27017)
            # twitterdb is the new db that I created to store the tweets
            db = client.clean_tweets

            
            # Decode the JSON from Twitter
            datajson = json.loads(data)
            #Get just the tweet
            tweet = datajson['text']
            # apply the cleaning function to the tweet
            clean_tweet = cleanTweet(tweet)
            # Python Object that would be save in the db.
            pyObject = { 'text': clean_tweet, 'fullResponse': datajson }  

            #This is optional, I saw it as a suggestion from a website.
            #grab the 'created_at' data from the Tweet to use for display
            #print out a message to the screen that we have collected a tweet
            #print("Tweet collected at " + str(created_at))

            #It will insert into 'tweets' collection the data that are streamed
            db.tweets.insert(pyObject)
        except Exception as e:
           print(e)

    def on_error(self, status):
        print(status)

auth=OAuthHandler(consumerkey,consumersecret)
auth.set_access_token(accesskey,accesssecret)
twitterStream=Stream(auth,listener())
twitterStream.filter(locations=[-122.995004, 32.323198,-67.799695, 49.893813])

