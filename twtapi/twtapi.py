import json
from twython import Twython
import csv

#Load the twitter_credentials
with open("twitter_credentials.json","r") as file:
    creds = json.load(file)

#Instantiate an object
python_tweets = Twython(creds['CONSUMER_KEY'],creds['CONSUMER_SECRET'])


#create a q
query = {'q':'',
        'result_type':'recent',
        'geocode':'-86.887 40.428 10mi',
        'lang':'en',
        }

#Filter the unwanted data
def tw_info(tweet):
    d = {}
    d['text'] = tweet['text']
    d['user'] = tweet['user']['screen']
    d['user_loc'] = tweet['user']['location']
    return d


class twStreamer(Twython):
    def on_sucess(self,data):
        if data['lang'] == 'en':
            tweet_inf = tw_info(data)
            self.save_to_csv(tweet_inf)

    def on_error(self, status_code, data):
        print(status_code,data)
        self.disconnect()

    def save_to_csv(self, tweet):
        with open(r'saved_tweets.csv','a') as file:
            writer = csv.writer(file)
            writer.writerow(list(tweet.values()))

stream = twStreamer(creds)

#Find out what are things that are neccessary for streaming
stream.statuses.filter(query)
