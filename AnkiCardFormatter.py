import sys

# small Python script for creating verb-specific Anki decks
# takes two arguments:
#	file1: the forms of the verb you want
#		formatting of the lines has to be:
#		yourLanguage;thatLanguage;past tense singular;past tense plural;participle
#	file2: your output file (will contain the lines depicted in "cardLine"
#
# usage: python AnkiCardFormatter.py file1.txt file2.txt
#
def buildImportFile(file1,file2):
	with open(file2, 'a') as outfile, open(file1, 'r') as infile:
		for line in infile:
			line = line.strip()
			a = line.split(";")
			cardLine = str(a[0])+";"+str(a[1])+"<br><br>Past: "+str(a[2])+ " - "+str(a[3])+"<br>Perfect: "+str(a[4])+'\n'
			outfile.write(cardLine)

buildImportFile(str(sys.argv[1]),str(sys.argv[2]))
