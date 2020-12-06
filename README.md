# Speakable-Challenge
A python program to extract key words of an article and determines a score that indicates the relevance of a "Donate" button.
Completed for the challenge puzzle for Speakable.

What I Did
I created a Python program that takes an article and produces key words and key word pairs associated with that article. This program also produces a “word signal score” that indicates to some degree how much an article demands a particular action, such as “Donate”. In fact, my implementation right now only produces scores for “Donate”, but the same idea can be used for other actions.

Why I Did It
I saw that Speakable finds “inspiring content” on publisher websites and finds related actions. My program can aid in that process because it picks out key, important words of an article so we can get an idea of what articles are about without manually reading every one. Moreover, with the “word signal score” it helps us choose which particular actions are most suitable for the article by assigning to each action (Donate,  Petition, Volunteer) a score that lets us how much that particular action is relevant to the article.

How I Did It
To pick out key words and key word pairs, I first preprocessed the text (removing stop words, lemmatization, removing obscure characters). (I use a stopword list picked from the internet to remove stop words, but I recognize that this process is much more enhanced if we have a whole collection of articles so we can use tf-idf). Then I created counters of every unique word (unigram) and word pair (bigrams) in the text, and picked the most occurring unigrams and bigrams. To calculate a “word signal score”, I generate my own list of words that I thought indicated a need for donations like “bills” or “disaster” and count the occurences of those words and word pairs in the complete unigram and bigram lists. (This is an absolute score, so we can make this better by making the score relative to the length of the article. Moreover, we can make this better by creating the lists not by hand but by finding patterns among previous articles that have a “donate” button assigned to it).

Author: Long Ho
