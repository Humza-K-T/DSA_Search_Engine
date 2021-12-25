import GenerateForwardIndex 
import GenerateInvertedIndex
import GenerateLexicon
from Lexicon import Lexicon
import os
import ProjectConfiguration
#start of function
#simply prints menu
#takes user input
#returns option




# print("\n")
# print("You Selected *Generate Lexicon*!")
# print("Enter The Following: ")
# print("\n")

# starting = 0
# directory=ProjectConfiguration.INPUTPATH
# total_files=len([item for item in os.listdir(directory) if os.path.isfile(os.path.join(directory, item))])

# ending = total_files
# print("\n")

# GenerateLexicon.GenerateLexicon(starting,ending)


# # print("\n")
# # print("You Selected *Create Forward Index*!")
# # # print("Enter The Following: ")
# # # print("\n")

# starting = 0

# directory=ProjectConfiguration.UPDATED_JSONS
# total_files=len([item for item in os.listdir(directory) if os.path.isfile(os.path.join(directory, item))])

# ending = total_files
# # print("\n")

# # GenerateForwardIndex.GenerateForwardIndex(starting,ending)
# GenerateForwardIndex.GenerateForwardIndex(starting,ending)


# # # print("\n")
# # # print("You Selected *Create Inverted Index*!")
# # # print("Enter The Following: ")
# # # print("\n")

# # # # starting = int(input('Starting File Number: '))
# # # # ending = int(input('Ending File Number: '))
# strstart=str(0)
# # strend=str(len([name for name in os.listdir('.') if os.ProjectConfiguration.UPDATED_JSONS.isfile(name)]))
# directory=ProjectConfiguration.UPDATED_JSONS
# total_files=len([item for item in os.listdir(directory) if os.path.isfile(os.path.join(directory, item))])
# strend = str(total_files)
# userinput=strstart+","+strend
# range = userinput.split(',')
# # print("\n")

GenerateInvertedIndex.GenerateInvertedIndex(range)

