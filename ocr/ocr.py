from PIL import Image
from numpy import ndarray
import pandas as pd
import cv2 as cv
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
tessdata_dir_config = '--tessdata-dir "C:\Program Files\Tesseract-OCR\tesseract"'


image = Image.open('11.jpg')
res = pytesseract.image_to_string(image, lang='eng')

print(res)



