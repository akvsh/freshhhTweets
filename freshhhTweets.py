#!/usr/bin/python
import praw
import tweepy
import time
import sys

#TODO
# Add /r/indieheads and /r/popheads

temp_file = 'tweeted.txt'

#getting the top 25 posts from 'hot'
reddit = praw.Reddit('fresh music from /r/hiphopheads')
hot_posts = reddit.get_subreddit('hiphopheads').get_hot(limit=25)
#The tag that we are looking for
fresh_tag = 'FRESH'

#tokens and auth needed for twitter API
access_token = ''
access_token_secret = ''
consumer_key = ''
consumer_secret = ''
#authenticating
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
tweet = tweepy.API(auth)


#look through text file and see if post id exists
#returns true if post is already tweeted (the id is in the file)
def check_duplicate_submission(curr_id):
	id_exists = False
	with open(temp_file,'r') as f:
		for posted_id in f:
			print posted_id
			if posted_id.strip() == curr_id:
				id_exists = True
				break;
	print "Does id exist? {0}".format(id_exists)
	return id_exists

#first check for a duplicate tweet and then tweet if new and score >= 100
def tweet_fresh_post(title, link, post_id, score):
	posted = check_duplicate_submission(post_id)
	if(not posted and score >= 100):
		print '{0} \nReddit Thread: {1}'.format(title,link)
		print "adding id: {0} to file".format(post_id)
		with open(temp_file,'a') as f:
			f.write(post_id + '\n')
		time.sleep(25)
		tweet.update_status(title + '\nReddit Thread: ' + link)
		#tweet Here
	else:
		print ('Already tweeted' if score >= 100 else 'Score not high enough')

def main():
	for submission in hot_posts:
		print submission.score
		if submission.title[1:6].lower() == fresh_tag.lower():
			print "FRESH Music Found!"
			tweet_fresh_post(submission.title, submission.permalink, submission.id, submission.score)

if __name__ == "__main__":
	main()

