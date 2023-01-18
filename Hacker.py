def hacker(diractory):
	import os
	import time
	from countline import getnumline#its a userbuilt module that counts number of line in a file
	from random import shuffle
	total_file=os.listdir(diractory)#you have to give your reposatry name 
	py_files_list=[]#This list will store all python files in given diractory
	for files in total_file:#itarating throw every file in tge given diractory
	     if files.endswith(".py"):
	     	py_files_list.append(files)#if any file ends with .py it will it will store inside py_files_list you can also use other extenshon but i only have py files thats why iuse .py
	     else:
	     	pass
	shuffle(py_files_list)#then i will shuffel it so i can create some randomness in the terminal
	for file in py_files_list*4:#*4 because i have few py files in this devise so i repeted it multipal times
		total_line=getnumline(diractory,file)#this is a userbilt function that tells us how many lines of code is written frist parameter is path second is file name
		with open(diractory+file,"r") as data:
			for _ in range(1,total_line):#this loop will run depnading on how many lines are in the code
				read_line=data.readline()#and read line
				if "#" in read_line:
					print('\033[31m'+read_line)#it will convert the line into red color you change the color by changing [31 or[32
				else:
					print('\033[92m'+read_line)#this will be green
				time.sleep(00.1)#for some delay
hacker("/data/user/0/ru.iiec.pydroid3/files/aarch64-linux-android/lib/python3.9/")#you can give your diractory and spacific diractris also