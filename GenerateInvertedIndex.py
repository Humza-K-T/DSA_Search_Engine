import os
import pickle
import ProjectConfiguration
from InvertedIndex import InvertedIndex
from Lexicon import Lexicon
import concurrent.futures


#Starting of function
#Takes 1 arguments
#returns nothing

def GenerateInvertedIndex(InvertedIndexRange):

	#creating lexicon, passing the path
	InvIndLexicon = Lexicon(ProjectConfiguration.LEXICONPATH)

	#passing forward barrel path
	GenInvInd = InvertedIndex(ProjectConfiguration.INVERTEDINDEXPATH, ProjectConfiguration.TEMPORARYINVERTEDINDEXPATH, len(InvIndLexicon), ProjectConfiguration.MAXIMUMSIZE )

	with concurrent.futures.ThreadPoolExecutor() as executor:

		#creating empty dictionary
		GenInvIndDict = []

		for index in InvertedIndexRange:

			fileToOpen=os.path.join(ProjectConfiguration.FORWARDINDEXPATH, f"batch_00{index}")
			if os.path.isfile(fileToOpen):

				thread = executor.submit(GenInvInd.CreateInvertedIndex, fileToOpen)


		
		for index in concurrent.futures.as_completed(GenInvIndDict):
			print(f"{index.result()}  Inverted Index Created Successfully!")

	GenInvInd.MergeIndex()


	#printing process progress

	# print('-'*137)
	# print('*'*137)

	# #initializing variables
	# barrel = 0
	# number = 20

	# print("\n")
	# print(f"{number} Barrel Enteries {barrel}:")
	# print("\n")

	# with open(os.path.join(ProjectConfiguration.INVERTEDINDEXPATH, f"{barrel:03}_inverted"), 'rb') as InvertedIndexData:
		
	# 	InvertedIndexOpen = pickle.load(InvertedIndexData)
	# 	for i, word_id in enumerate(InvertedIndexOpen):

	# 		if i >= number:
	# 			break
			
	# 		#printing
	# 		print(f"\t{word_id}:")
	# 		for doc in InvertedIndexOpen[word_id]:
	# 			print(f"\t\t{doc}: {InvertedIndexOpen[word_id][doc]}")

	# print("\n")
	# print('*'*137)
	# print('-'*137)
	