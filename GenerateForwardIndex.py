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
	"""Genertaed forward index, takes all files as input, calls functions from ForwardIndex.py file.
	Uses multithreading for parallel execution by dividing input files into 2 seprate threads."""


	#creating lexicon obj, passing the path
	ForIndLexicon = Lexicon(ProjectConfiguration.LEXICONPATH)

	#creatinv forwardindex obj, passing forward barrel path
	GenForInd = ForwardIndex(ProjectConfiguration.FORWARDINDEXPATH, ForIndLexicon)

	#threads management
	with concurrent.futures.ThreadPoolExecutor() as executor:

		#creating empty dictionary
		GenForIndDict = []

		#if starting file number is same as endong file number, only 1 file
		if startingfile == endingfile:
			#single thread creation
			Thread1 = executor.submit(GenForInd.AddForwardIndex, ProjectConfiguration.InputPath(startingfile, startingfile + 1,True), f"batch_00{startingfile}",True)
			
			#appending in dict
			GenForIndDict.append(Thread1)

		#if starting file number is NOT same as endong file number, 2 or more files
		else:
			#dividing files in two parts
			middle = int(( startingfile+endingfile) / 2)

			#creating 2 seprate threads
			Thread2 = executor.submit(GenForInd.AddForwardIndex, ProjectConfiguration.InputPath(startingfile, middle,True), f"batch_00{startingfile}")
			Thread3= executor.submit(GenForInd.AddForwardIndex,ProjectConfiguration.InputPath(middle, endingfile,True), f"batch_00{middle}")
			
			#appending in dict
			GenForIndDict.append(Thread2)
			GenForIndDict.append(Thread3)

		#if threads execution completed
		for index in concurrent.futures.as_completed(GenForIndDict):
			print("\n")
			print(f"{index.result()} Forward Index Created Successfully!")

	