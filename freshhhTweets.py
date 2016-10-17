import praw
import tweepy
import time

#TODO
#store the tweeted post id into temp_file 
#Make it run every hour or so and check that you aren't posting duplicates
# make cron job to make it run every hour
temp_file = 'tweeted.txt'

#reddit getting hot posts
reddit = praw.Reddit('fresh music from /r/hiphopheads')
hot_posts = reddit.get_subreddit('hiphopheads').get_hot(limit=30)
fresh_tag = 'FRESH'

#tokens and auth needed for twitter API
access_token = ''
access_token_secret = ''
consumer_key = ''
consumer_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
tweet = tweepy.API(auth)


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

def tweet_fresh_post(title, link, post_id):
	posted = check_duplicate_submission(post_id)
	if(not posted):
		print title + '\nReddit Thread: ' + link
		print "adding id: " + post_id + " to file"
		with open(temp_file,'a') as f:
			f.write(post_id + '\n')
		time.sleep(25)
		tweet.update_status(title + '\nReddit Thread: ' + link)
		#tweet Here
	else:
		print 'Already Tweeted'

def main():
	for submission in hot_posts:
		if submission.title[1:6].lower() == fresh_tag.lower():
			print "FRESH Music Found!"
			tweet_fresh_post(str(submission.title), str(submission.permalink), str(submission.id))

if __name__ == "__main__":
	main()

