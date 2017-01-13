# stemmer.py
# Written by Alex MAthson and Noah Brackenbooty
# CS 322, Fall 2015
# This program stems any word in English

import string
import re

#The main function prompts the user to enter a word and prints the stem of that word.
def main():
    userInput = input('Enter the word to be stemmed: ')
    print(stem(userInput))

def stem(word):
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
    vowels = ['a', 'e', 'i', 'o', 'u']
    word = word.lower()    
    #Step 1a
    message = re.sub('sses$', 'ss', word)
    if message == word:
        message = re.sub('ies$', 'i', word)
    if message == word:
        message = re.sub('([^s])s$', r'\1', word)
    #Step 1b
    taboo = ['l', 's', 'z', 'a', 'e', 'i', 'o', 'u', 'y']
    word = message
    if len(message) >= 3 and message[-3:] == 'eed' and getM(message[:-3]) > 0:
        message = re.sub('eed$', 'ee', message)
    elif len(message) >= 2 and message[-2:] == 'ed':
        word = message
        message = re.sub('(([b-df-hj-np-tv-xz]y|[aeiou])[b-df-hj-np-tv-z]*)ed', r'\g<1>', message)
        if word != message:
            message = re.sub('at$', 'ate', message)
            message = re.sub('bl$', 'ble', message)
            message = re.sub('iz$', 'ize', message)
            if len(message) >= 2 and message[-2] == message[-1] and message[-1] not in taboo:
                message = re.sub('.$', '', message)
            if len(message) >= 3 and getM(message) == 1 and (message[-3] in consonants or message[-3] == 'y') \
            and (message[-2] in vowels or message[-2] == 'y') \
            and message[-1] in consonants and message[-1] != ('w' or 'x' or 'y'):
                message = re.sub('$', 'e', message)
                
    elif len(message) >= 3:
        message = re.sub('(([b-df-hj-np-tv-xz]y|[aeiou])[b-df-hj-np-tv-z]*)ing', r'\g<1>', message)
        if word != message:
            message = re.sub('at$', 'ate', message)
            message = re.sub('bl$', 'ble', message)
            message = re.sub('iz$', 'ize', message)
            if len(message) >= 2 and message[-2] == message[-1] and message[-1] not in taboo:
                message = re.sub('.$', '', message)
            if len(message) >= 3 and getM(message) == 1 and (message[-3] in consonants or message[-3] == 'y') \
            and (message[-2] in vowels or message[-2] == 'y') \
            and message[-1] in consonants and message[-1] != ('w' or 'x' or 'y'):
                message = re.sub('$', 'e', message)
    #Step 1c
    message = re.sub('(([b-df-hj-np-tv-xz]y|[aeiou])[b-df-hj-np-tv-z]*)y', r'\g<1>i', message)
    
    # Step 2
    if len(message) >= 7 and message[-7:] == 'ational' and getM(message[:-7]) > 0:
        message = re.sub('ational$', 'ate', message)
    if len(message) >= 6 and message[-6:] == 'tional' and getM(message[:-6]) > 0:
        message = re.sub('tional$', 'tion', message)
    if len(message) >= 4 and message[-4:] == 'enci' and getM(message[:-4]) > 0:
        message = re.sub('enci$', 'ence', message)
    if len(message) >= 4 and message[-4:] == 'anci' and getM(message[:-4]) > 0:
        message = re.sub('anci$', 'ance', message)
    if len(message) >= 4 and message[-4:] == 'izer' and getM(message[:-4]) > 0:
        message = re.sub('izer$', 'ize', message)
    if len(message) >= 4 and message[-4:] == 'abli' and getM(message[:-4]) > 0:
        message = re.sub('abli$', 'able', message)
    if len(message) >= 4 and message[-4:] == 'alli' and getM(message[:-4]) > 0:
        message = re.sub('alli$', 'al', message)
    if len(message) >= 5 and message[-5:] == 'entli' and getM(message[:-5]) > 0:
        message = re.sub('entli$', 'ent', message)
    if len(message) >= 3 and message[-3:] == 'eli' and getM(message[:-3]) > 0:
        message = re.sub('eli$', 'e', message)
    if len(message) >= 5 and message[-5:] == 'ousli' and getM(message[:-5]) > 0:
        message = re.sub('ousli$', 'ous', message)
    if len(message) >= 7 and message[-7:] == 'ization' and getM(message[:-7]) > 0:
        message = re.sub('ization$', 'ize', message)
    if len(message) >= 5 and message[-5:] == 'ation' and getM(message[:-5]) > 0:
        message = re.sub('ation$', 'ate', message)
    if len(message) >= 4 and message[-4:] == 'ator' and getM(message[:-4]) > 0:
        message = re.sub('ator$', 'ate', message)
    if len(message) >= 5 and message[-5:] == 'alism' and getM(message[:-5]) > 0:
        message = re.sub('alismd$', 'al', message)
    if len(message) >= 7 and message[-7:] == 'iveness' and getM(message[:-7]) > 0:
        message = re.sub('iveness$', 'ive', message)
    if len(message) >= 7 and message[-7:] == 'fulness' and getM(message[:-7]) > 0:
        message = re.sub('fulness$', 'ful', message)
    if len(message) >= 7 and message[-7:] == 'ousness' and getM(message[:-7]) > 0:
        message = re.sub('ousness$', 'ous', message)
    if len(message) >= 5 and message[-5:] == 'aliti' and getM(message[:-5]) > 0:
        message = re.sub('aliti$', 'al', message)
    if len(message) >= 5 and message[-5:] == 'iviti' and getM(message[:-5]) > 0:
        message = re.sub('iviti$', 'ive', message)
    if len(message) >= 6 and message[-6:] == 'biliti' and getM(message[:-6]) > 0:
        message = re.sub('biliti$', 'ble', message)
    
    #Step 3
    word = message
    if len(message) >= 5 and message[-5:] == 'icate' and getM(message[:-5]) > 0:
        message = re.sub('icate$', 'ic', message)
    elif len(message) >= 5 and message[-5:] == 'ative' and getM(message[:-5]) > 0:
        message = re.sub('ative$', '', message)
    elif len(message) >= 5 and message[-5:] == 'alize' and getM(message[:-5]) > 0:
        message = re.sub('alize$', 'al', message)
    elif len(message) >= 5 and message[-5:] == 'iciti' and getM(message[:-5]) > 0:
        message = re.sub('iciti$', 'ic', message)
    elif len(message) >= 4 and message[-4:] == 'ical' and getM(message[:-4]) > 0:
        message = re.sub('ical$', 'ic', message)
    elif len(message) >= 3 and message[-3:] == 'ful' and getM(message[:-3]) > 0:
        message = re.sub('ful$', '', message)
    elif len(message) >= 4 and message[-4:] == 'ative' and getM(message[:-4]) > 0:
        message = re.sub('ness$', '', message)
        
    #Step 4
    word = message
    if len(message) >= 2 and message[-2:] == 'al' and getM(message[:-2]) > 1:
        message = re.sub('al$', '', message)
    elif len(message) >= 4 and message[-4:] == 'ance' and getM(message[:-4]) > 1:
        message = re.sub('ance$', '', message)
    elif len(message) >= 4 and message[-4:] == 'ence' and getM(message[:-4]) > 1:
        message = re.sub('ence$', '', message)
    elif len(message) >= 2 and message[-2:] == 'er' and getM(message[:-2]) > 1:
        message = re.sub('er$', '', message)
    elif len(message) >= 2 and message[-2:] == 'ic' and getM(message[:-2]) > 1:
        message = re.sub('ic$', '', message)
    elif len(message) >= 4 and message[-4:] == 'able' and getM(message[:-4]) > 1:
        message = re.sub('able$', '', message)
    elif len(message) >= 4 and message[-4:] == 'ible' and getM(message[:-4]) > 1:
        message = re.sub('ible$', '', message)
    elif len(message) >= 3 and message[-3:] == 'ant' and getM(message[:-3]) > 1:
        message = re.sub('ant$', '', message)
    elif len(message) >= 5 and message[-5:] == 'ement' and getM(message[:-5]) > 1:
        message = re.sub('ement$', '', message)
    elif len(message) >= 4 and message[-4:] == 'ment' and getM(message[:-4]) > 1:
        message = re.sub('ment$', '', message)
    elif len(message) >= 3 and message[-3:] == 'ent' and getM(message[:-3]) > 1:
        message = re.sub('ent$', '', message)
    elif len(message) >= 4 and message[-3:] == 'ion' and getM(message[:-3]) > 1:
        message = re.sub('[st]ion$', '', message)
    elif len(message) >= 2 and message[-2:] == 'ou' and getM(message[:-2]) > 1:
        message = re.sub('ou$', '', message)
    elif len(message) >= 3 and message[-3:] == 'ism' and getM(message[:-3]) > 1:
        message = re.sub('ism$', '', message)
    elif len(message) >= 3 and message[-3:] == 'ate' and getM(message[:-3]) > 1:
        message = re.sub('ate$', '', message)
    elif len(message) >= 3 and message[-3:] == 'iti' and getM(message[:-3]) > 1:
        message = re.sub('iti$', '', message)
    elif len(message) >= 3 and message[-3:] == 'ous' and getM(message[:-3]) > 1:
        message = re.sub('ous$', '', message)
    elif len(message) >= 3 and message[-3:] == 'ive' and getM(message[:-3]) > 1:
        message = re.sub('ive$', '', message)
    elif len(message) >= 3 and message[-3:] == 'ize' and getM(message[:-3]) > 1:
        message = re.sub('ize$', '', message)
        
    #Step 5a
    if len(message) >= 3 and message[-1] == 'e' and getM(message[:-1]) > 1:
        message = re.sub('e$', '', message)
    elif len(message) >= 1 and message[:-1] == 'e' and getM(message[:-1]) > 1 and\
    (len(message) < 4 or message[-4] not in consonants or message[-3] not in vowels\
    or message[-2] not in consonants or message[-2] == ('w' or 'x' or 'y')):
        message = re.sub('e$', '', message)
        
    #Step 5b
    if len(message) >= 3 and message[-2] == message[-1] and message [-2] == 'l' and\
    getM(message) > 1:
        message = re.sub('l$', '', message)
    return message

#This function calculates the M value of a word as Porter describes it.
def getM(word):
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
    vowels = ['a', 'e', 'i', 'o', 'u']
    m = 0
    chars = list(word)
    #The loops strip vowels off the end of the list and consonants off the start of the list.
    while chars[-1] in vowels:
        chars.pop()
        if len(chars) == 0:
            return m
    if len(chars) >= 2 and chars[-1] == 'y' and chars[-2] in consonants:
        chars.pop()
        if len(chars) == 0:
            return m
    if chars[0] == 'y':
        chars.pop(0)
        if len(chars) == 0:
            return m
    while (len(chars) >= 1) and (chars[0] in consonants):
        chars.pop(0)
        if len(chars) == 0:
            return m
    while 'true':
        if len(chars) == 0:
            return m
        if chars[0] in vowels:
            m+=1
            while chars[0] in vowels:
                chars.pop(0)
                if len(chars) == 0:
                    return m
        if chars[0] in consonants:
            while chars[0] in consonants:
                chars.pop(0)
                if len(chars) == 0:
                    return m

if __name__ == '__main__':
    main()


