import pytesseract
from PIL import Image
from configparser import ConfigParser

config = ConfigParser()
config.read("./config.ini")
ocr_path = config['DEFAULT']['path']

pytesseract.pytesseract.tesseract_cmd = f"{ocr_path}"

""" img = Image.open('./input/1.jpg')
img_data = pytesseract.image_to_string(img)

print(img_data)
print(img_data.split(' ')) """

def match(data,src_path):
    img = Image.open(src_path)
    img_data = pytesseract.image_to_string(img)
    img_data = img_data.lower()
    img_data = img_data.split(' ')

    for name1 in data:
        for name2 in img_data:
            if name1 == name2:
                return name1 

    




