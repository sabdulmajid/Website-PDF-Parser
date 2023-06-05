import requests
from bs4 import BeautifulSoup
import os

# Define the URL of the website
url = "https://cs.uwaterloo.ca/~cbruni/CS241Resources/index.php"

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content of the website using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the <a> tags with the lecture links
lecture_links = soup.find_all('a')

# Specify the path to the folder where you want to save the files
folder_path = r"C:\Users\shaik\OneDrive - University of Waterloo\UW SE\2A\CS241\Lecture Slides - Carmen Bruni"

# Iterate over the lecture links and download the files
for link in lecture_links:
    # Get the lecture title from the link text
    lecture_title = link.text.strip()
    
    # Get the lecture file URL
    lecture_url = link['href']
    
    # Construct the complete lecture file URL
    lecture_file_url = url + lecture_url[1:]  # Removing the leading dot (.) from the relative URL
    
    # Send a GET request to download the lecture file
    lecture_response = requests.get(lecture_file_url)
    
    # Determine the file extension
    file_extension = os.path.splitext(lecture_file_url)[1]
    
    # Save the lecture file with the appropriate title
    filename = lecture_title + file_extension
    filepath = os.path.join(folder_path, filename)
    
    with open(filepath, 'wb') as file:
        file.write(lecture_response.content)
    
    print(f"Downloaded: {filename}")

print("All lectures downloaded successfully!")
