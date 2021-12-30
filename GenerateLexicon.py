import ProjectConfiguration
from Lexicon import Lexicon


#Starting of function
#Takes 2 arguments, i.e., starting & ending file 
#returns nothing

def GenerateLexicon(startingfile, endingfile):
	"""Takes files & creates lexicon via functions in Lexicon.py file. Passes files, creates dictionary & prints the words."""
	#creating lexicon, passing the path
	lexicon = Lexicon(ProjectConfiguration.LEXICONPATH)

	#calling function to use dataset files
	lexicon.CreateLexicon(ProjectConfiguration.InputPath(startingfile, endingfile))

	print("\n")
	print(f"Lexicon created with {len(lexicon)} words.")
	print("\n")
	
	#printing process progress

	print('-'*137)
	print('*'*137)

	#initializing variables
	barrel = 0
	number = len(lexicon)
	#number=50

	print("\n")
	print(f"{number} Words Are: ")
	print("\n")

