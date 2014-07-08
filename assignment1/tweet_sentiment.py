import json
import sys
# print to stdout the sentiment of each tweet in the file, one numeric sentiment score per line. The first score should correspond to the first tweet, the second score should correspond to the second tweet, and so on.
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {} # initialize an empty dictionary
    sentiments = [] # initialise an empty list
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    for line in tweet_file:
        if 'text' in json.loads(line): # if object contains key 'text' field
            tweetText = json.loads(line)['text'].lower().encode('utf8')
            sentimentScore = 0
            for key in scores:
                if key in tweetText:
                    sentimentScore += scores[key]        
            sentiments.append(sentimentScore)
        else: #set sentiment score for line to 0 for lines that do not contain tweet data
            sentiments.append(0)
    for i in range(0, len(sentiments)):
        print sentiments[i]     

if __name__ == '__main__':
    main()
