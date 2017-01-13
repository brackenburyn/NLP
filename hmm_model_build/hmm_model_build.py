#hmm_model_build.py
#Noah Brackenbury
#CS 322, Fall 2015
#This program creates a language model with parts-of-speech tagging

import sys
import re
import string
import pickle


def main():
    brown = hmm(sys.argv[1])
    pickle.dump(brown, open('countmodel.dat', 'wb'))


class hmm:
    def __init__(self, thefile):
        self.text = open(thefile).read()
        self.a = {}
        self.b = {}
        self.lines = self.text.splitlines()
        self.counts = {}
        self.tagCounts = {}
        self.startCounts = {}
        self.testSet = []
        
    for line in self.lines:
        lineNumber = 0
        line = line.lower()
        line = re.sub("[-—]+", ' ', line)
        prevTag = '<start>'
        if prevTag in self.tagCounts:
            self.tagCounts[prevTag] += 1
        else:
            self.tagCounts[prevTag] = 1
        for word in line.split():
            word = re.sub(r'\/', ' ', word)
            aWord = 'true'
            examinedWord = ''
            for item in word.partition(' '):
                if aWord == 'true':
                    examinedWord = item
                    if examinedWord in self.counts:
                        self.counts[examinedWord] += 1
                    else:
                        self.counts[examinedWord] = 1
                    if lineNumber % 10 == 0:
                        self.testSet.append(examinedWord + ' ')
                aWord = 'false'
                if aWord == 'false':
                    if item != examinedWord and item != ' ':
                        if item in self.tagCounts:
                            self.tagCounts[item] += 1
                        else:
                            self.tagCounts[item] = 1
                        if prevTag in self.a:
                            if item in self.a[prevTag]:
                                self.a[prevTag][item] += 1
                            else:
                                self.a[prevTag][item] = 1
                        else:
                            self.a[prevTag] = {}
                            self.a[prevTag][item] = 1
                        if examinedWord in self.b:
                            if item in self.b[examinedWord]:
                                self.b[examinedWord][item] += 1
                            else:
                                self.b[examinedWord][item] = 1
                        else:
                            self.b[examinedWord] = {}
                            self.b[examinedWord][item] = 1
                        if prevTag == '<start>':
                            if item in self.startCounts:
                                self.startCounts[item] += 1
                            else:
                                self.startCounts[item] = 1
                        prevTag = item
        if prevTag in self.a:
            if '<end>' in self.a[prevTag]:
                self.a[prevTag]['<end>'] += 1
            else:
                self.a[prevTag]['<end>'] = 1
        else:
            self.a[prevTag] = {}
            self.a[prevTag]['<end>'] = 1
        lineNumber += 1
    print('Finished training language model.')
                    
    #Returns the number of times the unigram word was encountered while training this language model.        
    def getCounts(self, word):
        if word in self.counts:
            return self.counts[word]
        else: 
            return 0
        
    #Returns the number of times the unigram tag was encountered while training this language model.        
    def getTagCounts(self, tag):
        if tag in self.tagCounts:
            return self.tagCounts[tag]
        else: 
            return 0
     
    #Returns the number of times the bigram tag1, tag2 was encountered while training this language model.   
    def getA(self, tag1, tag2):
        if tag1 in self.a:
            if tag2 in self.a[tag1]:
                return self.a[tag1][tag2]
            else:
                return 0
        else:
            return 0
        
    #Returns the number of times a specific tag appears for a certain word for this language model.   
    def getB(self, word, tag):
        if word in self.b:
            if tag in self.b[word]:
                return self.b[word][tag]
            else:
                return 0
        else:
            return 0
                    
                    
if __name__ == '__main__':
    main()  