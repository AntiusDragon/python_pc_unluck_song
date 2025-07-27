import pygame
import time

# Inicializuojame pygame
pygame.init()

# Nustatome garsą
# pygame.mixer.music.load('C:\\Users\\AURUS\\Documents\\python_pc_unluck_song\\unluck_song.wav')  # Pakeiskite su savo dainos failo keliu

# Gaunam pilną kelią iki .wav failo (turi būti tame pačiame aplanke kaip .pyw)
wav_path = os.path.join(os.path.dirname(__file__), 'unluck_song.wav')
pygame.mixer.music.load(wav_path)

# Įkeliam ir paleidžiam muziką
pygame.mixer.music.play()

# Groti dainą 17 sekundžių
time.sleep(17)

# Sustabdyti muziką
pygame.mixer.music.stop()
