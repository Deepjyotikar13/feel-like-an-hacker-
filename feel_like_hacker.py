#deepjyoti
#thanks for visiting my code
import os
import time
from random import shuffle
from countfileline import getnumline#this is a user built module to count total number of line

def get_total_pyfile():
	total_file=os.listdir('/storage/emulated/0')#you have to give your reposatry name 
	text_files_list=[]
	for i in range(0,len(total_file)):#it will go thrue all files in your diractory and identify alk py files 
	     values=total_file[i]
	     if values[-2::]=="py":
	     	text_files_list.append(values)#willl retyrn all py file
	shuffle(text_files_list)#shuffling all .py files
	return text_files_list

def get_hackcode():
	file_py=get_total_pyfile()
	for kl in range(0,len(file_py)):#this will run for all files
		file_line=getnumline(file_py[kl])#count total line in file
		with open(f'/storage/emulated/0/{file_py[kl]}') as opf:#this will open an file acording to its index
			for jj in range(0,file_line+1):
				line_read=opf.readline()#it will read all line one by one 
				if "#" in line_read:
					print('\033[31m'+line_read)#This'\033[32m' will turn your text into green wow
				elif "import" in line_read:
					print("\033[94m"+line_read)
				else:
					print( '\033[92m' +line_read)
				time.sleep(0.1)
get_hackcode()
print( "         YOU HAVE BEEN HACKED BROOOO")	
