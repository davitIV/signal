import pygame

pygame.mixer.init()

sound_file = 'static/audio/son.mp3'

pygame.mixer.music.load(sound_file)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
