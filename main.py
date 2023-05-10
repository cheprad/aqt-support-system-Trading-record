import PyPDF2
import os

# Replace "directory_path" with the path to the directory you want to read
directory_path = "input_file/"

# List all the files in the directory
file_names = os.listdir(directory_path)

# Loop through the file names and print them
for file_name in file_names:
    print(file_name)
    # Open the PDF file in binary mode
    pdf_file = open(directory_path+str(file_name), 'rb')

    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    # # Initialize an empty string to store the text
    text = ''
    i = 0
    # Loop through each page of the PDF and extract the text
    for page_num in range(pdf_reader.numPages):
        page_obj = pdf_reader.getPage(page_num)
        text += page_obj.extractText()
        i += 1 
        print(text)

    # Close the PDF file
    pdf_file.close()

    # Cut the string using slicing
    file_only_name = file_name[:-4]
    
    # Open a new text file and write the extracted text to it
    text_file = open("text/"+file_only_name+".txt", 'w', encoding="utf-8")
    text_file.write(text)
    text_file.close()