import os
import pygame

def play_violin_sound1(filename, instrument):
    # Initialize Pygame mixer
    pygame.mixer.init()

    # Get the path to the "violin" directory
    violin_dir = os.path.join(os.path.dirname(__file__), instrument)

    # Get the path to the sound file
    sound_file = os.path.join(violin_dir, filename)

    # Load the sound file
    sound = pygame.mixer.Sound(sound_file)

    # Play the sound file
    sound.play()

    # Wait for the sound to finish playing
    pygame.time.wait(int(sound.get_length() * 500))

    # Clean up Pygame mixer
    pygame.mixer.quit()

#play_violin_sound1("40-4C.wav", "Violin")



