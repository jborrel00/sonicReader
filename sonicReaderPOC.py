import os
os.chdir('../../PySynth') #change to directory where I can use pysynth
import pygame #for playing back stuff when wanted
import pysynth
pygame.mixer.init()

"""
test = ( ('c', 4), ('e', 4), ('g', 4), ('c5', 1) )
test2 = ( ('c', 4), ('eb', 4), ('g', 4), ('c5', 1) )
pysynth.make_wav(test, fn = "test.wav")
pysynth.make_wav(test2, fn = "test2.wav")

pygame.mixer.music.load('test.wav')
pygame.mixer.music.play()
pygame.mixer.music.load('test2.wav')
pygame.mixer.music.play()
"""
musicWord = raw_input("make a word into music: ")
musicWordASCII = map(ord,musicWord) #makes the word ASCII
#print musicWordASCII #debugging
mwal = len(musicWordASCII)
#print mwal #debugging
wordSong = [] #array to hold musical values of each ascii character
for x in range(0,mwal):
	#print musicWordASCII[x] #debugging
	notatedWord =  musicWordASCII[x] % 7
	print notatedWord #debugging
	if notatedWord==1:
		wordSong.append('a')
	elif notatedWord==2:
		wordSong.append('b')
	elif notatedWord==3:
		wordSong.append('c')
	elif notatedWord==4:
		wordSong.append('d')
	elif notatedWord==5:
		wordSong.append('e')
	elif notatedWord==6:
		wordSong.append('f')
	else:
		wordSong.append('g')
print wordSong #debugging
#pysynth.make_wav(wordSong, fn = "wordSong.wav")
#pygame.mixer.music.load('wordSong.wav')
#pygame.mixer.music.play()
"""
this might come up:
string to ascii--> map(ord,"string")
"""
