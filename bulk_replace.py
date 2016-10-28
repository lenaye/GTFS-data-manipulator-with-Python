# Python script to bulk replace all instances of a string in a single column of all rows with a new string, in a GTFS file
# Usage: >bulk_replace.py -f <source file> -s <csv file containing substitutes> > output.txt 
#
#
# Substitute file format:
# old_string1, new_string1
# old_string2, new_string2
# old_string3, new_string3
# old_string4, new_string4
# old_string5, new_string5
#
# Source file can be any GTFS file which requires bulk replacment of data in a single field
# Typical Use Case: You have decided to change the trip_ids in the trips.txt and they have to be reflected in the stop_times.txt file.
#
# Leonard Aye - Oct 2016.


import argparse

def replace(text,replacements):	
	for i, j in replacements.iteritems():
		text = text.replace(i, j)

	return text
	
def main(inFile,subsFile):

	replacements = {}
	with open(subsFile, 'r') as f:
		for line in f:
			line = line.rstrip()
			splitLine = line.split(',')
			replacements[splitLine[0]] = splitLine[1]
	
	fhand = open(inFile,'r')
	text = fhand.read()
	new = replace(text,replacements)
	print 'after\n', new
	
	
	
if __name__ == '__main__':

        parser = argparse.ArgumentParser()

        parser.add_argument("-f", "--file", dest="inFile", help="File", metavar="STRING")
        parser.add_argument("-s", "--substitute", dest="subsFile", help="File containing substitues", metavar="STRING")

        args=parser.parse_args()
        main(args.inFile,args.subsFile)
		
		