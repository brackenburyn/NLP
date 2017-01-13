#parser.py
#Noah Brackenbury, Alex Mathson
#CS 322, Fall 2015
#This program uses a CFG file to parse the sentence provided as input.

import sys

def main():
    grammar_file = open(sys.argv[1])
    sentence = sys.argv[2]

	#This code builds a dictionary containing all of the rules from the CFG.
    grammar = {}
    for line in grammar_file:
        if line[0] != '#':
            line = line.replace('\n', '')
            if line.split(' -> ')[0] in grammar:
                grammar[line.split(' -> ')[0]].append(line.split(' -> ')[1])
            else:
                grammar[line.split(' -> ')[0]] = []
                grammar[line.split(' -> ')[0]].append(line.split(' -> ')[1])
    keys = list(grammar.keys())

    words = sentence.split()

	#Sets up the table for the CKY algorithm as a two-dimensional dictionary of lists.
    cky_table = {}
    for i in range(len(words)):
        cky_table[i] = {}
        for j in range(len(words)):
            cky_table[i][j] = []

	#Tags all of the terminal outputs.
    terminals = []
    for i in range(len(words)):
        for key in keys:
            if words[i] in grammar[key]:
                cky_table[i][i].append(key)
                terminals.append((key, words[i], [i,i,1]))

    nonterminals = []
    for i in range(1, len(words)):
        for j in range(i, -1, -1):
            for k in range(1, i+1):
                for key in keys:
                    values = grammar[key]
                    for value in values:
                        if len(value.split()) > 1 and value.split()[0] in cky_table[i-k][j] and value.split()[1] in cky_table[i][j+k]:
                            cky_table[j][i].append(key)
                            nonterminals.append((key, [i-k, j, 1], [i, j+k, 1]))
                            

    print(cky_table)
    print(terminals)
    print(nonterminals)
    print('S' in cky_table[0][len(words) - 1])
    if 'S' in cky_table[0][len(words) - 1]:
        print('(S' + '(')
    for i in terminals:
        print('(' + i[0] + ' ' + i[1] + ')')
    print(')')

if __name__ == '__main__':
    main()