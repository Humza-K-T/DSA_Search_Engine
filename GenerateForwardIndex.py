import os
import pickle
import ProjectConfiguration
from ForwardIndex import ForwardIndex
from Lexicon import Lexicon
import concurrent.futures


#Starting of function
#Takes 2 arguments, i.e., starting & ending file numbers
#returns nothing

def GenerateForwardIndex(startingfile, endingfile):

	#creating lexicon, passing the path
	ForIndLexicon = Lexicon(ProjectConfiguration.LEXICONPATH)

	#passing forward barrel path
	GenForInd = ForwardIndex(ProjectConfiguration.FORWARDINDEXPATH, ForIndLexicon)

	with concurrent.futures.ThreadPoolExecutor() as executor:

		#creating empty dictionary
		GenForIndDict = []

		#if starting file number is same as endong file number
		if startingfile == endingfile:
			Thread1 = executor.submit(GenForInd.AddForwardIndex, ProjectConfiguration.InputPath(startingfile, startingfile + 1), f"batch_00{startingfile}")
			GenForIndDict.append(Thread1)

		#if starting file number is NOT same as endong file number
		else:
			middle = int(( startingfile+endingfile) / 2)
			Thread2 = executor.submit(GenForInd.AddForwardIndex, ProjectConfiguration.InputPath(startingfile, middle), f"batch_00{startingfile}")
			Thread3= executor.submit(GenForInd.AddForwardIndex,ProjectConfiguration.InputPath(middle, endingfile), f"batch_00{middle}")
			
			GenForIndDict.append(Thread2)
			GenForIndDict.append(Thread3)

		for index in concurrent.futures.as_completed(GenForIndDict):
			print("\n")
			print(f"{index.result()} Forward Index Created Successfully!")

	print("\n")
	
	#printing process progress
	
	print('-'*137)
	print('*'*137)

	#initializing variables
	barrel = 0
	number = endingfile-startingfile

	print("\n")
	print(f"{number} entrie(s) from barrel {barrel}:")
	print("\n")

	with open(os.path.join(ProjectConfiguration.FORWARDINDEXPATH, f"batch_00{barrel}"), 'rb') as ForwardIndexData:
		
		ForwardIndexOpen = pickle.load(ForwardIndexData)
		for i, doc_id in enumerate(ForwardIndexOpen):

			if i >= number:
				break
			
			#printing
			print(f"\t{doc_id}:")
			for word_id in ForwardIndexOpen[doc_id]:
				print(f"\t\t{word_id}: {ForwardIndexOpen[doc_id][word_id]}")


	print("\n")
	print('*'*137)
	print('-'*137)

	#end of function