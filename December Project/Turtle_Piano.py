# This code uses all the previous codes to make an interactive keyboard with the ability to
#  only play specific notes in a specific key if the user wants

# The code will play .wav files downloaded from the internet. The files are stored in a folder
#  called 'samples' and are named after their note and octave, e.g. the fifth A note is called "A5.wav"

import turtle
import random
import time

from Getting_Key_Binds import key_binds_dict
from Getting_correct_notes import Gettng_key
from Scales import scales_dict
from Frequency import srp_flt_dict

from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from pygame.mixer import Sound
import pygame
pygame.mixer.init(44100, -16,2,2048)


# These will be used later in my functions
stay_in_key = True
random_notes = False

# This prints out a list of scales to choose from by looping through the scales dictionary
for scale in range(len(scales_dict.keys())):
    print(str(scale),":", list(scales_dict.keys())[scale])

print("\n")

specified_scale = input("Please Select the key you want to play in from the list above (Enter the number), then press enter: ")
specified_key = input("Please select the root note, then press enter. (e.g. Ab, E, F#): ")

# This changes the users input into a string that can be used by the "Getting_key" function
specified_scale_txt = (list(scales_dict.keys())[int(specified_scale)])

# Using the Gettting_key function from Scales.py I get a list of notes in the specified scale and key
scale = Gettng_key(specified_key, specified_scale_txt)


print("The notes in", specified_key,specified_scale_txt,"key are: ", scale)
print("\n")



turtle.hideturtle()
turtle.setup(1000,1000)
turtle.title('Rounded Rectangle - PythonTurtle.Academy')
turtle.speed(0)
turtle.up()
turtle.hideturtle()


# These lines print out the basic instructions to the user on the turtle window
turtle.setpos(0,-320)
turtle.write("Make sure Caps Lock is on whilst playing",align="center", font=("Arial", 16, "normal"))
turtle.setpos(0,-350)
turtle.write("Press Space Bar to stop all notes playing",align="center", font=("Arial", 16, "normal"))
turtle.setpos(0,-380)
turtle.write("Press Return key play any note",align="center", font=("Arial", 16, "normal"))
turtle.setpos(0,-410)
turtle.write("Press Backspace key to add random notes in key instead of silence when wrong note is played",align="center", font=("Arial", 16, "normal"))
turtle.setpos(0,-440)
turtle.write("(If 'Play Any Note' is on, filler notes will not play)",align="center", font=("Arial", 16, "normal"))
turtle.setpos(0,-470)
turtle.write("Press Hash key ('#') to end session",align="center", font=("Arial", 16, "normal"))


# This function creates a rectangle with rounded edges, it also writes a letter at the bottom of
#  each rectangle and plays a specific note when the rectangle is drawn.
def round_rectangle(center_x,center_y,width,height,cornersize, color,letter,key_col):

    # This if statement clears up a channel so a new note can be played
    if pygame.mixer.find_channel() == None:
        pygame.mixer.Channel(0).stop()

    sound = Sound("./samples/" + key_binds_dict[letter] + ".wav")
    sound.play()

    turtle.up()
    turtle.bgcolor("LightSalmon4")
    #turtle.goto(center_x-width/2+cornersize,center_y-height/2)
    turtle.color(color)
    turtle.down()
    turtle.begin_fill()

    for _ in range(2):
        turtle.fd(width-2*cornersize)
        turtle.circle(cornersize,90)
        turtle.fd(height-2*cornersize)
        turtle.circle(cornersize,90)


    turtle.end_fill()

    time.sleep(0.1)

    turtle.pendown()
    turtle.color(key_col)
    turtle.write(" "+str(letter), font=("Arial", 16, "normal"))


# I will iterate through these lists and draw my keys. I use the letters instead of numbers so i can
#  write the letters on each key to make it easier for the user to know which note to play

# In the black keys list I use dashes to represent gaps in the keyboard, the code will not draw anything when it
#  reads a dash but it will still move forward
white_keys = list("QWERTYUIOXCVBNM,./")
black_keys = list("23-567-9S-FGH-KL-")

turtle.penup()
turtle.setpos(-480,-200)


# Draws the white keys
for i in white_keys:

    round_rectangle(0,0,50,300,10,"ivory",i,"Gray0")
    turtle.penup()
    turtle.forward(55)


# Moves the turtle up slightly for a better looking keyboard
turtle.penup()
turtle.setpos(-455,-105)

# Draws the black keys, lifting the pen and moving forward whenever it reads a "-"
for b in black_keys:

    if b == "-":
        turtle.penup()
        turtle.forward(55)
    else:
        round_rectangle(0, 0, 50, 205, 10, "Gray0",b,"ivory")

        turtle.penup()
        turtle.forward(55)



# This function plays whatever note is passed into it... Depending on a few things.

def play(note):
    # pygame.mixer can only handle 8 channels playing at a time. I have to explicitly ask the computer to empty the
    #  first channel if all 8 are full. If i dont do this then nothing would play until a channel has stopped playing
    if pygame.mixer.find_channel() == None:
        pygame.mixer.Channel(0).stop()


    # The user can change the value of both of these variables during the session

    if stay_in_key == True and random_notes == False:

        # The code will only play notes in the scale specified by the user. If the user presses a wrong key, no sound
        #  will play and the wrong note will be printed to the screen

        if "/" in key_binds_dict[note.upper()][:-1] or "#" in key_binds_dict[note.upper()][:-1]:
            note2 = srp_flt_dict[key_binds_dict[note.upper()][:-1]]
        else:
            note2 = key_binds_dict[note.upper()][:-1]

        if note2 in scale:
            # The key binds dictionary is used to find the specific note that the user wants to play
            sound = Sound("./samples/" + key_binds_dict[note.upper()] + ".wav")
            sound.play()
        else:
            print(note2, "not in scale")

    elif stay_in_key == True and random_notes == True:

        # The code will only play notes in the scale specified by the user but this time if a wrong key is pressed the
        #  code will play a random note in the correct scale. It will also print out the random key

        if "/" in key_binds_dict[note.upper()][:-1] or "#" in key_binds_dict[note.upper()][:-1]:
            note2 = srp_flt_dict[key_binds_dict[note.upper()][:-1]]
        else:
            note2 = key_binds_dict[note.upper()][:-1]

        if note2 in scale:
            # The key binds dictionary is used to find the specific note that the user wants to play
            sound = Sound("./samples/" + key_binds_dict[note.upper()] + ".wav")
            sound.play()
        else:
            filler_note = scale[random.randint(0,(len(scale)-1))]

            if "/" in filler_note:
                filler_note = filler_note.split("/")[0]

            octave = str(random.randint(4,6))
            print(filler_note+octave)
            # The key binds dictionary is used to find the specific note that the user wants to play




    else:

        # The code will play any note on the keyboard regardless of specified key.
        # The key binds dictionary is used to find the specific note that the user wants to play
        sound = Sound("./samples/" + key_binds_dict[note.upper()] + ".wav")
        sound.play()


# Making a function to draw a rectangle cleans up the code a lot
def rectangle(h,w, col):
    turtle.color(col)
    turtle.begin_fill()

    for i in range(2):
        turtle.forward(w)
        turtle.left(90)
        turtle.forward(h)
        turtle.left(90)

    turtle.end_fill()


# This function changes the "stay_in_key" variable from True to False or from False to True. It also tells the user
#  which mode they are currently in. The "stay_in_key" variable determines which notes can be played

def accidental():
    global stay_in_key

    if stay_in_key == True:
        stay_in_key = False


        # This box is used to cover over whatever was writen down before so the new text is readable
        turtle.setpos(-440, -300)
        rectangle(20,360, "LightSalmon4")


        turtle.color("white")
        turtle.setpos(-320, -300)
        turtle.write("Play Any Note: ON", align="center", font=("Arial", 16, "normal"))

    else:
        stay_in_key = True

        # This box is used to cover over whatever was writen down before so the new text is readable
        turtle.setpos(-440, -300)
        rectangle(20, 360, "LightSalmon4")

        turtle.color("white")
        turtle.setpos(-320, -300)
        turtle.write("Play Any Note: OFF", align="center", font=("Arial", 16, "normal"))

# This function is practically identical to the 'accidental' function, it changes the 'random_notes' variable's status
#  and shows the user what mode they are in. The random_notes variable determines weather random notes in the scale
#  will be played if the user presses a wrong key

def filler_notes():
    global random_notes

    if random_notes == True:
        random_notes = False

        turtle.setpos(-500, -340)
        rectangle(20, 300, "LightSalmon4")

        turtle.color("white")
        turtle.setpos(-320, -340)
        turtle.write("Filler Notes: OFF", align="center", font=("Arial", 16, "normal"))

    else:
        random_notes = True

        turtle.setpos(-500, -340)
        rectangle(20, 300, "LightSalmon4")

        turtle.color("white")
        turtle.setpos(-320, -340)
        turtle.write("Filler Notes: ON", align="center", font=("Arial", 16, "normal"))


# This function stops all sounds from playing, if all channels are full this is an easy way to empty them and play
#  several notes at once
def sustain_peddal():
    pygame.mixer.stop()

# This function terminates the turtle window
def end_session():
    turtle.bye()


# Here all the functions are assigned to a specific key
turtle.listen()
turtle.onkey(sustain_peddal, "space")
turtle.onkey(end_session, "#")
turtle.onkey(accidental, "Return")
turtle.onkey(filler_notes, "BackSpace")


# These for loops create a turtle.onkey() for each note on the keyboard. The
#  lambda part allows me to pass an argument to the play function

window = turtle.Screen()

for n in white_keys:
    window.onkeypress(lambda n=n: play(n), str(n))

for n in black_keys:

    # The dashes were used for the drawing of the keyboard but serve no other purpose. The if statement
    #  is used so no error occurs
    if n != "-":
        window.onkeypress(lambda n=n: play(n), str(n))


# Turtle.done() keeps the window open until the user closes it
turtle.done()
