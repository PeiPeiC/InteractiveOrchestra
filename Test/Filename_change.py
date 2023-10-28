import os

number_to_note =  {1: '0A', 2: '0A#', 3: '0B', 4: '1C',
 5: '1C#', 6: '1D', 7: '1D#', 8: '1E', 9: '1F', 10: '1F#', 11: '1G', 12: '1G#', 13: '1A', 14: '1A#', 15: '1B', 16: '2C',
 17: '2C#', 18: '2D', 19: '2D#', 20: '2E', 21: '2F', 22: '2F#', 23: '2G', 24: '2G#', 25: '2A', 26: '2A#', 27: '2B', 28: '3C',
  29: '3C#', 30: '3D', 31: '3D#', 32: '3E', 33: '3F', 34: '3F#', 35: '3G', 36: '3G#', 37: '3A', 38: '3A#', 39: '3B', 40: '4C',
   41: '4C#', 42: '4D', 43: '4D#', 44: '4E', 45: '4F', 46: '4F#', 47: '4G', 48: '4G#', 49: '4A', 50: '4A#', 51: '4B', 52: '5C',
    53: '5C#', 54: '5D', 55: '5D#', 56: '5E', 57: '5F', 58: '5F#', 59: '5G', 60: '5G#', 61: '5A', 62: '5A#', 63: '5B', 64: '6C',
     65: '6C#', 66: '6D', 67: '6D#', 68: '6E', 69: '6F', 70: '6F#', 71: '6G', 72: '6G#', 73: '6A', 74: '6A#', 75: '6B', 76: '7C',
      77: '7C#', 78: '7D', 79: '7D#', 80: '7E', 81: '7F', 82: '7F#', 83: '7G', 84: '7G#', 85: '7A', 86: '7A#', 87: '7B', 88: '8C'}

note_to_number = {'0A': 1, '0A#': 2, '0B': 3, '1C': 4,
 '1C#': 5, '1D': 6, '1D#': 7, '1E': 8, '1F': 9, '1F#': 10, '1G': 11, '1G#': 12, '1A': 13, '1A#': 14, '1B': 15,
  '2C': 16, '2C#': 17, '2D': 18, '2D#': 19, '2E': 20, '2F': 21, '2F#': 22, '2G': 23, '2G#': 24, '2A': 25, '2A#': 26, '2B': 27,
   '3C': 28, '3C#': 29, '3D': 30, '3D#': 31, '3E': 32, '3F': 33, '3F#': 34, '3G': 35, '3G#': 36, '3A': 37, '3A#': 38, '3B': 39,
    '4C': 40, '4C#': 41, '4D': 42, '4D#': 43, '4E': 44, '4F': 45, '4F#': 46, '4G': 47, '4G#': 48, '4A': 49, '4A#': 50, '4B': 51,
     '5C': 52, '5C#': 53, '5D': 54, '5D#': 55, '5E': 56, '5F': 57, '5F#': 58, '5G': 59, '5G#': 60, '5A': 61, '5A#': 62, '5B': 63,
      '6C': 64, '6C#': 65, '6D': 66, '6D#': 67, '6E': 68, '6F': 69, '6F#': 70, '6G': 71, '6G#': 72, '6A': 73, '6A#': 74, '6B': 75,
      '7C': 76, '7C#': 77, '7D': 78, '7D#': 79, '7E': 80, '7F': 81, '7F#': 82, '7G': 83, '7G#': 84, '7A': 85, '7A#': 86, '7B': 87, '8C': 88}





def edit_filenames(directory_path):

    for filename in os.listdir(directory_path):
        # Split the filename into the number and the rest of the name
        num = filename.split("-")[1].split(".")[0]

        print(num)

        new_filename = str(note_to_number[num]) + "-" + num + ".wav"

        print(new_filename)

        # Rename the file
        os.rename(os.path.join(directory_path, filename), os.path.join(directory_path, new_filename))

edit_filenames(r"C:\Users\adamf\PycharmProjects\Visual Studio\IO project\InteractiveOrchestra\Test\Violin")






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
