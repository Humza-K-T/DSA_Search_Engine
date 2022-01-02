import ProjectConfiguration
from Lexicon import Lexicon


#Starting of function
#Takes 2 arguments, i.e., starting & ending file 
#returns nothing

def GenerateLexicon(startingfile, endingfile):
	"""Takes files & creates lexicon via functions in Lexicon.py file. Passes files, creates dictionary & prints the number of words."""
	
	#creating lexicon obj, passing the path
	lexicon = Lexicon(ProjectConfiguration.LEXICONPATH)

	#calling function to use dataset files
	lexicon.CreateLexicon(ProjectConfiguration.InputPath(startingfile, endingfile))

	#initializing variables, getting length of lexicon
	number = len(lexicon)

	print(f"Lexicon created with {len(lexicon)} words.")
	#printing number of words found
	print(f"{number} Words Found!")
	

