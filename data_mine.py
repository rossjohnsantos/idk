import tweepy

consumer_key = "w1Nu7IlXH3LQVMAmP2g9lgXnL"
consumer_secret = "1IOUg99lrWLLwdubWwyX2ek3kacbvQRVIaLhli4BRADJ0S495h"
access_token = "1436461563934879744-jhC27GzQ797XC0jPJL4ZM4Mm2tsWPw"
access_token_secret = "RWC0zjqGZG9PObPssxDkkh0HzvqdE38uSBEeYk0aqXYgO"

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth) 

# Using the API object to get tweets from your timeline, and storing it in a variable called public_tweets
public_tweets = api.home_timeline()
# foreach through all tweets pulled
for tweet in public_tweets:
   # printing the text stored inside the tweet object
   print (tweet.text)
