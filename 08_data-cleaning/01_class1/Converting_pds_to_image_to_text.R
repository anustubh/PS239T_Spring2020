##This file uses pdftools to convert pdf (Transfer Orders) to image
##and then tesseract to convert the image to text 
##Author Anustubh Agnihotri
##This introduction will walk you through a basic introduction to the tesseract library
##and will include conversion from english and non-english language 

rm(list=ls())

library(tesseract)
library(pdftools)

working_dir='C:/Users/anust/Dropbox/Mac/Documents/Courses/PS239T_Spring2020/08_data-cleaning/01_class1/'

##Set working directory 
##Note: Saving frequenty used paths as variables is a good programming practice
setwd(working_dir)

##Select all PDF files 
pdf_file<-list.files(working_dir,"*.pdf")

#This is a generic code but right now I am selecting the Pdf file with 
#English content
pdf_file_hindi=pdf_file[1]
pdf_file_spanish=pdf_file[2]
pdf_file=pdf_file[3]

#down the library of the language that you are converting 
tesseract_download('eng')
#save it as a variable 
eng <- tesseract("eng")

####IMAGE
####First convert the PDFs into png file output in the working dir
####dpi decides the quality
pngfile <- pdftools::pdf_convert(paste(working_dir,pdf_file,sep=''), dpi = 600)

#Take one of the image files and convert into text 
text <- tesseract::ocr(pngfile[1],engine=eng)
#Get the name from the PDF file
file_name=gsub('^(.*).pdf','\\1',pdf_file)
#Create a file name that will be created in your local directory
file_path=paste(working_dir,file_name,'_1.txt',sep='')
#write the text file 
write.table(text,file_path,row.names=F,col.names=F,quote=F,fileEncoding="UTF-8")


#Non English language conversion
#hojadeayudapasaporte.pdf was downloaded from Maxico government's website

#there are different languages that can be used 
#more information https://github.com/tesseract-ocr/tesseract/wiki/Data-Files
tesseract_download('spa')
#we have chosen spanish
spanish <- tesseract("spa")
#convert the 
pngfile_spanish <- pdftools::pdf_convert(paste(working_dir,pdf_file_spanish,sep=''), dpi = 600)

#Take one of the image files and convert into text 
text_spanish <- tesseract::ocr(pngfile_spanish,engine=spanish)
#assign name for the text file
file_name_spanish=gsub('^(.*)_spanish.pdf','\\1',pngfile_spanish)
#create a file path
file_path_spanish=paste(working_dir,file_name_spanish,'.txt',sep='')
#write the file
write.table(text_spanish,file_path_spanish,row.names=F,col.names=F,quote=F,fileEncoding="UTF-8")


