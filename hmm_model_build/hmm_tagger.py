#hmm_tagger.py
#Noah Brackenbury, with help from Wikipedia and Alex Mathson
#CS 322, Fall 2015
#This program calculates a the probability of a tag sequence based on a given 
#word sequence

import pickle
import sys
import string


def main():
    brown = pickle.load(open('countmodel.dat', 'rb'))
    inputString = sys.stdin.read()
    processed = inputString.lower()
    tags = ['adj', 'adt', 'adv', 'conj', 'det',
            'noun', 'num', 'pron', 'verb', '.']
    print(viterbi(processed, tags, hmm.startCounts, hmm.a, hmm.b))
#    for word in inputString:
#        lower = word.lower()
#        calculate tag
#        print(word + '/' + tag)
        
def viterbi(observations, tags, startProb, a, b):
    V = [{}]
    path = {}
    
    # Initialize base cases (t == 0)
    for i in tags:
        V[0][i] = startProb[i] * b[i][observations[0]]
        path[i] = [i]
    
    # Run Viterbi for t > 0
    for t in range(1, len(observations)):
        V.append({})
        newpath = {}

        for i in tags:
            (prob, state) = max((V[t-1][i0] * a[i0][i] * b[i][observations[t]], i0) for i0 in states)
            V[t][i] = prob
            newpath[i] = path[state] + [i]

        # Don't need to remember the old paths
        path = newpath
    n = 0           
    if len(observations) != 1:
        n = t
    (prob, state) = max((V[n][i], i) for i in states)
    return (prob, path[state])


if __name__ == '__main__':
    main()  