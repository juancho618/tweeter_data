import re
import nltk
import numpy
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
tknz = TweetTokenizer()
clean_tweets = []
url_expression = 'http[s]?[:]?//(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

def cleanTweet(tweet):    
    wordnet_lemmatizer = WordNetLemmatizer()
    stop = set(stopwords.words('english')) #stop words!
    framents = tknz.tokenize(tweet)
    clean_fragments = []
    for f in framents:
        if f not in stop: # not included in the stop words
            f = f.lower() #lowercase fragment
            f = re.sub(r'[.,"!~_:|?\']+', '', f,flags=re.MULTILINE) # Special characters
            f =  re.sub(r'\.\.\.', '', f,flags=re.MULTILINE)) # 3 dots
            f = re.sub(url_expression, '', f,flags=re.MULTILINE) # links
            f = re.sub(r'@[a-z,A-Z,0-9 ]*', '', f, flags=re.MULTILINE) #clean at person references
            f = re.sub(r'RT @[a-z,A-Z]*: ', '', f, flags=re.MULTILINE) #Remove retweets
            f = wordnet_lemmatizer.lemmatize(f)
            if f:
                clean_fragments.append(f)
    return(" ".join(clean_fragments))

    
        



# links :
# https://stackoverflow.com/questions/26304191/get-the-document-name-in-scikit-learn-tf-idf-matrix
# https://www.youtube.com/watch?v=RPMYV-eb6lI