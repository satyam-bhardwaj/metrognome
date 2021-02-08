#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 17:52:44 2021

@author: chaos
"""

import numpy as np
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt
import sounddevice as snd

bpm = 200
interval = 60/bpm

samplerate, primary_click = wavfile.read('primary.wav')
primary_click = primary_click[:,0]
secondary_click = wavfile.read('secondary.wav')[1]
secondary_click = secondary_click[:,0]

time_sig = [4,4]
N_measure = int(4*samplerate*interval*(time_sig[0]/time_sig[1]))
N_beat = int(N_measure/time_sig[0])
measure = np.zeros(N_measure)

measure[:primary_click.size] = primary_click
for i in range(1,time_sig[0]):
    measure[i*N_beat:i*N_beat+secondary_click.size] = secondary_click

measure = measure/np.max(measure)
metro = np.tile(measure, 64)
# main loop
snd.play(metro)
snd.wait()
