# Write a Python script top_ten.py that computes the ten most frequently occurring hashtags from the data you gathered in Problem 1.

import json
import sys
from collections import Counter #https://docs.python.org/2/library/collections.html

def main():
    tweet_file = open(sys.argv[1])
    hashtag_counter = [] # Store hashtags in a list
    for line in tweet_file:
        tweet = json.loads(line)
        if 'text' in tweet and tweet['entities']['hashtags']:
            hashtag = tweet['entities']['hashtags'][0]['text']
            hashtag_counter.append(hashtag)
    topTen = Counter(hashtag_counter).most_common()[:10] #https://docs.python.org/2/library/collections.html
    for hashtag in topTen:
        print '{0} {1}'.format(hashtag[0], hashtag[1])    

if __name__ == '__main__':
    main()

