# these should be the only imports you need
import tweepy
import nltk
import json
import sys

# write your code here
# usage should be python3 part1.py <username> <num_tweets>
from app_data import access_token, access_token_secret, consumer_key, consumer_secret
from nltk.corpus import *
from nltk import FreqDist
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
# input
input_name=sys.argv[1]
user = api.get_user(input_name)
tweet_number=int(sys.argv[2])
# ask data
user_timeline = api.user_timeline(user.screen_name, count = tweet_number)
text = []
nonretweeted_count = 0
tweet_favorited = 0
tweet_retweeted = 0
special_words = ['http', 'https', 'RT']
diction = {}
# create word diction
for tweet in user_timeline:
	tokens = nltk.word_tokenize(tweet.text)
	# print(tokens)
	for eachword in tokens:
		if (eachword[0].isalpha()) and (eachword not in special_words):
			if eachword not in diction:
				diction[eachword] = 1
			else:
				diction[eachword] += 1
	try:
		test = tweet.retweeted_status
	except:
		nonretweeted_count += 1
		tweet_favorited += tweet.favorite_count
		tweet_retweeted +=tweet.retweet_count
# print(diction)
# print(nonretweeted_count, tweet_retweeted, tweet_favorited)
# sort words
keys_sort = sorted(list(diction.keys()), key = lambda k: diction[k], reverse = True)
# for key in keys_sort:
# 	print(key, diction[key])
words_tag = nltk.pos_tag(keys_sort)
# print(words_tag)
vb = []
nn = []
jj = []
for eachtag in words_tag:
	if "VB" in eachtag[1]:
		vb.append(eachtag[0])
# print(vb[:5])
for eachtag in words_tag:
	if "NN" in eachtag[1]:
		nn.append(eachtag[0])
# print(nn[:5])
for eachtag in words_tag:
	if "JJ" in eachtag[1]:
		jj.append(eachtag[0])
# print(jj[:5])

# output results
print("USER: " + user.screen_name)
print("TWEETS ANALYZED: " + str(tweet_number))
string_n = ""
string_v = ""
string_a = ""
for n in range (5):
	string_v += vb[n] + '(' + str(diction[vb[n]]) + ')' + " "
	string_n += nn[n] + '(' + str(diction[nn[n]]) + ')' + " "
	string_a += jj[n] + '(' + str(diction[jj[n]]) + ')' + " "
print("VERBS: " + string_v)
print("NOUNS: " + string_n)
print("ADJECTIVES: " + string_a)
print("ORIGINAL TWEETS: " + str(nonretweeted_count))
print("TIMES FAVORITED (ORIGINAL TWEETS ONLY): " + str(tweet_favorited))
print("TIMES RETWEETED (ORIGINAL TWEETS ONLY): " + str(tweet_retweeted))

# output csv
fileout = open("noun_data.csv", "w")
fileout.write("Noun, Number\n")
for noun in range(5):
	fileout.write("{}, {}\n".format(nn[noun],diction[nn[noun]]))
fileout.close()      

