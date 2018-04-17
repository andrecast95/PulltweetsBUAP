from TwitterSearch import *
import os
from nltk.tokenize import TweetTokenizer

tokenizer = TweetTokenizer()

try:
    # create a TwitterUserOrder for user named 'NeinQuarterly'
	tuo = TwitterUserOrder('CAPUFE') # is equal to TwitterUserOrder(458966079)
	tuo.set_exclude_replies(True)
    #tuo.set_keywords(['Incidente','incidente', 'ha sido atendido','ha sido atendido,'])

    # it's about time to create TwitterSearch object again
	ts = TwitterSearch(
        consumer_key = os.environ['TWITTER_CONSUMER_KEY'],
        consumer_secret = os.environ['TWITTER_CONSUMER_SECRET'],
        access_token = os.environ['TWITTER_ACCESS_TOKEN'],
        access_token_secret = os.environ['TWITTER_ACCESS_SECRET']
    )

    # start asking Twitter about the timeline
	for tweet in ts.search_tweets_iterable(tuo):
		key_words = tokenizer.tokenize(tweet['text'])
		for words in key_words:
			for search_words in ['Incidente','incidente','ha sido atendido','ha sido atendido,']:
				if search_words in words:
					print('@%s tweeted: %s' % (tweet['user']['screen_name'], tweet['text']))	

except TwitterSearchException as e: # catch all those ugly errors
    print(e)
