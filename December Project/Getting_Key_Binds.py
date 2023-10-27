# This code creates a key bind for every note on my turtle piano

from Getting_correct_notes import *

#This scale contains every note on the keyboard so it is used.
scale = Gettng_key("C", "Chromatic (Free Play)")

piano_note = []
x=0
n=0

# This loop creates a list of every note on a keyboard from octave 4-6. e.g. [C4, C#/Db4, ..., B6]
for i in range(3*len(scale)):

    piano_note.append(str(scale[x]+str(n+4)))

    x+=1

    if x == len(scale):
        x=0
        n+=1


# Looking at my keyboard drawn by the turtle I saw that the highest note was the F6 which is located
#  at piano_note[-7]. So the notes on my keyboard go from C4-F6 (piano_note[:-6]
my_turtle_piano = piano_note[:-6]


# These key binds were chosen by me since they seem to make the most sense to me.
# The dashes represent the empty space between the black keys
white_keys = list("QWERTYUIOXCVBNM,./")
black_keys = list("23-567-9S-FGH-KL-")

count_white = 0
count_black = 0

# I will fill this dictionary up with the keybinds. e.g. {"Q": "C4", "2": "C#4", ..., "/": "F6"}
key_binds_dict = {}


for key in my_turtle_piano:

    if "/" in key:
    # If the note has a "/" in it, I know its a sharp or a flat, therefrore it should be binded to a black key

        if black_keys[count_black] == "-":
            count_black +=1
            # If the item in list is a dash then it means it doesnt need a key bind so I just add to the count
            #  in order to skip it

        letter_on_keyboard = black_keys[count_black]

        # Since the sharp and flat notes are stored like "A#/Bb" in the "my_turtle_piano" list, but the sound files
        #  are named after just the sharp, e.g. A#. I will use my dictionary to convert the notes into their different
        #  form. Then I add it to the dictionary including the octave number at the end
        key_binds_dict[letter_on_keyboard] = srp_flt_dict_rvs[key[:-1]]+str(key[-1])
        count_black += 1

    else:
        letter_on_keyboard = white_keys[count_white]
        key_binds_dict[letter_on_keyboard] = key

        count_white += 1

