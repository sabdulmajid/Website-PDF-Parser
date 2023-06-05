import os

# Define the directory where the PDF files are located
directory = r"C:\Users\shaik\OneDrive - University of Waterloo\UW SE\2A\CS241\Lecture Slides - Carmen Bruni"

# Function to sanitize the filename
def sanitize_filename(filename):
    # Replace disallowed characters with underscores
    filename = filename.replace(':', '').replace('?', '').replace('*', '').replace('<', '').replace('>', '').replace('|', '').replace('"', '')
    return filename

# Iterate over the PDF files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.pdf'):
        # Remove unwanted parts from the filename
        new_filename = filename.replace('Lecture CS 241 ', '').replace('  With thanks to Brad Lushman, Troy Vasiga and Kevin Lanctot', '')

        # Sanitize the filename
        sanitized_filename = sanitize_filename(new_filename)

        # Construct the new filepath
        old_filepath = os.path.join(directory, filename)
        new_filepath = os.path.join(directory, sanitized_filename)

        # Rename the file
        os.rename(old_filepath, new_filepath)

        print(f"Renamed: {filename} -> {sanitized_filename}")

print("All files renamed successfully!")
