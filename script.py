import os
import time
import pytesseract
from PIL import Image
from OCR import match
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"


with open('data.txt') as file:
    array = file.read().split()
    
    

data = [s.strip('\n') for s in array]
for i in range(len(data)):
    data[i] = data[i].lower()

data_path = os.listdir("./input")
start = time.time()
def main():
    event_name = input('Enter Event Name: ')

    for i in range(len(data_path)):
        filename = data_path[i]
        src = './input/' + filename
        name = match(data,src)
        """print(name)"""
        suffix = event_name + name + '.jpg'
        dst = './input/' + suffix
        os.rename(src,dst)
        print(f'renamed {filename} to {suffix}')
if __name__ == '__main__':
    main()
else:
    print("Error running code")
end = time.time()
run_time = round(end-start,3)        
print(f'Task finished [{run_time}ms]')