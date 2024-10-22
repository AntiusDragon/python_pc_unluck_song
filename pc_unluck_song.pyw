import pygame
import time

# Inicializuojame pygame
pygame.init()

# Nustatome garsą
pygame.mixer.music.load('C:\\Users\\AURUS\\Documents\\python_pc_unluck_song\\unluck_song.wav')  # Pakeiskite su savo dainos failo keliu
pygame.mixer.music.play()

# Groti dainą 17 sekundžių
time.sleep(17)

# Sustabdyti muziką
pygame.mixer.music.stop()
