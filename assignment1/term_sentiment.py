import json
import sys

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {}
    sentiments = []
    term_sentiment = {}

    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    # Calculate sentiment for each tweet and initialise dict containing words with score 0
    for line in tweet_file:
        if 'text' in json.loads(line): # if object contains key 'text' field
            tweetText = json.loads(line)['text'].lower().encode('utf8')
            sentimentScore = 0
            for key in scores: # iterate over scores 
                if key in tweetText: #  if tweetText contains term, incremement sentiment score
                    sentimentScore += scores[key]        
            sentiments.append(sentimentScore)
            words = tweetText.split()
            for i in range(0, len(words)-1):
                # if word is not in the term_sentiment dictionary, add it to term_sentiment with sentiment score of this tweet
                if words[i] not in term_sentiment:
                    term_sentiment[words[i]] = sentimentScore
                else: # increment term_sentiment score by sentiment Score
                    term_sentiment[words[i]] += sentimentScore
        else: #set sentiment score for line to 0 for lines that do not contain tweet data
            sentiments.append(0)
    
    for key in term_sentiment:
        print '{0} {1}'.format(key, term_sentiment[key])
            
if __name__ == '__main__':
    main()

# script that computes the sentiment for the terms that do not appear in the file AFINN-111.txt.
# We will run your script on a file that contains strongly positive and strongly
# negative tweets and verify that the non-sentiment-carrying terms in the
# strongly positive tweets are assigned a higher score than the non-sentiment-carrying
# terms in negative tweets. Your scores need not (and likely will not) exactly match
# any specific solution.

# First, get a list of all non sentiment carrying tweets
# Then assign a nummber to it by going through all tweets that contain the word and then checking that tweet's sentiments
# Create a dictionary that has these non sentiment carrying words and change their key, which is their score
