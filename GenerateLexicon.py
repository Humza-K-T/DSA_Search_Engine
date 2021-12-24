import ProjectConfiguration
from Lexicon import Lexicon


#Starting of function
#Takes 2 arguments, i.e., starting & ending file 
#returns nothing

def GenerateLexicon(startingfile, endingfile):

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

	# LexiconLexicon = lexicon.ReadLexicon()

	# for i, word in enumerate(LexiconLexicon):
	# 	if i >= number:
	# 		break

	# 	print(f"\t{word}: {LexiconLexicon[word]}")

	# print("\n")
	# print('*'*137)
	# print('-'*137)
	
