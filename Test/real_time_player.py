import os

# create dictionary with keys from a to z
violin_dict = {chr(i): None for i in range(ord('a'), ord('z')+1)}

# get all files in the Violin directory
violin_dir = "Violin"
violin_files = os.listdir(violin_dir)

# loop through each file and add to dictionary based on note
for file in violin_files:
    # get the note from the filename
    note = file.split(".")[0].lower()
    # check for # in filename
    if "#" in note:
        # get the letter and number separately
        letter = note[0]
        number = int(note[1])
        # check if the current note is lower than the current value in the dictionary
        if violin_dict[letter] is None or (number + 0.5) < int(violin_dict[letter][1]):
            violin_dict[letter] = (note.upper(), number + 0.5)
    else:
        # get the letter and number separately
        letter = note[0]
        number = int(note[1])
        # check if the current note is lower than the current value in the dictionary
        if violin_dict[letter] is None or number < int(violin_dict[letter][1]):
            violin_dict[letter] = (note.upper(), number)

print(violin_dict)
