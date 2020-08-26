# Simple script for renaming files in batches

This is a simple python script that takes input from a txt file and changes the part of the names of multiple files
Uses tesseract-OCR to read data from a jpg/png file.

for now it works with jpg files only. will update the script so you can also mention the file extension.

## Changes
v2: CLI added! read below for more information

## Instructions

in v2, i've added CLI to make life easier 😋
### usage
```
python script.py --help
```
There are 4 options for the CLI:
    
    --name: this specifies the event name [REQUIRED]
    --data: this is the path to input data, usually a .txt file (defaults to ./data.txt)
    --input: this is the path to the pictures (defaults to ./input) [JPEGs only]
    --dest: this is the path to the output (defaults to ./input)

## Requirements
1. [tesseract-OCR](https://github.com/UB-Mannheim/tesseract/wiki)
2. pytesseract(pip install pytesseract)

## Upcoming Changes
1. adding a mode to run renamer without tesseract. This would allow to use this for files other than JPEGs.
