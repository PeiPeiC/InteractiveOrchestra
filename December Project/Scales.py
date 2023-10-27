# This code creates a dictionary of different scales and their corresponding intervals


# "Scales_steps" was found online and contains the intervals between notes
#  in various different scales
text = open("Scale_steps.txt")

# Creating an empty dictionary to fill in the for loop
scales_dict = {}

line = text.readline()[:-1]

# This while loop fills the 'scales_dict' dictionary with each line of the 'scales_steps' file
while line != "":

    row = line.split(": ")

    scales_dict[row[0]] = row[1].split(", ")

    line = text.readline()[:-1]


# This dictionary is used for other code, "W" stands for Whole step which is
#  a movement of 2 notes on the keyboard so it is given value of 2.

steps = {"W":2, "H":1, "1 1/2":3, "R":0}