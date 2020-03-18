# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 20:15:12 2019

@author: anustubh agnihotri
"""
##import the pytesseract library
import pytesseract
##use Image library for reading images
from PIL import Image

##Point towards the image file
Image_File='C:/Users/anust/Dropbox/Mac/Documents/Courses/PS239T_Spring2020/08_data-cleaning/01_class1/INFO_Q1 2019 Market Medians Report_1.png'
##read the image file
img=Image.open(Image_File)

##convert into text
text=pytesseract.image_to_string(img, lang='eng')

##write the output
with open('C:/Users/anust/Dropbox/Mac/Documents/Courses/PS239_T/Examples/Tesseract/INFO_Q1 2019 Market Medians Report_1.txt','w', encoding='utf-8') as myfile:
           myfile.write(text)



##Point towards the image file
Image_File_Hindi='C:/Users/anust/Dropbox/Mac/Documents/Courses/PS239_T/Examples/Tesseract/Hindi_1.png'
##read the image file
img_hindi=Image.open(Image_File_Hindi)

##convert into text
text=pytesseract.image_to_string(img_hindi, lang='hin')

##write the output
with open('C:/Users/anust/Dropbox/Mac/Documents/Courses/PS239_T/Examples/Tesseract/Hindi_1.txt','w', encoding='utf-8') as myfile:
           myfile.write(text)


##transliteration
           
from indic_transliteration import sanscript
from indic_transliteration.sanscript import SchemeMap, SCHEMES, transliterate
from transliterate import detect_language, translit, get_available_language_codes

#get text in hindi
hindi_file_path = 'C:/Users/anust/Dropbox/Mac/Documents/Courses/PS239_T/Examples/Tesseract/Hindi_1.txt'
#open the file using utf-8 encoding 
hindi_file = open(hindi_file_path,'r',encoding='UTF-8')
##get the contents
hindi_text=hindi_file.read()
#transliterate from hindi to english
English_text=(transliterate(hindi_text, sanscript.DEVANAGARI, sanscript.HK))
#write back
English_text = English_text.lower()

with open('C:/Users/anust/Dropbox/Mac/Documents/Courses/PS239_T/Examples/Tesseract/English_Hindi_1.txt','w', encoding='utf-8') as myfile:
           myfile.write(English_text)
        