import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import io
import json 
# twitter OAuth
ckey = '6uCSWswyHYDjUmnXqZY0EOPTT'
consumer_secret = 'KqEqpU0uXoEE8qXHw9sow8wZSUuHGuhEXBPgHWjwXbtsSQ55ha'
access_token_key = '723228015891599362-Hqg6THTKZhtOssrxMVSl3uMc69drnTo'
access_token_secret = 'M6nCHBAqYqym8RhaqUiLV0nVOoDwBjtOfxaelilrKrTmS'

class listener(StreamListener):

	def __init__(self, start_time):
         self.counter=0        
         self.time = start_time
#         self.limit = time_limit
         self.tweet_data = []
        
	def on_data(self, data):
         saveFile = io.open('/home/tanvi/Documents/1tweets.json', 'a', encoding='utf-8')
         if self.counter<1:
             try:
                    self.tweet_data.append(data)
                    self.counter+=1
                    saveFile = io.open('/home/tanvi/Documents/1tweets.json', 'w', encoding='utf-8')
                    saveFile.write(u'[\n')
                    saveFile.write(',\n'.join(self.tweet_data))
                    saveFile.write(u'\n]')
                    print(self.counter)
                    return True
             except:
                        print 'failed ondata,'
                        time.sleep(5)
                        pass   
         else:
            return False
         saveFile.close()
         print("file closed")
         exit()
         
        def on_error(self, status):
            print(status)
            return True
#    def on_status(self, status):
#        record = {'Text': status.text, 'Created At': status.created_at}
#        print record #See Tweepy documentation to learn how to access other fields
#        self.num_tweets += 1
#        if self.num_tweets < 20:
#            collection.insert(record)
#            return True
#        else:
#            return False


start_time = time.time() #grabs the system time
keyword_list = ['my pregnancy'] #track list

auth = OAuthHandler(ckey, consumer_secret) #OAuth object
auth.set_access_token(access_token_key, access_token_secret)
twitterStream = Stream(auth, listener(start_time)) #initialize Stream object with a time out limit
twitterStream.filter(track='my pregnancy', languages=['en'],stall_warnings=True)  