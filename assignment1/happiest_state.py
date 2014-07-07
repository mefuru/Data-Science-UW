# returns the name of the happiest state as a string.
import json
import sys

def main():
    states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
    }
    states_count = {}
    most_occurring_state_count = 0
    most_occurring_state = ''
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {} # initialize an empty dictionary
    sentiments = [] # initialise an empty list

    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    # Calculate sentiment for each tweet and initialise dict containing words with score 0
    for line in tweet_file:
        tweet = json.loads(line)
        if 'user' in tweet and 'location' in tweet['user']:
            tweetText = json.loads(line)['text'].lower().encode('utf8')
            sentimentScore = 0
            for key in scores: # iterate over scores 
                if key in tweetText: #  if tweetText contains term, incremement sentiment score
                    sentimentScore += scores[key]        
            sentiments.append(sentimentScore)
            for key in states:
                if states[key] in tweet['user']['location']:
                    if key not in states_count:
                        states_count[key] = sentimentScore
                    else:
                        states_count[key] += sentimentScore
        else: #set sentiment score for line to 0 for lines that do not contain tweet data
            sentiments.append(0)
                
    # print most occuring state
    for key in states_count:
        if states_count[key] > most_occurring_state_count:
            most_occurring_state_count = states_count[key]
            most_occurring_state = key

    print most_occurring_state
            

if __name__ == '__main__':
    main()
