#wavereader.py
#Noah Brackenbury
#CS 322, Fall 2015
#This program produces an image of the contributing frequencies of a wav file

import sys
import wave
import math
import numpy


def main():
    wavFile = sys.argv[1]
    waveRead = wave.open(wavFile, 'rb')
    for j in range(int(waveRead.getnframes() / 160)):
        waveRead.setpos(j * 160)
        answers = getAnswers(waveRead)
        print(answers)
        
    
def getAnswers(waveReading):
    waveList = []
    for i in range(400):
        waveList.append(waveReading.readframes(1))
        if int.from_bytes(waveList[i], byteorder='little') >= 10:
            waveList[i] = int.from_bytes(waveList[i], byteorder='little', signed=True)
        else:
            waveList[i] = int.from_bytes(waveList[i], byteorder='little')
    waveArray = numpy.array(waveList)
    fourier = numpy.fft.fft(waveArray)
    answers = []
    for k in range(200):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
        real = fourier.real.tolist()[k] ** 2
        imag = fourier.imag.tolist()[k] ** 2
        answer = math.sqrt(real + imag)
        if answer != 0:
            answer = 10 * math.log(answer)
        answers.append(answer)

    return answers
    

if __name__ == '__main__':
    main()