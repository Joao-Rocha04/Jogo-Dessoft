import pygame
from config import SND
import os

class SOM:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {}
        self.load_sounds()

    def load_sounds(self):
        self.sounds['adaga'] = pygame.mixer.Sound(os.path.join(SND, 'dagger_drawn2-89025.mp3'))
        self.sounds['especial'] = pygame.mixer.Sound(os.path.join(SND, '632336__igroglaz__magic-spell-06.wav'))
        self.sounds['entrada'] = pygame.mixer.Sound(os.path.join(SND, 'field_theme_1.wav'))
        self.sounds['game_over'] = pygame.mixer.Sound(os.path.join(SND, 'Game_Over_2.wav'))
        self.sounds['corrida'] = pygame.mixer.Sound(os.path.join(SND, 'Running Footsteps - Sound Effect.mp3'))

    def play_sound(self, sound_name, volume=1.0, loops=0):
        if sound_name in self.sounds:
            self.sounds[sound_name].set_volume(volume)
            self.sounds[sound_name].play(loops=loops)

    def stop_sound(self, sound_name):
        if sound_name in self.sounds:
            self.sounds[sound_name].stop()