import re # For regex
import PyPDF2 # For pdfs
import random # For sampling
import glob # For multiple files


def import_resume(path='/Users/ekremguzelyel/Desktop/Assignments/Cs/Hackathons/ResumeExtractor/SamplePDF/Sample_Resume.pdf'):
   # Opening PDF file and cleaning text.

   pdfFileObj = open(path, 'rb') 
   pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

   print("Resume found.\n# of pages:", pdfReader.numPages) 
    
   pageObj = pdfReader.getPage(0) 
   text = pageObj.extractText()
   pdfFileObj.close() 

   # Clean spaces and handle special characters.
   text = re.sub("\s\s+", " ", text).lower()
   text = text.replace("ó","\"").replace("ò","\"").replace("¥!", "").replace("õ","'").replace("\n"," ")

   # Apply regex to get list of words.
   reg_list = (re.split(r'[^(\w+(\.+|@)\w+)]|[()]', text))

   # Filter None values. -> Regex could be implemented better to eliminate this step. 
   # but, it works. So don't touch it :D
   key_list = list(filter(None,reg_list))
   final_text = " ".join(key_list)

   # print(text)
   print("Resume successfully extracted")
   
   return key_list, final_text

def import_keys(path='./keywords/*.txt'):
   '''Returns a dictionary of keywords for skill sets.
   Args:
      path: Directory where keywords present.
   Returns:
      keyword_dic: A dictionary of keywords.
   '''
   
   keyword_dic = {}
   stop_words = ['with','to', 'of','the', 'a', 'and','on']

   # Read from the list of files
   list_of_files = glob.glob(path)
   for file_name in list_of_files:
   #     print(file_name[11:-4])

       FI = open(file_name, 'r')
       keys = FI.read()
       
       keyword_dic[file_name[11:-4]] = set(re.split('\W+', keys.lower())).difference(stop_words)


       FI.close()

   print("Keywords imported.")
   return keyword_dic
