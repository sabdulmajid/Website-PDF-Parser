import urllib.request
from bs4 import BeautifulSoup
import os
import re

# Define the URL of the website
url = "https://cs.uwaterloo.ca/~cbruni/CS241Resources/index.php"

# Send a GET request to the website
response = urllib.request.urlopen(url)

# Parse the HTML content of the website using BeautifulSoup
soup = BeautifulSoup(response, 'html.parser')

# Find all the <a> tags with the lecture links
lecture_links = soup.find_all('a')

# Define the directory to save the downloaded files
directory = r"C:\Users\shaik\OneDrive - University of Waterloo\UW SE\2A\CS241\Lecture Slides - Carmen Bruni"
os.makedirs(directory, exist_ok=True)

# Function to sanitize the file name
def sanitize_filename(filename):
    # Replace disallowed characters with underscores
    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    return filename

# Iterate over the lecture links and download the files
for link in lecture_links:
    # Get the lecture title from the link text
    lecture_title = link.text.strip()
    
    # Get the lecture file URL
    lecture_url = link['href']
    
    # Skip non-PDF files
    if not lecture_url.endswith('.pdf'):
        continue
    
    # Construct the complete lecture file URL
    lecture_file_url = url + lecture_url[1:]  # Removing the leading dot (.) from the relative URL
    
    # Sanitize the lecture title for the file name
    sanitized_title = sanitize_filename(lecture_title)
    
    # Save the lecture file with the appropriate title and extension
    filename = sanitized_title + '.pdf'
    filepath = os.path.join(directory, filename)
    
    urllib.request.urlretrieve(lecture_file_url, filepath)
    
    print(f"Downloaded: {filename}")

print("All lectures downloaded successfully!")
