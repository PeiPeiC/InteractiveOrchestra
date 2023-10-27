# This code returns all of the notes in a user specified scale in a user specified key

from Frequency import *
from Scales import *


# In this function I use a formula which returns the frequency of a note which is 'n' notes away
#  from another note
# I use this formula as well as the scales_dict to work out which frequencies are in a certain scale
#  in a certain key.
# When I know these frequencies I can compare them to the dictionary of notes and their frequencies to
#  deduce which notes are in the scale

def Gettng_key(key, scale):
    allowed_freqs = []

    # If the user wants to get a scale in the key of a sharp or flat note, the user
    #  will type, for example, "Eb". Since there is no dictionary key "Eb" I will need
    #  to convert "Eb" into "D#/Eb" so the computer can find it in the 'all_notes_and_freqs' dictionary

    if "#" in key and not "/" in key or "b" in key and not "/" in key:
        key = srp_flt_dict[key]


    start_freq = all_notes_and_freqs[key][0]
    chosen_scale = scales_dict[scale]


    # This loop uses the formula to find all the frequencies in the scale
    for x in range(len(chosen_scale)):

        # I use the 'steps' dictionary to convert the letter to a number which can be used in the formula
        N = (steps[chosen_scale[x]])

        start_freq = start_freq * (2**(N/12))


        allowed_freqs.append(round(start_freq))


    # The 'notes_in_scale' list will be filled with the notes in the scale. e.g. [A#, B, C, ...]
    notes_in_scale = []


    for allowed_note in all_notes_and_freqs:

    # This loop iterates through every note in the 'all_notes_and_freqs' dictionary

        if round(all_notes_and_freqs[allowed_note][0]) in (allowed_freqs)\
                or round(all_notes_and_freqs[allowed_note][1]) in (allowed_freqs):

        # If a frequency in the 'all_notes_and_freqs' dictionary matches the a frequency in the 'allowed_freqs' list
        #  then that means that the note is in the scale so it's appended to the list

            notes_in_scale.append(allowed_note)


    # To make it look nicer I put the list of notes in order, starting with the root note

    # I double the length of the list then started the list from the root note
    notes_in_scale_ord = (notes_in_scale*2)
    notes_in_scale_ord = notes_in_scale_ord[(notes_in_scale.index(key)):(notes_in_scale.index(key))+len(chosen_scale)-1]


    return notes_in_scale_ord

#print(Gettng_key("B", "Major"))