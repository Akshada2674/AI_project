#Import Natural Language Toolkit (NLTK)
import nltk 

import numpy as np

#Install punkt module from nltk used for tokenizing text, specifically for dividing text into sentences.
#nltk.download('punkt')

#For Stemming 
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence , all_words):
    tokenized_sentence = [stem(w) for w in tokenized_sentence]
    
    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx , w in enumerate(all_words):
        if w in tokenized_sentence:
            bag[idx] = 1.0
    
    return bag


'''
#Tokenization
a = "What documents are required?"
print(a)
a= tokenize(a)
print(a)

Output: 
What documents are required?
['What', 'documents', 'are', 'required', '?']

#Stemming

words=["Organize","organizes","organizing"]
stemmed_words = [stem(w) for w in words]
print(stemmed_words)

Output:
    ['organ', 'organ', 'organ']

#bag of words eg.

sentence = ['hello','how','are','you']
words = ['hi','hello','I','you','bye','thank','cool']
#actual ans [0. 1. 0. 1. 0. 0. 0.]
bag = bag_of_words(sentence,words)
print(bag)

Output: [0. 1. 0. 1. 0. 0. 0.]
'''