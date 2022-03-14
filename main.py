import re
import csv
import os

def reader(filename, thisFile, operation_type):
	with open(filename, "r", encoding="utf-8") as f:
		for row in csv.reader(f):
			if any(field.strip() for field in row):
				text = ""
				for item in row:
					text += "," + item
				global a 
				a = pars_object(text)
				if operation_type == 0:
					add_row_circ(thisFile)
				if operation_type == 1:
					add_row_acirc(thisFile)
	base = os.path.splitext(thisFile)[0]
	os.rename(thisFile, base + ".koc")

def add_row_circ(thisFile):
	if not os.path.exists(thisFile):
		with open(thisFile, "w", newline = "", encoding="utf-8") as csvfile:
			writer = csv.writer(csvfile, delimiter='\t')
			header = ["Version=1.0","Generator=RuslanDat2koc","GeneratorVersion=0.1"]
			writer.writerow(header)
			row = [a.date3,"issue",a.holdingname,a.bookname]
			writer.writerow(row)
	
	else:
		with open(thisFile, "a", newline = "", encoding="utf-8") as csvfile:
			writer = csv.writer(csvfile, delimiter='\t')
			row = [a.date3,"issue",a.holdingname,a.bookname]
			writer.writerow(row)

def add_row_acirc(thisFile):
	if not os.path.exists(thisFile):
		with open(thisFile, "w", newline = "", encoding="utf-8") as csvfile:
			writer = csv.writer(csvfile, delimiter='\t')
			header = ["Version=1.0","Generator=RuslanDat2koc","GeneratorVersion=0.1"]
			writer.writerow(header)
			row = [a.date1003,"issue",a.holdingname,a.bookname]
			writer.writerow(row)
			row = [a.date3,"return",a.bookname]
			writer.writerow(row)
	
	else:
		with open(thisFile, "a", newline = "", encoding="utf-8") as csvfile:
			writer = csv.writer(csvfile, delimiter='\t')
			row = [a.date1003,"issue",a.holdingname,a.bookname]
			writer.writerow(row)
			row = [a.date3,"return",a.bookname]
			writer.writerow(row)

class pars_object:
	def __init__(self, text):
		self.text = text
		self.holdingname = " "
		self.bookname = " "
		self.date3 = " "
		self.date1003 = " "
		self.objects_fields()
	
	def objects_fields(self):
		m = self.text.split("@")
		for item in m:
			a = item.split(",",1)
			if a[0] == "100":
				self.holdingname = item.split("=")[1].split(",",1)[0]
			if a[0] == "140":
				self.bookname = item.split("=")[1].split(",",1)[0]
			if a[0] == "3":
				b = item.split("=")[1]
				self.date3 = b[0] + b[1] + b[2] + b[3] + "-" + b[4] + b[5] + "-" + b[6] + b[7] + " " + b[8] + b[9] + ":" + b[10] + b[11] + ":" + b[12] + b[13]
			if a[0] == "1003":
				b = item.split("=")[1]
				self.date1003 = b[0] + b[1] + b[2] + b[3] + "-" + b[4] + b[5] + "-" + b[6] + b[7] + " " + b[8] + b[9] + ":" + b[10] + b[11] + ":" + b[12] + b[13]

dirname = './'
files = os.listdir(dirname)

for item in files:
	base = item.split(".",1)
	if base[1] == "dat":
		if base[0][0] == "a":
			if os.path.exists(base[0] + ".koc"):
				os.remove(base[0] + ".koc")
			if os.path.exists(base[0] + ".csv"):
				os.remove(base[0] + ".csv")	
			reader(item, base[0] + ".csv", 1)
		if base[0][0] == "c":
			if os.path.exists(base[0] + ".koc"):
				os.remove(base[0] + ".koc")
			if os.path.exists(base[0] + ".csv"):
				os.remove(base[0] + ".csv")
			reader(item, base[0] + ".csv", 0)


