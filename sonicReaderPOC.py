import os
os.chdir('./PySynth') #change to directory where I can use pysynth
import pygame #for playing back stuff when wanted
import pysynth
pygame.mixer.init()

test = ( ('c', 4), ('e', 4), ('g', 4), ('c5', 1) )
test2 = ( ('c', 4), ('eb', 4), ('g', 4), ('c5', 1) )
pysynth.make_wav(test, fn = "test.wav")
pysynth.make_wav(test2, fn = "test2.wav")

pygame.mixer.music.load('test.wav')
pygame.mixer.music.play()
pygame.mixer.music.load('test2.wav')
pygame.mixer.music.play()
