import os
import re

pdf_directory = r'path\to\pdf\files'
output_file = 'lectures_arranged3.txt'

# Get the list of PDF files in the directory
pdf_files = [file for file in os.listdir(pdf_directory) if file.lower().endswith('.pdf')]

# Extract lecture names from the file names using regular expressions
lecture_names = []
for pdf_file in pdf_files:
    match = re.search(r'Lecture \d+ - (.+)\.pdf', pdf_file)
    if match:
        lecture_name = match.group(1)
        lecture_names.append(lecture_name)

# Sort the list of lecture names
sorted_names = sorted(lecture_names)

# Append sorted lecture names to the output file
with open(output_file, 'w') as file:
    for lecture_name in sorted_names:
        file.write(lecture_name + '\n')

print("Lecture names sorted and appended successfully.")
