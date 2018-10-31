import json
from twython import TwythonStreamer
from twython import Twython
import csv

#Load the twitter_credentials
with open("twitter_credentials.json","r") as file:
    creds = json.load(file)

#Instantiate an object
python_tweets = Twython(creds['CONSUMER_KEY'],creds['CONSUMER_SECRET'])


#create a q
query = {'q':' ',
        'result_type':'recent',
        #'geocode':'-86.887 40.428 10mi',
        'lang':'en',
        }

#Filter the unwanted data
def tw_info(tweet):
    d = {}
    d['text'] = tweet['text']
    d['user'] = tweet['user']['screen']
    d['user_loc'] = tweet['user']['location']
    return d


class twStreamer(TwythonStreamer):
    def on_sucess(self,data):
        print(data)
        if data['lang'] == 'en':
            tweet_inf = tw_info(data)
            self.save_to_csv(tweet_inf)

    def on_error(self, status_code, data):
        print("111111")
        print(status_code,data)
        self.disconnect()

    def save_to_csv(self, tweet):
        print(list(tweet.values()))
        with open(r'saved_tweets.csv','a') as file:
            writer = csv.writer(file)
            writer.writerow(list(tweet.values()))
#stream = twStreamer(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'], creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])
stream = twStreamer('x4FguSwehXpgdPtq2bTi5dOJU', 'yAHfjLyxuct4I6He9uDbqr547MN0RP6ghdSFgYn19XDF4uXbge',
'2219948304-c60sVwWulIqRJLnPSFH6rMWn9uMIvYxmQSTQx56', 'dH11u0vsbWIiMBzgEbHTgpFSzlrmu0vhyGfqbXiRsBsUf')

#Find out what are things that are neccessary for streaming

try:
    print("start")
    stream.statuses.filter(locations = "-86.96,40.41,-86.87,40.49")
    print("end")
except:
    print("Oops!",sys.exc_info()[0],"occured.")
    print("Next entry.")
    print()
