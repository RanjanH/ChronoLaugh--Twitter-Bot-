import tweepy 
from time import sleep 
from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth) 

QUERY = '# funny' # Will consist the hashtags that the bot will search for example: '# memes'
LIKE = True
FOLLOW = True
SLEEP_TIME = 300

print("Twitter bot which retweets, like tweets and follow users") 
print("Bot Settings") 
print("Like Tweets :", LIKE) 
print("Follow users :", FOLLOW) 

for tweet in tweepy.Cursor(api.search, q = QUERY).items(): 
	try: 
		print('\nTweet by: @' + tweet.user.screen_name) 

		tweet.retweet() 
		print('Retweeted the tweet') 

		# Favorite the tweet 
		if LIKE: 
			tweet.favorite() 
			print('Favorited the tweet') 

		# Follow the user who tweeted 
		# check if bot is already following the user 
		if FOLLOW: 
			if not tweet.user.following: 
				tweet.user.follow() 
				print('Followed the user') 

		sleep(SLEEP_TIME) 

	except tweepy.TweepError as e: 
		print(e.reason) 

	except StopIteration: 
		break
