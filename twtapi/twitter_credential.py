import json

#this is the log in information of the twitter api
credentials = {}
credentials['CONSUMER_KEY'] = 'x4FguSwehXpgdPtq2bTi5dOJU'
credentials['CONSUMER_SECRET'] = 'yAHfjLyxuct4I6He9uDbqr547MN0RP6ghdSFgYn19XDF4uXbge'
credentials['ACCESS_TOKEN'] = '2219948304-c60sVwWulIqRJLnPSFH6rMWn9uMIvYxmQSTQx56'
credentials['ACCESS_SECRET'] = 'dH11u0vsbWIiMBzgEbHTgpFSzlrmu0vhyGfqbXiRsBsUf'

with open("twitter_credentials.json","w") as file:
    json.dump(credentials,file)
