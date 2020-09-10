#---------- Twitter API ----------#

# pip install tweepy
import tweepy
import sys
import importlib
import json
# http://docs.tweepy.org/en/v3.8.0/api.html

# =============================================================================
# First I add directory, set my rate limit, and define my user
# =============================================================================

sys.path.insert(0, 'C:/Users/jenna/python/HW')

twitter = importlib.import_module('start_twitter_hw')
api = twitter.client

# See rate limit
limit = api.rate_limit_status()
limit.keys() ##look at dictionary's keys
# prepare for dictionaries all the way down

# Create user objects
washu_polisci = api.get_user('WUSTLPoliSci')
washu_polisci #object 

# Check type and methods
type(washu_polisci)
dir(washu_polisci)

# Trying some of these methods
print(washu_polisci.id)
print(washu_polisci.name)
print(washu_polisci.screen_name)
print(washu_polisci.location)

# =============================================================================
# ONE DEGREE OF SEPARATION
# PART ONE: Among the followers of @WUSTLPoliSci who is the most active?
# =============================================================================

# First, generate info and save data for followers
total_followers = washu_polisci.followers_ids() 
print(total_followers[0:50]) #to test
#compare with followers_count
washu_polisci.followers_count == len(total_followers) 

#Create empty lists to fill with tweet and follower counts:
tweets = []
followers = []

# Now I fill these lists, using only 10 users to test:
for follower_id in total_followers[0:len(total_followers)]:
    try:
        user = api.get_user(follower_id)
        tweets.append(user.statuses_count)
        followers.append(user.followers_count)  
    except:
        pass
        
#dir(tweets)
# Identify the max tweets
sorted(tweets)[-1]
# Now identify and print the user with these tweets
max_tweet_user = api.get_user(total_followers[tweets.index(max(tweets))])
print(max_tweet_user.name)

# =============================================================================
# PART TWO: Among the followers of @WUSTLPoliSci who is the most popular?
# =============================================================================

# Identify max followers
sorted(followers)[-1]
# Identify and print user with max followers
popular_user = api.get_user(total_followers[followers.index(max(followers))])
print(popular_user.name)


# =============================================================================
# PART THREE: Among the friends of @WUSTLPoliSci, i.e. the users she is following,
# who are the most active layman, expert and celebrity?
# =============================================================================

# Then generate info and save data for friends
washu_polisci.friends_count

# This will only generate 20. We need 158.
friends = washu_polisci.friends()
type(friends)
len(friends)
# Let's try again
#friends = washu_polisci.friends_ids()
# my user object does not have attribute friends_ids. Guess I need to go 'up' to my API?
#dir(api)
#dir(washu_polisci)
washu_friends = api.friends_ids(washu_polisci.id)
len(washu_friends) == washu_polisci.friends_count
washu_friends[0:5] # to see what this looks like
#dir(washu_friends)
##############################################################################
# Now we move onto filling lists for each friend type
lay_friends = []
expert_friends = []
celeb_friends = []

lay_friends_tweets = []
expert_friends_tweets = []
celeb_friends_tweets = []

pop_friends_followers = []

# Now I fill these lists, using only 10 users to test:
for friend_id in washu_friends[0:len(washu_friends)]:
    user = api.get_user(friend_id)
    pop_friends_followers.append(user.followers_count)
    try:
        if user.followers_count < 100:
            lay_friends.append(friend_id)
            lay_friends_tweets.append(user.statuses_count)
        elif user.followers_count > 1000:
           celeb_friends.append(friend_id)
           celeb_friends_tweets.append(user.statuses_count)
        else:
            expert_friends.append(friend_id)
            expert_friends_tweets.append(user.statuses_count)
    except tweepy.TweepError:
        pass

# Identify the max tweets for laypeople
sorted(lay_friends_tweets)[-1]
# Now identify and print the user with these tweets
max_lay_tweeter = api.get_user(lay_friends[lay_friends_tweets.index(max(lay_friends_tweets))])
print(max_lay_tweeter.name)

# Identify the max tweets for experts
sorted(expert_friends_tweets)[-1]
# Now identify and print the user with these tweets
max_expert_tweeter = api.get_user(expert_friends[expert_friends_tweets.index(max(expert_friends_tweets))])
print(max_expert_tweeter.name)

# Identify the max tweets for celebs
sorted(celeb_friends_tweets)[-1]
# Now identify and print the user with these tweets
max_celeb_tweeter = api.get_user(celeb_friends[celeb_friends_tweets.index(max(celeb_friends_tweets))])
print(max_celeb_tweeter.name)

# =============================================================================
# PART FOUR: Among the friends of @WUSTLPoliSci, i.e. the users she is following,
# who is the most popular?
# =============================================================================

# Identify max followers
pop_friends_followers 
sorted(pop_friends_followers)[-1]		
# Identify and print friend with max followers
popular_friend = api.get_user(washu_friends[pop_friends_followers.index(max(pop_friends_followers))])
print(popular_friend.name)

# =============================================================================
# TWO DEGREES OF SEPARATION
# PART ONE: Among the followers of @WUSTLPoliSci and their followers, who is the
#       most active?
# =============================================================================

# First, I restrict the followers/fof to users with < 1000 followers
unpopular_followers = []

# I will first test a loop that only takes followers without celeb status.
# I am subsetting this to test the code. My computer restarted (???) while the
# OG code was running
for follower_id in total_followers[0:50]:
    user = api.get_user(follower_id)
    if user.followers_count < 1000:
        unpopular_followers.append(follower_id)
    else:
        continue

# Did it work?
len(unpopular_followers)
 
# Next, I want to pull the followers of these unpopular followers with less than
# 1000 followers     

unpopular_fof = []  
for follower_id in unpopular_followers:
    user = api.get_user(follower_id)
    try:
        if user.followers_count < 1000:
           unpopular_fof.append(follower_id)
        else:
            continue
    except tweepy.TweepError:
        pass
len(unpopular_fof) 
# Then I join the unpopular friends and fof    
unpop_ffof = unpopular_fof + unpopular_followers

# Finally, I generate a list of tweets for this population
ffof_tweets = []
for follower_id in unpop_ffof:
    user = api.get_user(follower_id)
    try:
        ffof_tweets.append(user.statuses_count)
    except:
        pass

# Once this is collected, I'll find the most active follower  
active_unpop_follower = api.get_user(unpop_ffof[ffof_tweets.index(max(ffof_tweets))])
print(active_unpop_follower.name)
    
# =============================================================================
# PART TWO: Among the friends of @WUSTLPoliSci and their followers, who is the
#       most active?
# =============================================================================

# First, I restrict the friends/fof to users with < 1000 followers

unpopular_friends = lay_friends + expert_friends

for friend_id in unpopular_friends[0:50]:
    try:
        user = api.get_user(follower_id)
        unpopular_friends.append(follower_id)
    except tweepy.TweepError:
        pass
    
# Then I add the tweets of fof to the tweets I've already gathered for friends    
unpopular_tweets = lay_friends_tweets + expert_friends_tweets
unpopular_tweets.append(user.statuses_count)

# Finally, I generate the name of the friend/fof with the greatest number of tweets
active_unpop_friend = api.get_user(unpopular_friends[unpopular_tweets.index(max(unpopular_tweets))])
print(active_unpop_friend.name)

##############################################################################

# Questions for Ben:
  # why am I subsetting "celeb friends" and not "washu friends" in part 3?  
  # Why does my for loop not work with range(len(washu_friends))? Is this not grabbing the same
  # data as washu_friends[0:len(washu_friends)]?
