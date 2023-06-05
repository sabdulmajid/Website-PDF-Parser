# Website PDF Parser

Welcome to the Website PDF Parser project! This Python script brings order and convenience to the world of PDF files. It empowers you to effortlessly download and organize a collection of PDFs from a website of your choice. Say goodbye to manual file management and embrace the power of automation! The project utilizes the ```requests``` library to retrieve the webpage content and the ```BeautifulSoup``` library to parse the HTML and extract the PDF links. Additionally, it uses the ```PyPDF2``` library to access the PDF metadata and rename the downloaded files.

## How It Works

The Website PDF Parser script follows these main steps:

1. **Retrieves** the webpage content using the requests library.
2. **Parses** the HTML content using BeautifulSoup to extract the links to the PDF files.
3. **Downloads** the PDF files using the requests library.
4. **Extracts** the PDF title from the metadata using the PyPDF2 library.
5. **Renames** the downloaded files based on their extracted titles.

## Getting Started

To clone and run the Website PDF Parser, follow these steps:

1. **Clone** the repository:
```bash
git clone https://github.com/sabdulmajid/Website-PDF-Parser.git
```
   
2. **Install** the required dependencies:

```bash
pip install requests beautifulsoup4 PyPDF2
```

3. **Open a terminal** or command prompt and navigate to the project directory:

```bash
cd website-pdf-parser
```

4. **Open the ```bs4_parser.py```** file in an IDE of your choice and specify the website URL and the directory to save the downloaded files.

```python
# Website URL
url = "https://example.com"

# Directory to save the downloaded PDF files
directory = r"/path/to/save/directory"
```

5. **Run** the script:

```bash
python bs4_parser.py
```

The script will download the PDF files from the specified website and save them to the specified directory.

## Renaming the files
When I first downloaded the files, I found that I didn't really like the file names (they were too cryptic). So I decided to add on this extra piece of code which renames the PDF according to the 'title' field present in the metadata, which made more sense as a PDF name. I also had to "sanitize" the file name because they contained illegal characters for a file name. Here is the code for it:
```python
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

    # Sanitize the filename
    sanitized_title = sanitize_filename(pdf_title)

    # Construct the new filename
    new_filename = f"Lecture {sanitized_title}.pdf"
    new_filepath = os.path.join(directory, new_filename)

    # Rename the file
    os.rename(filepath, new_filepath)

    print(f"Renamed: {filename} -> {new_filename}")
```

Now if you want to run this as well, simply run this script on your terminal:
```bash
python pdf_rename.py
```

## Common Issues
- **Invalid URL or Website Structure**: If you encounter errors related to the URL or website structure, ensure that the specified URL is correct and accessible. Verify that the website contains the expected <a> tags and follows a consistent structure.

- **Missing Dependencies**: If you encounter a "ModuleNotFoundError" or a similar error, ensure that you have installed the required dependencies. Use the following command to install the necessary libraries:

  ```bash
  pip install requests beautifulsoup4 PyPDF2
  ```
- **PDF Metadata Extraction**: If you encounter issues with extracting the PDF metadata using the PyPDF2 library, it may be due to the deprecated features. In such cases, the script falls back to extracting the title directly from the filename using regular expressions.

- **Corrupt PDF Files**: If the downloaded PDF files appear to be corrupt or have a significantly reduced file size, it could indicate an issue with the file retrieval process or the PDF source. Double-check the source website and ensure that the files are downloaded correctly.

## Contributions and Feedback
Contributions, suggestions, and bug reports are welcome! Feel free to open an issue or submit a pull request. If you have any feedback or ideas for improving the Website PDF Parser, please let me know.
