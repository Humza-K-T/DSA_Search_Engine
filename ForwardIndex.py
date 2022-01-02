import json
import ntpath
import os
import nltk
import re
import pickle
from tqdm import tqdm

class ForwardIndex:
    """ForwardIndex = { Article1: [wordId <HitList>,....] Article2: [wordId <HitList>],...}"""

    #Creating object for removing stopwords, i.e.,the,an,a....
    GlobalStopwords = set(nltk.corpus.stopwords.words('english'))

    #Creating object for removing stemmer,converting words to root forms i.e., quickly->quick...
    GlobalStemmer = nltk.stem.PorterStemmer()


    #start of function
    #acts as constructor
    #fun init, takes self instance, path & lexicon

    def __init__(self, path, lexicon):
        """Gets path of forward index docs & gets lexicon"""
        self.path = path
        self.lexicon = lexicon

    #end of constructor


    #start of function
    #fun CreateForwardIndex, takes self instance, document path & name of file
    #returns path

    def AddForwardIndex(self, documentpaths, filename):
        """Takes 3 arguments. Adds words with hitlists. Function is to go through each file & stemmerize words + remove punctuations
            & URLs. Serialzes the files & dumps them. Takes self instance, document path & filename. Uses dictionaries """
        
        #creating empty dictionary
        ForwardIndexDictionary= {}
       
        #try block
        DocHistory={}
        DocHistoryPath=self.path+ "\\Doclist"

        #looking for fies, opening them, loading & serializing them and then closing
        try:
            if os.path.getsize(DocHistoryPath) > 0:
                OpenFile1 = open(DocHistoryPath , 'rb')
                DocHistory = pickle.load(OpenFile1)
                OpenFile1.close()

        #catch block    
        except IOError:
            
            with open(DocHistoryPath, 'wb') as file:

                #dumping file
                pickle.dump(DocHistory, file)

            #closing file

        #if change detected
        change=False
        for path in tqdm(documentpaths):

            if path not in DocHistory:
                change=True
                 
                with open(path, encoding="utf8") as newjson:
                    #getting file content in variable
                    document = json.load(newjson)
                    DocHistory[path]=1

                DocumentId = os.path.splitext(ntpath.basename(path))[0]

                words= document['content']
                token = re.sub('[^A-Za-z]', " ", words).split()

                #Removing Punctuations
                #Removing URL's
                #Stemming words
                #simply tokenizing

                token = [re.sub(r'^https?:\/\/.*[\r\n]*', '', x, flags=re.MULTILINE) for x in token]
                token = [re.sub(r'[^A-Za-z]+', '', x) for x in token]
                token = [x for x in token if not x in self.GlobalStopwords]
                token = [self.GlobalStemmer.stem(x) for x in token]

                #creating empty dictionary
                WordId = {}

                #creating variable for word position
                #by default posiion is set to one
                position = 1

                #iterating through each word in tokenized
                for word in token:
                    #if word not a space/empty & exists in lexicon, look for word in lexicon,get its id
                    if word != '' and self.lexicon.Exist(word):
                        key = self.lexicon.SearchWordId(word)
                        if key in WordId:
                            WordId[key].append(position)
                        else:
                            WordId[key] = [position]

                        #incrementing position
                        position = position + 1

                    ForwardIndexDictionary[DocumentId] = WordId

        #dumping file

        #if change detected opening file & dumping it
        path = os.path.join(self.path, filename)
        if(change):
            # path = os.path.join(self.path, filename)
            with open(path, 'wb') as file:
                pickle.dump(ForwardIndexDictionary, file)

            with open(DocHistoryPath, 'wb') as file:
                pickle.dump(DocHistory, file)

        #returning
        return path

        