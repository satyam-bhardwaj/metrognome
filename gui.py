#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 01:06:01 2021

@author: chaos
"""
from gi import require_version
require_version('Gtk', '3.0')
from gi.repository import Gtk

import numpy as np
import scipy.io.wavfile as wavfile
import sounddevice as snd

class MainWindow(Gtk.Window):
    def __init__(self): # constructor
        Gtk.Window.__init__(self, title="Metronome")
        
        # Box
        self.box = Gtk.Box(spacing=100)
        self.add(self.box)
        
        # Yes button
        self.play_button = Gtk.Button(label="Play")
        self.play_button.connect("clicked", self.play)
        self.box.pack_start(self.play_button, True, True, 0)     
        
        # No button
        self.stop_button = Gtk.Button(label="Stop")
        self.stop_button.connect("clicked", self.stop)
        self.box.pack_start(self.stop_button, True, True, 0)     
        
    def play(self, widget):        
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
        snd.play(metro)
        
    def stop(self, widget):
        snd.stop()
        
window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()