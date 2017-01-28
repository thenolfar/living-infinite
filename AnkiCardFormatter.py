import sys

def buildImportFile(file1,file2):
	filenameIn = file1
	filenameOut = file2
	with open(filenameOut, 'a') as outfile, open(filenameIn, 'r') as infile:
		for line in infile:
			line = line.strip()
			a = line.split(";")
			cardLine = str(a[0])+";"+str(a[1])+"<br><br>Imperfekt: "+str(a[2])+ " - "+str(a[3])+"<br>Partizip: "+str(a[4])+'\n'
			outfile.write(cardLine)

buildImportFile(str(sys.argv[1]),str(sys.argv[2]))
