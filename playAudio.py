# this is a script to play the mp3 file
# working perfectly fine

import pygame

def play_music(file_path):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

# Example usage
# file_path = "C:\\Users\\ammad\\Documents\\Ebad\\Codes\\Major_Project\\wake_up.mp3"
file_path = "wake_up.mp3"
play_music(file_path)

# Add a delay so the program doesn't exit immediately
pygame.time.wait(5000)  # Adjust the time as needed
