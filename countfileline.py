#this is the module
def getnumline(filename):
	""" THIS MODULE WILL HELP YOU TO COUNT TOTAL NUMBER OF LINE IN A FILE """
	with open(f'/storage/emulated/0/{filename}','r') as d:
		Counter = 0
		Content = d.read() 
		CoList = Content.split("\n") 
		for i in CoList: 
		    if i:
		    	Counter += 1
	return Counter
if __name__=="__main__":
	gh=getnumline("trainBOOK.py")
	print(gh)