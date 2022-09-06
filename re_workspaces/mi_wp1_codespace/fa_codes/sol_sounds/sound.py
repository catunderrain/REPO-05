# reference resources
# https://pages.mtu.edu/~suits/notefreqs.html

#--------------------------------------------------------------------
import numpy
import os
import scipy
import sys
sys.path.append(os.path.abspath('D:\\do\\re_workspaces\\mi_wp1_codespace\\fa_codes\\sol_sounds\\'))
from data import *

#-----------------------------------------------------------------------------------------------------
samplerate = 44100
tempo = 140

#-----------------------------------------------------------------------------------------------------
def freqofnote(note):
    if note == 'xx':
        notefreq = 0
    else:
        frequency = 16.35
        notedir = {}
        notealpha = ['c', 'C', 'd', 'D', 'e', 'f', 'F', 'g', 'G', 'a', 'A', 'b']
        notenum = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
        for num in notenum:
            for alpha in notealpha:
                notedir[alpha + num] = frequency
                frequency *= pow(2, 1/12)
        notefreq = notedir[note]
    return notefreq


#-----------------------------------------------------------------------------------------------------
def wave(note, type = 0, wavetempo = tempo): # measuring unit is second
    frequency = freqofnote(note)
    amplitude = 4096
    duration = 60/wavetempo
    time = numpy.linspace(0, duration, int(samplerate * duration))
    ampoftime = amplitude * numpy.sin(2 * numpy.pi * frequency * time)
    if type == 0:
        for i in range(int(3 * len(time)/4), len(time)):
            ampoftime[i] = 0
    elif type == 1:
        pass
    return ampoftime


#-----------------------------------------------------------------------------------------------------
# subdef
def multidata(data, n):
    datafixed = []
    for i in range(n):
        datafixed.append(data)
    return numpy.concatenate(datafixed)


#-----------------------------------------------------------------------------------------------------
def melody(string, type = 0):
    list = string.split(',')
    data = []
    for note in list:
        data.append(wave(note, type))
    return numpy.concatenate(data)


#-----------------------------------------------------------------------------------------------------
def chorddata(chord, type = 1):
    if type == 0: # 44100 * 60/tempo /4 = 661500/tempo = 2^2 * 3^3 * 5^3 * 7^2: 60, 90, 100, 140
        data = []
        for note in chord:
            data.append(wave(f'{note}', 1, 4*tempo))
        data = numpy.concatenate(data)
    elif type == 1:
        data = freqofnote('xx')
        for note in chord:
            data += wave(f'{note}', 1)
    elif type == 2:
        data = []
        data.append(wave(f'{chord[0]}', 1, 4*tempo))
        data.append(wave(f'{chord[2]}', 1, 4*tempo))
        data.append(wave(f'{chord[1]}', 1, 4*tempo))
        data.append(wave(f'{chord[3]}', 1, 4*tempo))
        data = numpy.concatenate(data)
    return data


#-----------------------------------------------------------------------------------------------------
def chordsmel(string, type = 1):
    list = string.split(',')
    data = []
    for chord in list:
        data.append(chorddata(chords[chord], type))
    return numpy.concatenate(data)


#-----------------------------------------------------------------------------------------------------
def fileout(data):
    data = data * 16300/numpy.max(data)
    try:
        os.remove('sound.wav')
    except:
        print('Nothing to remove.')
    scipy.io.wavfile.write('D:\\do\\re_workspaces\\mi_wp1_codespace\\fa_codes\\sol_sounds\\sound.wav', 44100, data.astype(numpy.int16))
    print('Done.')


#-----------------------------------------------------------------------------------------------------
# workspace 
