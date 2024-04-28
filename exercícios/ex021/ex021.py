import pygame
print(f'Tocando música Aladin (7mz)')
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input('Pressione enter para parar...')
