# wavetest.py
# Noah Brackenbury
# CS 322, Fall 2015

import sys
import wave

def main():
    b = wave.open('b.wav', 'rb')
    ey = wave.open('ey.wav', 'rb')
    bae = wave.open('bae.wav', 'wb')
    bae.setnchannels(2)
    bae.setframerate(44100)
    bae.setsampwidth(2)
    nbframes = b.getnframes()
    neyframes = ey.getnframes()
    bframes = b.readframes(int(nbframes*.75))
    bae.writeframes(bframes)
    bframe = []
    eyframe = []
    frames = []
    for i in range(0, int(nbframes*.25)):
        bframe.append(b.readframes(1))
        bframe[i] = int.from_bytes(bframe[i], byteorder='big')
        eyframe.append(ey.readframes(1))
        eyframe[i] = int.from_bytes(eyframe[i], byteorder='big')
        frames.append(bframe[i]+eyframe[i])
        bae.writeframes(frames[i].to_bytes((frames[i].bit_length() // 8) + 1, byteorder='big'))
    eyframes = ey.readframes(neyframes - int(nbframes*.25))
    bae.writeframes(eyframes)
    
        
    
if __name__ == '__main__':
    main()