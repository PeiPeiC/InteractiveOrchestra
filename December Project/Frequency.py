# This code converts an excel sheet into a dictionary containing each note and the
#  list of the corresponding frequencies for each of those notes

import pandas as pd

# This table of notes and their frequencies was found online and converted into an
#  excel sheet

df = pd.DataFrame(pd.read_excel("./frequencies_LOW_A.xlsx"))

# This dataframe was very messy and contained empty spaces so I will create a new dataframe
#  which will be easier to work with


df_all = pd.DataFrame({"Note":[], "Frequency (Hz)":[]})

notes_lst = []
freq_lst = []


# This loop appends each note into a list and each frequency into a list
for note in range(99):

    if "/" in df.loc[note,"Note"]:
        # The notes with a "/" in it all happened to have a blank space at the end of
        #  them for some reason

        # Here I am cleaning up each note in the "Note" column by getting rid of the
        #  empty space and the first octave number
        note1 = df.loc[note,"Note"].split("/")[0][1:-1]
        note2 = df.loc[note,"Note"].split("/")[1][:-1]

        note3 = note1+"/"+note2
        # Note3 is the tidied up version of the origonal note


        freq = df.loc[note,"Frequency (Hz)"]


        notes_lst.append(note3)
        freq_lst.append(freq)

    else:

        # The rest of the notes were already okay and ready to be added to the list
        freq = df.loc[note, "Frequency (Hz)"]
        note_own = df.loc[note, "Note"]

        notes_lst.append(note_own)
        freq_lst.append(freq)


# Here is the new dataframe which is much easier to work with
df_of_notes = pd.DataFrame({"Note":notes_lst, "Frequency (Hz)":freq_lst})


all_notes_and_freqs = {}

# This loop is creating a dictionary of empty lists assigned to the 12 different notes
for i in range(12):
    all_notes_and_freqs[df_of_notes.loc[i, "Note"][:-1]] = []


# This loop assigns the 12 different notes with all their corresponding frequencies

# Even though the loop iterates 99 times, there will only be 12 keys in 'dic' because
#  df_of_notes.loc[i,"Note"][:-1] does not include the octave number. This means that,
#  for example, the frequency corresponding to "C1" and "C5" will be appended to the
#  same list since ("C1")[:-1] = "C" and ("C5")[:-1] = "C"

for i in range(99):
    all_notes_and_freqs[df_of_notes.loc[i,"Note"][:-1]].append(df_of_notes.loc[i,"Frequency (Hz)"])


# These hard codded dictionaries will be used in other codes since, for example, "Bb" is now stored as "A#/Bb".
# So if a user wants to play in the key of "Bb" they don't have to type "A#/Bb"

srp_flt_dict = {"C#":"C#/Db","Db":"C#/Db","D#":"D#/Eb","Eb":"D#/Eb","F#":"F#/Gb", "Gb":"F#/Gb","G#":"G#/Ab","Ab":"G#/Ab","A#":"A#/Bb","Bb":"A#/Bb"}

srp_flt_dict1 = {"C#":"C#/Db","D#":"D#/Eb","F#":"F#/Gb","G#":"G#/Ab","A#":"A#/Bb"}

srp_flt_dict_rvs = {v: k for k, v in srp_flt_dict1.items()}
