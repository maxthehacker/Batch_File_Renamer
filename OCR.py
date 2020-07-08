import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

img = Image.open('C:/Users/srava/Pictures/photoshop/Protocol Day/code-a-thon_Swetha_1stplace.jpg')
img_data = pytesseract.image_to_string(img)
req_str = 'Swetha Swaminathan'
if(req_str in img_data):
    print(1)
else:
    print(0)  




