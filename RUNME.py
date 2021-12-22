import GenerateForwardIndex 
import GenerateInvertedIndex
import GenerateLexicon
from Lexicon import Lexicon


#start of function
#simply prints menu
#takes user input
#returns option

def menu():

		print("\n")
		print("Main Menu: ")
		print("1-Create Lexicon.")
		print("2-Create Forward Index.")
		print("3-Create Inverted Index.")
		print("4-EXIT.")
		print("\n")
		choice = input('Your Choice: ')

		return int(choice)

	#end of function


if __name__ == '__main__':
	choice=-1

while(choice!=4):
	choice=menu()

	if choice == 1:
		print("\n")
		print("You Selected *Generate Lexicon*!")
		print("Enter The Following: ")
		print("\n")

		starting = int(input('Starting File Number: '))
		ending = int(input('Ending File Number: '))
		print("\n")

		GenerateLexicon.GenerateLexicon(starting,ending)

	elif choice == 2:
		print("\n")
		print("You Selected *Create Forward Index*!")
		print("Enter The Following: ")
		print("\n")

		starting = int(input('Starting File Number: '))
		ending = int(input('Ending File Number: '))
		print("\n")

		GenerateForwardIndex.GenerateForwardIndex(starting,ending)

	elif choice == 3:
		print("\n")
		print("You Selected *Create Inverted Index*!")
		print("Enter The Following: ")
		print("\n")

		starting = int(input('Starting File Number: '))
		ending = int(input('Ending File Number: '))
		strstart=str(starting)
		strend=str(ending)
		
		userinput=strstart+","+strend
		range = userinput.split(',')
		print("\n")

		GenerateInvertedIndex.GenerateInvertedIndex(range)

