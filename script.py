import os
import time
import pytesseract
import click
from PIL import Image
from OCR import match
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

start = time.time()


@click.command()
@click.option('--name',required=1)
@click.option('--data',default='./data.txt')
@click.option('--input',default='./input')
@click.option('--dest',default='./input')
def main(name,data,input,dest):
    with open('{}'.format(data)) as file:
        array = file.read().split()
        print(array)
    

    data = [s.strip('\n') for s in array]
    for i in range(len(data)):
        data[i] = data[i].lower()

    data_path = os.listdir('{}'.format(input))
    event_name = '{}'.format(name)

    for i in range(len(data_path)):
        filename = data_path[i]
        src = '{}/'.format(input) + filename
        name = match(data,src)
        suffix = event_name + '_' + name + '.jpg'
        dst = '{}/'.format(dest) + suffix
        os.rename(src,dst)
        print(f'renamed {filename} to {suffix}')
if __name__ == '__main__':
    main()
else:
    print("Error running code")
end = time.time()
run_time = round(end-start,3)        
print(f'Task finished [{run_time}ms]')