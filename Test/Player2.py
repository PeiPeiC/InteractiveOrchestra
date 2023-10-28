import os
import playsound

def play_violin_sound(filename, instrument):

    # Get the path to the "violin" directory
    violin_dir = os.path.join(os.path.dirname(__file__), instrument)

    # Get the path to the sound file
    sound_file = os.path.join(violin_dir, filename)

    print(sound_file)

    # Play the sound file
    playsound.playsound(sound_file)

play_violin_sound("40-4C.wav", "Violin")

