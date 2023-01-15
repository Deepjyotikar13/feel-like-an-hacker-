def getnumline(path,filename):
	""" THIS MODULE WILL HELP YOU TO COUNT TOTAL NUMBER OF LINE IN A FILE """
	with open(path+filename,'r') as d:
		Counter = 0
		Content = d.read() 
		CoList = Content.split("\n") 
		for i in CoList: 
		    if i:
		    	Counter += 1
	return Counter#the total number of line
def getnumline_module(path):
	""""this is for 1 liner the path and the filename together """
	with open(path,'r') as d:
		Counter = 0
		Content = d.read() 
		CoList = Content.split("\n") 
		for i in CoList: 
		    if i:
		    	Counter += 1
	return Counter#the total number of line
if __name__=="__main__":
	gh=getnumline_module("/storage/emulated/0/Hacker.py")
	print(gh)
	#print(getnumline.__doc__)