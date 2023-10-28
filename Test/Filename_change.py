import os

def edit_filenames(directory_path):
    d = {"C": 1, "C#": 2, "D": 3, "D#": 4, "E": 5, "F": 6, "F#": 7, "G": 8, "G#": 9, "A": 10, "A#": 11, "B": 12}


    for filename in os.listdir(directory_path):
        # Split the filename into the number and the rest of the name
        parts = filename.split("ff-0")[1]



        note_number = int(number)*12 + d[letter]
            
        # Create the new filename with the number first
        new_filename = f"{note_number}-{number}{letter}.wav"
        print(new_filename)
        # Rename the file
        #os.rename(os.path.join(directory_path, filename), os.path.join(directory_path, new_filename))

#edit_filenames("C:/Users/adamf/PycharmProjects/Visual Studio/Test/Violin")






d = {"C": 1, "C#": 2, "D": 3, "D#": 4, "E": 5, "F": 6, "F#": 7, "G": 8, "G#": 9, "A": 10, "A#": 11, "B": 12}


# assign a note to a number
# note number = note[0] + d[note[1:]]
# for note in directory "Violin" print note numer

def print_note_number(directory_path):
    note_n = {}
    for filename in os.listdir(directory_path):
        # Split the filename into the number and the rest of the name
        filename = filename.split("-")[1]
        parts = filename.split(".")
        name = parts[0]
        letter = name[1:]
        number = name[0]

        note_number = int(number)*12 + d[letter]

        note_n[note_number] = filename.replace(".wav", "")

    return note_n
        #print(f"number: {int(number)}, letter: {letter}, note number: {note_number}")

#note_dict = (print_note_number("C:/Users/adamf/PycharmProjects/Visual Studio/Test/Violin"))




def switch_dict_keys_values(d):
    return {v: k for k, v in d.items()}


order = {44: '3G', 45: '3G#', 46: '3A', 47: '3A#', 48: '3B',
 49: '4C', 50: '4C#', 51: '4D', 52: '4D#', 53: '4E', 54: '4F',
  56: '4G', 57: '4G#', 58: '4A', 59: '4A#', 60: '4B', 61: '5C', 62: '5C#',
   63: '5D', 64: '5D#', 65: '5E', 66: '5F', 67: '5F#', 68: '5G', 69: '5G#', 70: '5A', 71: '5A#', 72: '5B',
    73: '6C', 74: '6C#', 75: '6D', 76: '6D#', 77: '6E', 78: '6F', 79: '7F#', 80: '6G'}

print(switch_dict_keys_values(order))


d = {"C": 1, "C#": 2, "D": 3, "D#": 4, "E": 5, "F": 6, "F#": 7, "G": 8, "G#": 9, "A": 10, "A#": 11, "B": 12}

piano_dict = {}
for i in range(0, 9):
    for note in d:
        key_num = i*12 + d[note]
        if i == 0 and note == "A":
            piano_dict[f"{i}{note}"] = 0
        else:
            piano_dict[f"{i}{note}"] = key_num - 8

print(piano_dict)
# BEGIN: 8f7e4d3b9w3d
piano_dict = {
    1: "A0",
    2: "A#0",
    3: "B0",
    4: "C1",
    5: "C#1",
    6: "D1",
    7: "D#1",
    8: "E1",
    9: "F1",
    10: "F#1",
    11: "G1",
    12: "G#1",
    13: "A1",
    14: "A#1",
    15: "B1",
    16: "C2",
    17: "C#2",
    18: "D2",
    19: "D#2",
    20: "E2",
    21: "F2",
    22: "F#2",
    23: "G2",
    24: "G#2",
    25: "A2",
    26: "A#2",
    27: "B2",
    28: "C3",
    29: "C#3",
    30: "D3",
    31: "D#3",
    32: "E3",
    33: "F3",
    34: "F#3",
    35: "G3",
    36: "G#3",
    37: "A3",
    38: "A#3",
    39: "B3",
    40: "C4",
    41: "C#4",
    42: "D4",
    43: "D#4",
    44: "E4",
    45: "F4",
    46: "F#4",
    47: "G4",
    48: "G#4",
    49: "A4",
    50: "A#4",
    51: "B4",
    52: "C5",
    53: "C#5",
    54: "D5",
    55: "D#5",
    56: "E5",
    57: "F5",
    58: "F#5",
    59: "G5",
    60: "G#5",
    61: "A5",
    62: "A#5",
    63: "B5",
    64: "C6",
    65: "C#6",
    66: "D6",
    67: "D#6",
    68: "E6",
    69: "F6",
    70: "F#6",
    71: "G6",
    72: "G#6",
    73: "A6",
    74: "A#6",
    75: "B6",
    76: "C7",
    77: "C#7",
    78: "D7",
    79: "D#7",
    80: "E7",
    81: "F7",
    82: "F#7",
    83: "G7",
    84: "G#7",
    85: "A7",
    86: "A#7",
    87: "B7",
    88: "C8"
}

print(piano_dict)
# END: 8f7e4d3b9w3d

# for value in piano_dict get the number to the 

for key, value in piano_dict.items():
    
    note = value[:-1]
    octave = value[-1]

    print(octave + note)