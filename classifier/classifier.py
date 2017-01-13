#classifier.py
#Written by Alex Mathson and Noah Brackenbury
#CS 322, Fall 2015
#This program constructs language models from the writing of different
#authors and uses these language models to calculate the relative
#probability that a given sentence was written by a certain author.

import urllib.request
import string
import re
import sys
import math
import random

def main():
    global dictionary
    dictionary = set(open('/usr/share/dict/words', 'r').read().lower().splitlines())
    
    if len(sys.argv) > 1 and sys.argv[1] == '-dev':
        languageModels = {}
        authors = open(sys.argv[2]).read().splitlines()
        print('Training language models, this may take some time.')
        for line in authors:
            temp = line.split(',')
            author = temp[0]
            url = temp[1]
            languageModels[author] = LanguageModel(url, author, 'false')
        print('Finished training language models.')
        for key1 in list(languageModels.keys()):
            numberCorrect = 0
            for line in languageModels[key1].getDevSet():
                probabilities = {}
                print(numberCorrect)
                print(line)
                for key2 in list(languageModels.keys()):
                    probabilities[key2] = languageModels[key2].prob(line)
                if max(probabilities) == key1:
                    numberCorrect += 1
            print(key1 + ' ' + str(numberCorrect) + ' / ' + str(len(languageModels[key1].getDevSet())))
                    
          
    elif len(sys.argv) > 2 and sys.argv[1] == '-test':
        languageModels = {}
        authors = open(sys.argv[2]).read().splitlines()
        testSet = open(sys.argv[3]).read().lower().splitlines()
        print('Training language models, this may take some time.')
        for line in authors:
            temp = line.split(',')
            author = temp[0]
            url = temp[1]
            languageModels[author] = LanguageModel(url, author, 'true')
        print('Finished training language models.')
        for line in testSet:
            probabilities = {}
            for key in languageModels.keys():
                probabilities[key] = languageModels[key].prob(line)
            print(max(probabilities))
                
    else:
        print('Usage:\npython3 classifier.py -dev authorlist\npython3 classifier.py -test authorlist testset.txt')
        sys.exit()
        
                          

class LanguageModel:
    def __init__(self, url, authorname, isTesting):
        self.name = authorname
        self.text = urllib.request.urlopen(url).read().decode('utf-8')
        self.testing = isTesting
        self.counts = {}
        self.bigramCounts = {}
        self.valCounts = []
        self.lines = self.text.split('\n')
        self.tokenized = []
        self.devSet = []
        
        for i in range(100):
                self.devSet.append(self.lines[int(random.random()*len(self.lines))])
                print('Appending to dev set')
        
        if self.testing:
            for line in self.lines:
                line = line.lower()
                line = re.sub("[-—]+", ' ', line)
                line = re.sub(r'[\.,"\':\(\)\-—;\\/\|_]+', '', line)
                prevWord = '<start>'
                if prevWord in self.counts:
                    self.counts[prevWord] += 1
                else:
                    self.counts[prevWord] = 1
                for word in line.split():
                    if word in dictionary:
                        if word in self.counts:
                            self.counts[word] += 1
                        else:
                            self.counts[word] = 1
                        if prevWord in self.bigramCounts:
                            if word in self.bigramCounts[prevWord]:
                                self.bigramCounts[prevWord][word] += 1
                            else:
                                self.bigramCounts[prevWord][word] = 1
                        else:
                            self.bigramCounts[prevWord] = {}
                            self.bigramCounts[prevWord][word] = 1
                        prevWord = word
                    else:
                        line = str.replace(line, word, '<unk>')
                        word = '<unk>'
                        if word in self.counts:
                            self.counts[word] += 1
                        else:
                            self.counts[word] = 1
                        if prevWord in self.bigramCounts:
                            if word in self.bigramCounts[prevWord]:
                                self.bigramCounts[prevWord][word] += 1
                            else:
                                self.bigramCounts[prevWord][word] = 1
                        else:
                            self.bigramCounts[prevWord] = {}
                            self.bigramCounts[prevWord][word] = 1
                        prevWord = word
                word = '<end>'
                if prevWord in self.bigramCounts:
                    if word in self.bigramCounts:
                        self.bigramCounts[prevWord][word] += 1
                    else:
                        self.bigramCounts[prevWord][word] = 1
                else:
                    self.bigramCounts[prevWord] = {}
                    self.bigramCounts[prevWord][word] = 1
                self.tokenized.append(line)
                for k1, v1 in self.bigramCounts.items():
                    for k2, v2 in self.bigramCounts[k1].items():
                        self.valCounts.append(v2)
                        
        else:
            for line in self.lines:
                line = line.lower()
                line = re.sub("[-—]+", ' ', line)
                line = re.sub(r'[\.,"\':\(\)\-—;\\/\|_]+', '', line)
                prevWord = '<start>'
                if prevWord in counts:
                    counts[prevWord] += 1
                else:
                    counts[prevWord] = 1
                for word in line.split():
                    if word in dictionary:
                        if word in self.counts:
                            self.counts[word] += 1
                        else:
                            self.counts[word] = 1
                        if prevWord in self.bigramCounts:
                            if word in self.bigramCounts[prevWord]:
                                self.bigramCounts[prevWord][word] += 1
                            else:
                                self.bigramCounts[prevWord][word] = 1
                        else:
                            self.bigramCounts[prevWord] = {}
                            self.bigramCounts[prevWord][word] = 1
                        prevWord = word
                    else:
                        line = str.replace(line, word, '<unk>')
                        if word in self.counts:
                            self.counts[word] += 1
                        else:
                            self.counts[word] = 1
                        if prevWord in self.bigramCounts:
                            if word in self.bigramCounts[prevWord]:
                                self.bigramCounts[prevWord][word] += 1
                            else:
                                self.bigramCounts[prevWord][word] = 1
                        else:
                            self.bigramCounts[prevWord] = {}
                            self.bigramCounts[prevWord][word] = 1
                        prevWord = word
                    word = '<end>'
                    if prevWord in self.bigramCounts:
                        if word in self.bigramCounts:
                            self.bigramCounts[prevWord][word] += 1
                        else:
                            self.bigramCounts[prevWord][word] = 1
                    else:
                        self.bigramCounts[prevWord] = {}
                        self.bigramCounts[prevWord][word] = 1
                        self.tokenized.append(line)
                lineCount += 1            
            for k1, v1 in self.bigramCounts.items():
                for k2, v2 in self.bigramCounts[k1].items():
                    self.valCounts.append(v2)        
    
    #Returns the number of times the unigram word was encountered while training this language model.        
    def getCount(word):
        if word in self.counts:
            return self.count[word]
        else: 
            return 0
     
    #Returns the number of times the bigram word1 word2 was encountered while training this language model.   
    def getBigramCount(word1, word2):
        if word1 in self.bigramCounts:
            if word2 in self.bigramCounts[word1]:
                return self.bigramCounts[word1][word2]
            else:
                return 0
        else:
            return 0
     
    #Returns the number of bigrams that appeared value times while training this language model.       
    def getValCount(value):
        return valCount.count(value)
     
    #Returns the log of the probability of line appearing based on the training of this language model.   
    def prob(self, line):
        probability = 0.0
        line = line.lower()
        line = re.sub("[-—]+", ' ', line)
        line = re.sub(r'[\.,"\':\(\)\-—;\\/\|_]+', '', line)
        prevWord = '<start>'
        for word in line.split():
            if word not in self.counts or word not in self.bigramCounts[prevWord]:
                word = '<unk>'
            if prevWord not in self.bigramCounts:
                probability += math.log(((self.valCounts.count(1)) / (math.pow(len(self.counts), 2) - len(self.bigramCounts))) / self.counts[prevWord])
            elif self.bigramCounts[prevWord][word] < 6:
                probability += math.log(((self.bigramCounts[prevWord][word] + 1) * self.valCounts.count(self.bigramCounts[prevWord][word] + 1)) / self.valCounts.count(self.bigramCounts[prevWord][word]))
            else:    
                probability += math.log(self.bigramCounts[prevWord][word] / self.counts[prevWord])
            prevWord = word
        word = '<end>'
        if self.bigramCounts[prevWord][word] < 6:
            probability += math.log(((self.bigramCounts[prevWord][word] + 1) * self.valCounts.count(self.bigramCounts[prevWord][word] + 1)) / self.valCounts.count(self.bigramCounts[prevWord][word]))
        else:    
            probability += math.log(self.bigramCounts[prevWord][word] / self.counts[prevWord])
        return probability
        
    def getDevSet(self):
        return self.devSet

if __name__ == '__main__':
    main()
