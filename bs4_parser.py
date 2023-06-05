import requests
from bs4 import BeautifulSoup
import os

# Define the URL of the website
url = "https://cs.uwaterloo.ca/~cbruni/CS241Resources/lectures/2019_Winter/"

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content of the website using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the <a> tags with the lecture links
lecture_links = soup.find_all('a')

# Define the directory to save the downloaded files
directory = r"C:\Users\shaik\OneDrive - University of Waterloo\UW SE\2A\CS241\Lecture Slides - Carmen Bruni"
os.makedirs(directory, exist_ok=True)

# Function to sanitize the file name
def sanitize_filename(filename):
    # Replace disallowed characters with underscores
    filename = filename.replace("_", ": ")
    filename = filename.replace(".pdf", "")
    return filename

# Iterate over the lecture links and download the PDF files
for link in lecture_links:
    # Get the lecture file URL
    lecture_file_url = url + link['href']
    
    # Skip non-PDF files
    if not lecture_file_url.endswith('.pdf'):
        continue
    
    # Send a GET request to download the lecture file
    lecture_response = requests.get(lecture_file_url)
    
    # Get the lecture title from the file name
    lecture_title = sanitize_filename(link['href'])
    
    # Save the lecture file with the appropriate title and extension
    filename = lecture_title + '.pdf'
    filepath = os.path.join(directory, filename)
    
    with open(filepath, 'wb') as file:
        file.write(lecture_response.content)
    
    print(f"Downloaded: {filename}")

print("All lectures downloaded successfully!")
