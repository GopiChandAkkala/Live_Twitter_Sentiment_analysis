import tweepy
from textblob import TextBlob
import credentials


auth = tweepy.OAuthHandler(credentials.consumer_key,credentials.consumer_secret)
auth.set_access_token(credentials.access_token,credentials.access_token_secret)
api = tweepy.API(auth)
searchTerm = input("Enter Keyword/Tag to search about: ")
NoOfTerms = int(input("Enter how many tweets to search: "))
#searching for tweets
tweets = tweepy.Cursor(api.search, q=searchTerm, lang = "en").items(NoOfTerms)


for tweet in tweets:
    analysis = TextBlob(tweet.text)
    polar = analysis.sentiment.polarity
    if polar > 0:
        label = "pos"
    elif polar < 0:
        label = "neg"
    else:
        label = "neu"
    output = open("twitter-out.txt","a")    
    output.write(label)
    output.write('\n')
    output.close()		


        
        
        


