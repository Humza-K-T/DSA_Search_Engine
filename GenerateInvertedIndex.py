import os
import pickle
import ProjectConfiguration
from InvertedIndex import InvertedIndex
from Lexicon import Lexicon
import concurrent.futures


#Starting of function
#Takes 1 arguments
#returns nothing

def GenerateInvertedIndex():
	"""Generate inverted index, takes nothing input, calls functions from InvertedIndex.py file.
	First creating lexicon & invertedindex instance.Looks for files at respective path & creates threads and calls creatreinvertedindex func"""

	#creating lexicon, passing the path
	InvIndLexicon = Lexicon(ProjectConfiguration.LEXICONPATH)

	#passing forward barrel path
	GenInvInd = InvertedIndex(ProjectConfiguration.INVERTEDINDEXPATH, ProjectConfiguration.TEMPORARYINVERTEDINDEXPATH, len(InvIndLexicon), ProjectConfiguration.MAXIMUMSIZE )

	with concurrent.futures.ThreadPoolExecutor() as executor:

		#creating empty dictionary
		GenInvIndDict = []

		mypath=ProjectConfiguration.FORWARDINDEXPATH
		filesToOpen=[f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f)) and f.startswith("batch_")]
		for file in filesToOpen:
			file= ProjectConfiguration.FORWARDINDEXPATH+"/"+file
			thread = executor.submit(GenInvInd.CreateInvertedIndex, file)
			GenInvIndDict.append(thread)
		
		for index in concurrent.futures.as_completed(GenInvIndDict):
			print("Inverted Index Created Successfully!")

		#merging temporary created index
		GenInvInd.MergeIndex()

	