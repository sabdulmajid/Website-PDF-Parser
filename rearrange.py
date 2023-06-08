import os
import re

pdf_directory = r'path\to\pdf\files'
output_file = 'lectures_arranged2.txt'

# Get the list of PDF files in the directory
pdf_files = [file for file in os.listdir(pdf_directory) if file.lower().endswith('.pdf')]

# Extract lecture numbers from the file names using regular expressions
lecture_numbers = []
for pdf_file in pdf_files:
    match = re.search(r'Lecture (\d+)', pdf_file)
    if match:
        lecture_number = int(match.group(1))
        lecture_numbers.append((pdf_file, lecture_number))

# Sort the list of files based on lecture numbers
sorted_files = sorted(lecture_numbers, key=lambda x: x[1])

# Append sorted PDF file names (without extension) to the output file
with open(output_file, 'w') as file:
    for pdf_file, _ in sorted_files:
        file.write(os.path.splitext(pdf_file)[0] + '\n')

print("File names sorted and appended successfully.")
