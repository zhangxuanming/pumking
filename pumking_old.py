# Filename:pp.py
# this is the one to transform xml to xml for pumking patch

# predeifned xslt root file "pk.txt"


# from lxml import etree
import lxml.etree as etree
import os.path
import sys
import time
import unicodedata
import chardet

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
	date = time.strftime("%Y_%M_%d_%H_%M")
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
	# try:		
	# Open XSLT file and get bytes doc
	xslt_root = open(rootXSLT,'r')
	xslt_rootBytes = xslt_root.read()	
	xslt_root.close()


	# #open source File and get bytes doc
	dom = open(sourceXML,'r')
	domBytes = dom.read()
	dom.close()
	print(domBytes)
	# domEncodingType = chardet.detect(domBytes)
	# print(domEncodingType)
	# # s = domBytes.decode("CP936","ignore")
	# s = domBytes.decode(domEncodingType["encoding"],"ignore")
	# print(s)
	# sys.exit()
	# #get string from XSLT file	
	# # xs = str(xslt_rootBytes.decode(domEncodingType,"ignore"))	
	# xsltStr = str(xslt_rootBytes,domEncodingType,"ignore").encode("utf-8","ignore")
	# print(domBytes)
	# s = domBytes.decode(domEncodingType,"ignore")
	# print(s)
	# sys.exit()
	# domStr = str(domBytes,domEncodingType,"ignore").encode("utf-8","ignore")
	
	xsltXML = etree.fromstring(xsltStr)
	domXML = etree.fromstring(domStr)
	transform = etree.XSLT(xsltXML)
	result = transform(domXML)

	# print(xslt_rootBytes)
	# print(domBytes)
	# xslt_root = etree.parse(rootXSLT)
	# dom = etree.parse(sorceXML)
	# transform = etree.XSLT(xslt_root)
	# result = transform(dom)
	# print(type(result))
	# detector = UniversalDetector()
	# for line in result.readlines():
	# 	detector.feed(line)
	# 	if detector.done:		
	# 		break
	# detector.close()
	# usock.close()
	# print (detector.result)
	print(str(result))
	f = open(targetXML,'w')
	f.write(str(result))
	f.close()
	print("-------------------------------")
	print("New File Created:\n\r{}".format(targetXML))
	# except:
	# 	print("looks like something wrong with the file")
	# 	print("Please contact IT suppot ITsuppot@mysale.com")

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
