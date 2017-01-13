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
    phones = re.sub('[0-9]', '', phones)
    print(phones)
    makeWavFile(phones)
    
def getPhones(word):
    if word in pronunciationDict:
        arpabet = pronunciationDict[word]
    else:
        print(word + ' not in pronunciation dictionary')
        arpabet = ' q q q '
    arpabet += ' q '
    return arpabet
    
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