import os

def rename_files(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(".wav"):
            note = filename.split("-")[6].split(".")[0]
            if "sharp" in note:
                note = note.replace("sharp", "") + "#"
            if note[0].isalpha():
                note = note[1:] + note[0]
            new_filename = note.upper() + ".wav"
            print(new_filename)
            break
            output_file_path = os.path.join(output_dir, new_filename)
            if not os.path.exists(output_file_path):
                os.rename(os.path.join(input_dir, filename), output_file_path)

# Example usage
rename_files("C:/Users/adamf/PycharmProjects/Visual Studio/Test/Violin", "C:/Users/adamf/PycharmProjects/Visual Studio/Test/Violin")
