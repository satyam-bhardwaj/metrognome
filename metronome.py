#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 17:52:44 2021

@author: chaos
"""

import numpy as np
import matplotlib.pyplot as plt
import sounddevice as snd

bpm = 120
interval = 60/bpm
samplerate = 44100
duration = 100*10**(-3) #ms
time_axis = np.linspace(0,duration,int(duration*samplerate))

# gets rid of extremal transients
width = 0.007
square_wave = np.zeros_like(time_axis)
square_wave[int((duration/2-width)*samplerate):int((duration/2+width)*samplerate)]=1

# attack
left_edge = np.sin(np.pi*(time_axis+width)/duration)**20
left_edge[int((duration/2-width)*samplerate):]=0

# release
right_edge = np.sin(np.pi*(time_axis-width)/duration)**100
right_edge[:int((duration/2+width)*samplerate)]=0

volume_envelope = square_wave + left_edge + right_edge
plt.plot(volume_envelope)
plt.show()

primary_frequency = 880
primary_click = np.sin(2*np.pi*primary_frequency*time_axis)*volume_envelope

secondary_frequency = 440
secondary_click = np.sin(2*np.pi*secondary_frequency*time_axis)*volume_envelope

while True:
    snd.play(primary_click)
    for i in range(4):
        plt.pause(interval)
        snd.play(secondary_click)
