#CMU_parser.py
#Alex Mathson and Noah Brackenbury
#CS 322, Fall 2015

import pickle

#Parses the CMU pronunciation dictionary to create a usable pronunciation dictionary.
def main():
	CMU_file = open('cmudict-0.7b.txt', encoding = 'ISO-8859-1')
	pronunciation_dict = {}
	for line in CMU_file:
		#Only adds to the dictionary if the line isn't a comment.
		if line[:3] != ';;;':
			word = line.split('  ')[0]
			pronunciation = line.split('  ')[1]
			pronunciation_dict[word] = pronunciation
	pickle.dump(pronunciation_dict, open('cmudict.dat', 'wb'))

if __name__ == '__main__':
	main()