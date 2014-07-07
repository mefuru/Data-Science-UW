# compute the term frequency histogram of the livestream data you harvested from Problem 1.
# The frequency of a term can be calculated as [# of occurrences of the term in all tweets]/[# of occurrences of all terms in all tweets]

import json
import sys

def main():
    tweet_file = open(sys.argv[1])
    num_occurances_all_terms_all_tweets = 0
    term_occurances = {}
    # have a dict that maps words to number of occurances
    # Calculate sentiment for each tweet and initialise dict containing words with score 0
    for line in tweet_file:
        if 'text' in json.loads(line): # if object contains key 'text' field
            tweetText = json.loads(line)['text'].lower().encode('utf8')
            words = tweetText.split()
            num_occurances_all_terms_all_tweets += len(words)
            for i in range(0, len(words)-1):
                if words[i] not in term_occurances:
                    term_occurances[words[i]] = 1
                else: # increment term_sentiment score by sentiment Score
                    term_occurances[words[i]] += 1
        
    for key in term_occurances:
        frequency = round(term_occurances[key]/num_occurances_all_terms_all_tweets, 4)
        print '{0} {1}'.format(key, frequency)
                
if __name__ == '__main__':
    main()
