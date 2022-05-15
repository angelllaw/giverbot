import tweepy
import csv


#credentials
consumer_key = "CONSUMER_KEY"
consumer_secret_key = "CONSUMER_SECRET_KEY"
access_token = "ACCESS_TOKEN"
access_token_secret = "ACCESS_SCRET_TOKEN"

#authenticate to twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#test credentials
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

def main(giveawayType):
    alltweets = []
    search = giveawayType + " giveaway -filter:retweets"
    numberOfTweets = 5
    for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
        alltweets.append(tweet)
        try:
            tweet.favorite()
            #tweet.retweet()
            #api.create_friendship(tweet.user.id)
            print("Tweet retweeted and followed" + tweet.author.screen_name)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
        
    outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets] 
    return outtweets

def writeCSV(tweetArray):
    with open('tweets.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["id", "created_at", "text"])
        writer.writerows(tweetArray)

writeCSV(main("genshin"))