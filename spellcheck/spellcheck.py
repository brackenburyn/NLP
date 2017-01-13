#spellcheck.py
#Written by Alex Mathson and Noah Brackenbury
#CS 322, Fall 2015
#This program spellchecks a given file and creates a corrected document

import string
import sys
import re

#Sets up a global list of words to be used by this program.
def main():
    global dictionary 
    dictionary = open('/usr/share/dict/words', 'r').read().lower().splitlines()
    global adjacency
    adjacency = {}
    makeAdjacencyDictionary()
    inputPath = sys.argv[1]
    inputFile = open(inputPath, 'r')
    corrected = open('corrected_' + inputPath, 'w')
    ignore = string.punctuation + '—'
    for line in inputFile.readlines():
        line = line.lower()
        tokenized = re.sub(r'([\.,":\(\)\-—;\\/\|])+', r' \1 ', line)
        tokenized = re.sub("'", '', tokenized)
        for word in tokenized.split():
            if word not in ignore:
                if not isWord(word):
                    corrections = []
                    distances = []
                    for correction in dictionary:
                        # This narrows down possible corrections to within two letters and if the first letter is the same
                        if abs(len(word)-len(correction)) <= 2 and word[0] == correction[0]:
                            corrections.append(correction)
                            distances.append(calculateDistance(word, correction))
                    bestCorrections = []
                    bestDistances = []
                    for i in range(0, min(len(corrections), 5)):
                        m = min(distances)
                        bestCorrection = distances.index(m)
                        bestCorrections.append(corrections[bestCorrection])
                        del corrections[bestCorrection]
                        del distances[bestCorrection]
                    print(word + ' is mispelled in the following line:')
                    print(line)
                    print('Enter the number of your correction: ')
                    print('0. Leave as is')
                    for i in range(0, 5):
                        if len(bestCorrections) > i:
                            print(str(i+1) + '. ' + bestCorrections[i])
                    choice = input('Enter the number of your correction: ')
                    for j in range(0, 5):
                        if int(choice) == (j+1):
                            line = line.replace(word, bestCorrections[j])
        corrected.write(line)
    inputFile.close()
    corrected.close()


#Returns a true if word is found in the system dictionary and false otherwise.
def isWord(word):
    return word in dictionary

#Calculates a modified Levenshtein Distance between word1 and word2.
def calculateDistance(word1, word2):
    if len(word2) == 0:
            return len(word1)

    firstRow = []
    for i in range(len(word1) + 1):
            firstRow.append(i)

    for i, char2 in enumerate(word2):
            secondRow = [0]
            secondRow[0] = i
            for j, char1 in enumerate(word1):
                    secondRow.append(min(firstRow[j + 1] + 1, secondRow[j] + 1, firstRow[j] + subCost(char1, char2)))
            firstRow = secondRow
    return secondRow[-1]

#Generates a dictionary using letters as keys.
#The values are tuples containing any characters adjacent to the key character
#on the keyboard.
def makeAdjacencyDictionary():
    adjacency['a'] = 'q', 'w', 's', 'z'
    adjacency['b'] = 'v', 'g', 'h', 'n'
    adjacency['c'] = 'x', 'd', 'f', 'v'
    adjacency['d'] = 'e', 'r', 'f', 'c', 'x', 's'
    adjacency['e'] = 'r', 'd', 's', 'w'
    adjacency['f'] = 'r', 't', 'g', 'v', 'c', 'd'
    adjacency['g'] = 't', 'y', 'h', 'b', 'v', 'f'
    adjacency['h'] = 'y', 'u', 'j', 'n', 'b', 'g'
    adjacency['i'] = 'u', 'j', 'k', 'o'
    adjacency['j'] = 'u', 'i', 'k', 'm', 'n', 'h'
    adjacency['k'] = 'i', 'o', 'l', 'm', 'j'
    adjacency['l'] = 'k', 'o', 'p'
    adjacency['m'] = 'n', 'j', 'k'
    adjacency['n'] = 'b', 'h', 'j', 'm'
    adjacency['o'] = 'i', 'k', 'l', 'p'
    adjacency['p'] = 'o', 'l'
    adjacency['q'] = 'w', 'a'
    adjacency['r'] = 'e', 'd', 'f', 't'
    adjacency['s'] = 'w', 'e', 'd', 'x', 'z', 'a'
    adjacency['t'] = 'r', 'f', 'g', 'y'
    adjacency['u'] = 'y', 'h', 'j', 'i'
    adjacency['v'] = 'c', 'f', 'g', 'b'
    adjacency['x'] = 'z', 's', 'd', 'c'
    adjacency['y'] = 't', 'g', 'h', 'u'
    adjacency['z'] = 'a', 's', 'x'

#Returns the integer cost of replacing char1 with char2.
def subCost(char1, char2):
    if char1 == char2:
        return 0

    elif char2 in adjacency[char1]:
        return 1.5

    else:
        return 2

if __name__ == '__main__':
    main()