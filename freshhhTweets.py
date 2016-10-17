import praw
import tweepy

#TODO
#Make it run every hour or so and check that you aren't posting duplicates
temp_file = 'tweeted.txt'


#tokens and stuff needed for twitter API
access_token = ''
access_token_secret = ''
consumer_key = ''
consumer_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def tweet_fresh_post(title,link,post_id):
	is_already_posted = check_duplicate_submission(post_id)
	if(is_already_posted):
		break
	else:
		#tweet Here
	#tweet with title and post link to post

#def get_hot_posts():
reddit = praw.Reddit('fresh music from /r/hiphopheads')
hot_posts = reddit.get_subreddit('hiphopheads').get_hot(limit=30)
fresh_tag = '[FRESH]'

for submission in hot_posts:
	if submission.title[0:7].lower() == fresh_tag.lower():
		tweet_fresh_post(submission.title, submission.permalink, submission.id) 
		print "FRESH Music Found!"
		print submission.id
		print submission.title
		print submission.permalink
		#TODO check if post begins with [FRESH] (case doesn't matter) and call tweet function if it works

