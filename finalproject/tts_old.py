# tts.py
# Noah Brackenbury and Alex Mathson
# CS 322, Fall 2015
# This program produces a .wav file with speech of the given text

import sys
import wave
import pickle

def main():
    dickt = pickle.load(open('cmudict.dat', 'rb'))
    message = sys.argv[1].lower()
    phones = message.split()
    output = wave.open("message.wav", 'wb')
    output.setnchannels(2)
    output.setframerate(44100)
    output.setsampwidth(2)
    lastPhone = 'q'
    count = 0
    for phone in phones:
        phonefile = wave.open(phone + ".wav", 'rb')
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