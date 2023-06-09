import requests
from bs4 import BeautifulSoup
import os
import re
from urllib.parse import urljoin

# Define the URL of the website
url = "https://cs.uwaterloo.ca/~david/cs348/schedule.html"

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content of the website using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the <a> tags with the lecture links within <li> elements
lecture_links = soup.find_all('li')

# Define the directory to save the downloaded files
directory = r"C:\Users\shaik\OneDrive - University of Waterloo\UW SE\2B\CS348\Lecture Slides"
os.makedirs(directory, exist_ok=True)

# Function to sanitize the file name
def sanitize_filename(filename):
    # Replace disallowed characters with underscores
    filename = re.sub(r'[<>:"/\\|?*\n]', '_', filename)
    filename = filename.replace('.pdf', '')
    return filename

# Iterate over the lecture links and download the PDF files
for link in lecture_links:
    # Find the <a> tag within the <li> element
    anchor_tag = link.find('a')
    if anchor_tag is None:
        continue

    # Get the lecture file URL using urljoin
    lecture_file_url = urljoin(url, anchor_tag['href'])

    # Skip non-PDF files
    if not lecture_file_url.endswith('.pdf'):
        continue

    # Send a GET request to download the lecture file
    lecture_response = requests.get(lecture_file_url)

    # Get the lecture title from the file name
    lecture_title = sanitize_filename(anchor_tag.text)

    # Save the lecture file with the appropriate title and extension
    filename = lecture_title + '.pdf'
    filepath = os.path.join(directory, filename)

    with open(filepath, 'wb') as file:
        file.write(lecture_response.content)

    print(f"Downloaded: {filename}")

print("All lectures downloaded successfully!")
