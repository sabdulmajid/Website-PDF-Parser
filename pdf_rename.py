import os
from PyPDF2 import PdfReader
import re

# Define the directory where the PDF files are located
directory = r"C:\Users\shaik\OneDrive - University of Waterloo\UW SE\2A\CS241\Lecture Slides - Carmen Bruni"

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
        pdf_title = pdf_reader.getDocumentInfo().title.strip()

    # Sanitize the filename
    sanitized_title = sanitize_filename(pdf_title)

    # Construct the new filename
    new_filename = f"Lecture {sanitized_title}.pdf"
    new_filepath = os.path.join(directory, new_filename)

    # Rename the file
    os.rename(filepath, new_filepath)

    print(f"Renamed: {filename} -> {new_filename}")

print("All files renamed successfully!")
