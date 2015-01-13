# Filename:pp.py
# this is the one to transform xml to xml for pumking patch

# predeifned xslt root file "pk.txt"


# from lxml import etree
import lxml.etree as etree
import os.path
import sys
import time
import unicodedata
# import chardet

def welcome():
	os.system('cls')
	msg = {
	'1':"-------Welcom To MYSALEGROUP-------",
	'2':"Instructions:",
	"3":"1. Please Type the name of the file that you Downloaded from OZADMIN.",
	"4":"   Eg: blablabla.xml",
	"5":"2. Please Type The Filename That you want to SAVE To.",
	"6":"   Eg: Pumking Patch.xml",
	"7":"Then:",
	"8":"Go get a coffe :)",	
	}
	kyes = list(msg.keys())
	kyes.sort()
	for key in kyes:
		print(msg[key])

	print("---------------------------------\n\r")	

def getTargetFileName(prefix):
	date = time.strftime("%Y_%M_%d_%H_%M_%S")
	return "{}_{}.xml".format(prefix,date)

def getRootFileName(rootFile):
	ck = fileCheck(rootFile)
	if ck!=True:
		print("Can not find the XSLT File!!!")
		print("Please check if the [pumking.xslt] file in the folder")
		sys.exit()
	return rootFile

def fileCheck(filename):
	return os.path.isfile(filename)

def getSourceFileName():
	print("to exit the program please type quit")
	print("Please type The Name of the XML file You Downloaded From Admin Site")
	while True:		
		sourceFileName = input("Downloaded Filename : ")
		if sourceFileName == "quit":
			sys.exit()			

		fc = fileCheck(sourceFileName)
		if fc!=True:
			print("File not Exist,Please Try again")
			continue
		else:
			print("Your Awesome!")
			print("The Downloaded File name is : [{}]".format(sourceFileName))
			break	
	return sourceFileName	

def transformFile(rootXSLT,sourceXML,targetXML):
	try:		
		domFile = open(sourceXML,'r')
		domEncodingType = domFile.encoding
		domFile.close()

		# # Open XSLT file and get bytes doc
		# xslt_root = open(rootXSLT,'rb')
		# xslt_rootBytes = xslt_root.read()	
		# xslt_root.close()
		
		# # #open source File and get bytes doc
		# dom = open(sourceXML,'rb')	
		# domBytes = dom.read()
		# dom.close()

		xsltXML = etree.parse(rootXSLT)
		domXML = etree.parse(sourceXML)

		transform = etree.XSLT(xsltXML)
		result = transform(domXML)	

		result = str(result,domEncodingType,"ignore")
		
		f = open(targetXML,'w')
		f.write(str(result))
		f.close()
		print("-------------------------------")
		print("New File Created:\n\r{}".format(targetXML))
	except:
		print("looks like something wrong with the file")
		print("Please contact IT suppot ITsuppot@mysale.com")

def init():

	welcome()
	while True:
		rootFileName = getRootFileName("xslt\pumking.xslt")
		sourceFileName = getSourceFileName()
		TargetFileName = getTargetFileName("created_file\pumking")	
		transformFile(rootFileName,sourceFileName,TargetFileName)	

		ck = input("type y to continue, type n to exit: ")
		if ck == "y":
			continue	
		else:
			break

init()
