import pygame

def bg_music():
    pygame.mixer.music.load("sound/Guns N' Roses - Paradise City [8-bit].mp3")
    pygame.mixer.music.play(-1)