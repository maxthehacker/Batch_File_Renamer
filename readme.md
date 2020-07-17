# Simple script for renaming files in batches

This is a simple python script that takes input from a txt file and changes the part of the names of multiple files
Uses tesseract-OCR to read data from a jpg/png file.

for now it works with jpg files only. will update the script so you can also mention the file extension.

## Instructions
Change path in **config.ini** to tessract.exe in the installation folder of tesseract-ocr on your computer. Default path is C:/Program Files/Tesseract-OCR/tesseract.exe.

Place files in the **input** folder and add data in **data.txt**.


Once you run **script.py** you can enter an Event Name which will be the prefix of the filenames followed by data provided in **data.txt**.


After the script runs all the files will be renamed and will be in the **input** folder.

## Requirements
1. [tesseract-OCR](https://github.com/UB-Mannheim/tesseract/wiki)
2. pytesseract(pip install pytesseract)

