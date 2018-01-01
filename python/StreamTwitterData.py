#Redona Brahimetaj
#Juan Jose Soriano Escobar
#Distributed Computed and Storage Architecture
#DCSA project
#Last updated 24/12/2017

#import all the neccessary python packages that will be used
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener, json
from pymongo import MongoClient
from nltk.tokenize import TweetTokenizer
from clean import cleanTweet

#CONFIDENTIAL credentials that make possible to access Twitter API
consumerkey='cnV6zLTpFswKMIgpgvTfbae3g'
consumersecret=	"EwGSB3GQZAMBHp2x883BZfpO3pBWirbVBu2NzhFkVmUOOGEF6Y"
accesskey="804690952271044608-U1HO8J4UDTl5ygbfAhvWAoy4oPlmifM"
accesssecret="xgks2gpw4wZFK7mqr12FcqaamHdXtdnYUabffFVAbThai"

class listener(StreamListener):

    def on_data(self, data):
        #This is the main part of the script since it makes possible to connect to mongoDB and stores the tweet
        try:
            client = MongoClient('localhost',27017)
            # clean_tweets is the new db that we created to store the tweets
            db = client.clean_tweets
            # Decode the JSON from Twitter
            datajson = json.loads(data)
            #Get just the tweet
            tweet = datajson['text']
            # apply the cleaning function to the tweet
            clean_tweet = cleanTweet(tweet)
            # Python Object that would be save in the db.
            pyObject = { 'text': clean_tweet, 'fullResponse': datajson }

            #It will insert into 'tweets' collection the data that are streamed
            db.tweets.insert(pyObject)
        except Exception as e:
           print(e)

    #in case something went wrong, the status of the error will be printed
    def on_error(self, status):
        print(status)

#Set up the connection by using the credentials declared above and filter the tweets by specifying the coordinates of the location that was given.
auth=OAuthHandler(consumerkey,consumersecret)
auth.set_access_token(accesskey,accesssecret)
twitterStream=Stream(auth,listener())
twitterStream.filter(locations=[-122.995004, 32.323198,-67.799695, 49.893813])

