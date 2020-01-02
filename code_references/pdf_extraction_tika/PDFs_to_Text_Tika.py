#!/usr/bin/env python
# coding: utf-8

# # PDFs to Text via Tika

# This file is to convert pdf files into text files by using Tika. It has been designed to search the specified folder, and return a folder containing the converted text files.
# 
# This code was initially written for the UofT3666 - Applied Natural Language Processing final project. That being said, there are some lines of code in here specifically to help clean up the output of the files that we were converting. This code was build upon the following gist: https://gist.github.com/nadya-p/373e1dc335293e490d89d00c895ea7b3.

# In[1]:


# imports
from tika import parser
import os
import datetime


# In[2]:


# class for extracting tika files
class TikaExtract(object):
    # initialize the object
    def __init__(self, source_directory, target_directory_name):
        # assigned variables for source_directory and target_directory_name
        self.dir = source_directory
        self.target = str(target_directory_name)
    
    # define recursive function to walk through directory and convert pdfs    
    def extract_text_from_pdfs_recursively(self):
        for root, dirs, files in os.walk(self.dir):
            for file in files:
                path_to_pdf = os.path.join(root, file)
                [stem, ext] = os.path.splitext(path_to_pdf)
                if ext == '.pdf':
                    print("Processing " + path_to_pdf)
                    # use tika to parse contents from file
                    pdf_contents = parser.from_file(path_to_pdf)
                    # project specific - convert to raw
                    raw_text = r'{}'.format(pdf_contents['content'])
                    # project specific - replace new lines with spaces
                    raw_text = raw_text.replace("\n"," ")
                    # project specific - replace double new lines with spaces
                    raw_text = raw_text.replace("\n\n" , " ")
                    # project specific - replace tabs with spaces
                    raw_text = raw_text.replace("\t"," ")
                    path_to_txt = stem + '.txt'
                    # check if target directory exists
                    if not os.path.exists(str(os.getcwd()) + self.target):
                        os.makedirs(str(os.getcwd()) + self.target)
                    # write the text file to the target directory
                    # names of the files will be the same, except have the .txt extension
                    with open(str(os.getcwd()) + self.target + str(file[:-4]) + ".txt", 'w') as txt_file:
                        print("Writing contents to " + str(os.getcwd()) + self.target + str(file[:-4]) + ".txt")
                        txt_file.write(raw_text)


# In[3]:


get_ipython().run_line_magic('pwd', '')


# In[4]:


# this is an example, performing the operation on a local machine
tikaextract = TikaExtract(source_directory=str(os.getcwd())+'/source_directory/',
                         target_directory_name='/target_directory/')


# In[5]:


# run the function
tikaextract.extract_text_from_pdfs_recursively()


# In[6]:


# operationalize the function, while providing default parameters
# default source directory is the current working directory
# target dirctory name is tika_documents_datetime
#        in the format "tika_documents_date_month_year_hour_minute_pm"
if __name__ == "__main__":
    tikaextract = TikaExtract(source_directory = str(os.getcwd()), target_directory_name = '/target_directory/')
    # ignore the below line
    #                         target_directory_name = '/tika_documents_' +str(datetime.datetime.now().strftime("%d_%m_%Y_%I_%M_%p"))+"/")
    tikaextract.extract_text_from_pdfs_recursively()

