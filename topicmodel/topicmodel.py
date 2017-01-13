# topicmodel.py
# Noah Brackenbury
# CS 322, Fall 2015
# With help from: Andy Exley's code and Stack Overflow for syntax
# This program takes a .txt file as input, and summarizes it in five words

import sys

def summarize(fileGiven, numberOfWords):
# This function chooses the most-used words in the given text file that 
# are 6 or more letters (as to exclude articles and conjunctions)
    words = []
    summary = []
    counts = []
    for line in fileGiven:
        for word in line.split():
            if len(word) >= 6:
                if word in summary:
                    place = summary.index(word)
                    counts[place] += 1
                else:
                    summary.append(word)
                    counts.append(1)
    # These nested loops keep track of how many times each important word
    # is used using two paralell lists
    for i in range(0, numberOfWords):
        m = max(counts)
        bestWord = counts.index(m)
        words.append(summary[bestWord])
        del counts[bestWord]
        del summary[bestWord]
    # This for loop adds the most used word to the output list and then
    # deletes it from the original list (in order to find the next 
    # most-used) 5 times
    return words

def main():
# The main function takes a .txt file as a parameter and prints the five
# summary words
    fileGiven = open(sys.argv[1])
    for word in summarize(fileGiven, 5):
        print (word)
    fileGiven.close()

if __name__ == '__main__':
    main()