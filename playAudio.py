# this is a script to play the mp3 file
# working perfectly fine

import pygame

def play_music(file_path):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

i = 0
while(True):
    if(i%2 == 0):
        file_path = "loud_alarm.mp3"
        play_music(file_path)
    i += 1
    # Add a delay so the program doesn't exit immediately
    pygame.time.wait(5000)  # Adjust the time as needed
