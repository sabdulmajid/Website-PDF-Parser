import os

pdf_directory = r'path/to/pdf/files'
output_file = 'lectures.txt'

# Get the list of PDF files in the directory
pdf_files = [file for file in os.listdir(pdf_directory) if file.lower().endswith('.pdf')]

# Append PDF file names to the output file
with open(output_file, 'a') as file:
    for pdf_file in pdf_files:
        file.write(pdf_file + '\n')

print("File names appended successfully.")
