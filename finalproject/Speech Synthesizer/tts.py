# tts.py
# Noah Brackenbury and Alex Mathson
# CS 322, Fall 2015
# This program produces a .wav file with speech of the given text

import sys
import wave
import pickle
import re

def main():
    global pronunciationDict 
    pronunciationDict = pickle.load(open('cmudict.dat', 'rb'))
    inputWords = sys.argv[1].upper().split()
    phones = ''
    for word in inputWords:
        phones += getPhones(word)
        phones += ' q '
    phones = re.sub('[0-9]', '', phones)
    print(phones)
    makeWavFile(phones)

#Returns the Arpabet phones for an English word.
def getPhones(word):
    #If word is in the dictionary, return its phones.
    if word in pronunciationDict:
        return pronunciationDict[word]
    #Otherwise, try to figure out the phones with regular expressions.
    else:
        print(word + ' not in pronunciation dictionary.')
        word = word.lower()
        arpabet = word
        #Handles word final s.
        arpabet = re.sub('([a-bd-egi-jl-oru-wy-z])s$', r'\1 Z ', arpabet)
        arpabet = re.sub('s$', ' S ', arpabet)
        #Handles R-colored vowels.
        arpabet = re.sub('air | ere', ' EHR ', arpabet)
        arpabet = re.sub('ur', ' UHR ', arpabet)
        arpabet = re.sub('or | ore', ' AOR ', arpabet)
        arpabet = re.sub('ear', ' IHR ', arpabet)
        arpabet = re.sub('ar', ' AAR ', arpabet)
        arpabet = re.sub('er | ir$ | ir([b-df-hj-np-tv-xz][b-df-hj-np-tv-xz])', r' ER \1', arpabet)
        #Handles special vowel cases.
        arpabet = re.sub('a([b-df-hj-np-tv-xz][b-df-hj-np-tv-xz])', r' AE \1', arpabet)
        arpabet = re.sub('a([b-df-hj-np-tv-xz])', r' EY \1', arpabet)
        arpabet = re.sub('ee', 'IY', arpabet)
        arpabet = re.sub('i([b-df-hj-np-tv-xz][aeiou])', r' AY \1', arpabet)
        arpabet = re.sub('oo', ' UW ', arpabet)
        arpabet = re.sub('ou', ' UH ', arpabet)
        arpabet = re.sub('u([b-df-hj-np-tv-xz][aeiou])', r' UW \1', arpabet)
        arpabet = re.sub('y$', ' IY ', arpabet)
        #Deletes word final e.
        arpabet = re.sub('e$', '', arpabet)
        #Handles special consonant cases.
        arpabet = re.sub('ch', ' CH ', arpabet)
        arpabet = re.sub('th', ' TH ', arpabet)
        arpabet = re.sub('sh', ' SH ', arpabet)
        arpabet = re.sub('tt', ' DX ', arpabet)
        arpabet = re.sub('wh', ' W ', arpabet)
        arpabet = re.sub('ng', ' NG ', arpabet)
        arpabet = re.sub('^x', ' Z ', arpabet)
        arpabet = re.sub('^pn', ' N ', arpabet)
        arpabet = re.sub('^gh', ' G ', arpabet)
        arpabet = re.sub('gh', ' F ', arpabet)
        arpabet = re.sub('pp', ' P ', arpabet)
        arpabet = re.sub('ck', ' K ', arpabet)
        #Handles all other cases.
        arpabet = re.sub('a', ' AA ', arpabet)
        arpabet = re.sub('b', ' B ', arpabet)
        arpabet = re.sub('c', ' K ', arpabet)
        arpabet = re.sub('d', ' D ', arpabet)
        arpabet = re.sub('e', ' EH ', arpabet)
        arpabet = re.sub('f', ' F ', arpabet)
        arpabet = re.sub('g', ' G ', arpabet)
        arpabet = re.sub('h', ' HH ', arpabet)
        arpabet = re.sub('i', ' IH ', arpabet)
        arpabet = re.sub('j', ' JH ', arpabet)
        arpabet = re.sub('k', ' K ', arpabet)
        arpabet = re.sub('l', ' L ', arpabet)
        arpabet = re.sub('m', ' M ', arpabet)
        arpabet = re.sub('n', ' N ', arpabet)
        arpabet = re.sub('o', ' OW ', arpabet)
        arpabet = re.sub('p', ' P ', arpabet)
        arpabet = re.sub('q', ' K ', arpabet)
        arpabet = re.sub('r', ' R ', arpabet)
        arpabet = re.sub('s', ' S ', arpabet)
        arpabet = re.sub('t', ' T ', arpabet)
        arpabet = re.sub('u', ' AH ', arpabet)
        arpabet = re.sub('v', ' V ', arpabet)
        arpabet = re.sub('w', ' W ', arpabet)
        arpabet = re.sub('x', ' K S ', arpabet)
        arpabet = re.sub('y', ' Y ', arpabet)
        arpabet = re.sub('z', ' Z ', arpabet)
        return arpabet
        
#Creates a wave file out of the sequence of Arpabet phones.
def makeWavFile(message):
    phones = message.lower().split()
    output = wave.open("message.wav", 'wb')
    output.setnchannels(2)
    output.setframerate(44100)
    output.setsampwidth(2)
    lastPhone = 'q'
    count = 0
    for phone in phones:
        phonefile = wave.open("phones/" + phone + ".wav", 'rb')
        if lastPhone == 'q':
            nframes = phonefile.getnframes()
            frames = phonefile.readframes(int(nframes*.825))
            output.writeframes(frames)
        else:    
            nframes = phonefile.getnframes()
            phonefile.setpos(int(nframes/8))
            if count == len(phones) - 1 or phones[count+1] == 'q':
                frames = phonefile.readframes(int(nframes*.825))
                output.writeframes(frames)
            else:
                frames = phonefile.readframes(int(nframes*.75))
                output.writeframes(frames)
        lastPhone = phone
        count += 1
    print("Type 'afplay message.wav' to hear your message")



if __name__ == '__main__':
    main()