import os
from PyPDF2 import PdfReader
import re

# Define the directory where the PDF files are located
directory = r"C:\Users\shaik\OneDrive - University of Waterloo\UW SE\2B\CS348\Lecture Slides"

# Function to sanitize the filename
def sanitize_filename(filename):
    # Replace disallowed characters with underscores
    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    return filename

# Iterate over the PDF files in the directory
for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    if not filename.endswith('.pdf'):
        continue

    # Extract the PDF title from the metadata
    with open(filepath, 'rb') as file:
        pdf_reader = PdfReader(file)
        pdf_metadata = pdf_reader.metadata
        pdf_title = pdf_metadata.get('/Title', '').strip()

    # Sanitize the title
    sanitized_title = sanitize_filename(pdf_title)

    # Construct the new filename
    new_filename = f"{sanitized_title}.pdf"
    new_filepath = os.path.join(directory, new_filename)

    # Rename the file only if the new filename is different
    if filename != new_filename:
        os.rename(filepath, new_filepath)
        print(f"Renamed: {filename} -> {new_filename}")
    else:
        print(f"Skipping: {filename}")

print("All files renamed successfully!")
