import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import RegexpTokenizer

from nltk.stem.wordnet import WordNetLemmatizer
from collections import Counter
import numpy as np

# reference signal words and word pairs that might indicate a need for the action "donate"
donateUnigrams = ['relief', 'aid', 'money', 'donate', 'bills', 'fees', 'costly', 'expensive', 'cost',
'give', 'dire', 'flooding', 'earthquake', 'storm', 'hurricane', 'evacuate', 'vulnerable', 'landslides',
'loss', 'tragedy', 'worst', 'lack', 'catastrophe', 'destruction', 'recover', 'recovered', 'damage', 'damaged', 'need',
'help']

donateBigrams = [('natural', 'disaster'), ('hospital', 'bills'), ('economic', 'crisis'), ('economic', 'disaster')]


# compile stop words
stop_words = set(stopwords.words("english"))
f = open('new_stop_words.txt', "r")
new_words = f.readlines()
f.close()
stop_words = stop_words.union(new_words)


# Takes text, a string, and returns topUnigrams and topBigrams, the top
# key words(15) and key word pairs(5), as well as two Counter objects, 
# counterUnigrams, counterBigrams that has a count of all key words and 
# key word pairs in text
def getKeyWords(text):

    # keep letter, numbers, end punctuation
    text = re.sub('[^a-zA-Z0-9 \n\.?!]', '', text)


    #Convert to lowercase
    text = text.lower()
    
    #remove tags
    text=re.sub("&lt;/?.*?&gt;"," &lt;&gt; ",text)
    

    ##Convert to list from string
    text = text.split()
    

    #Lemmatisation and removal of stop words
    lem = WordNetLemmatizer()
    unigrams = [lem.lemmatize(word) for word in text if not word in  
            stop_words] 

    
    counterUnigrams = Counter(unigrams)
    topUnigrams = counterUnigrams.most_common(15)


    text = " ".join(unigrams)
    sentences = text.split('.')


    bigramList = [b for l in sentences for b in zip(l.split(" ")[:-1], l.split(" ")[1:])]
    bigrams = []
    for b in bigramList:
        if ((b[0] != '') and (b[1] != '')):
            bigrams.append(b)
    counterBigrams = Counter(bigrams)
    topBigrams = counterBigrams.most_common(5)


    return topUnigrams, topBigrams, counterUnigrams, counterBigrams



# Signal Word Score determines the number of times that words that signal a particular action
# such as "donate" occurs within a text, as an absolute number of occurences. Takes 
# the unigram and bigram list, uniCounter and biCounter, as well as the reference unigrams
# and bigrams attached to a particular action, refUniList and refBiList, to return
# the signal word score
def getSignalWordScore(uniCounter, biCounter, refUniList, refBiList):

    countUnigrams = [uniCounter[word] for word in refUniList]
    countBigrams =  [biCounter[word] for word in refBiList]
    sum = np.sum(countUnigrams) + np.sum(countBigrams)

    return sum


    



def main():
    f = open("corralreef.txt", "r", encoding="utf-8")
    text = f.read()
    
    topUnigrams, topBigrams, counterUnigrams, counterBigrams = getKeyWords(text)

    # turns lists into strings
    topUnigrams = [word[0] for word in topUnigrams]
    topUnigrams = ", ".join(topUnigrams)
    topBigrams = [(word[0][0] + ' ' + word[0][1]) for word in topBigrams]
    topBigrams = ", ".join(topBigrams)

    # Prints top key words and key word pairs in the article
    print('Top Key Words')
    print(topUnigrams)
    print('Top Key Word Pairs')
    print(topBigrams)


    # Signal Word Score for Action: Donate
    print('Signal Word Score for Action: \'Donate\'')
    print(getSignalWordScore(counterUnigrams, counterBigrams, donateUnigrams, donateBigrams))




if __name__ == "__main__":
    main()