import json
import ntpath
import os
import nltk
import re
import pickle
from tqdm import tqdm

class ForwardIndex:

    #Creating object for removing stopwords, i.e.,the,an,a....
    GlobalStopwords = set(nltk.corpus.stopwords.words('english'))

    #Creating object for removing stemmer,converting words to root forms i.e., quickly->quick...
    GlobalStemmer = nltk.stem.PorterStemmer()


    #start of function
    #acts as constructor
    #fun init, takes self instance, path & lexicon

    def __init__(self, path, lexicon):

        self.path = path

        self.lexicon = lexicon

    #end of constructor


    #start of function
    #fun CreateForwardIndex, takes self instance, document path & name of file
    #returns path

    def AddForwardIndex(self, documentpaths, filename):

        #creating empty dictionary
        ForwardIndexDictionary= {}
        
        
        #passing every path & opening file
        #try block
        DocHistory={}
        DocHistoryPath=self.path+ "\\Doclist"
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

        change=False
        for path in tqdm(documentpaths):

            if path not in DocHistory:
                change=True
                
                # with open(path, "rb") as OpenFile:
                #     document = pickle.load(OpenFile)
                #     DocHistory[path]=1  
                with open(path, encoding="utf8") as newjson:
                    document = json.load(newjson)
                    DocHistory[path]=1


                DocumentId = os.path.splitext(ntpath.basename(path))[0]

                words= document['content']

                # token = nltk.word_tokenize(document['content'])
                token = re.sub('[^A-Za-z]', " ", words).split()


                #Removing Punctuations
                #Removing URL's
                #RStemming words

                token = [re.sub(r'^https?:\/\/.*[\r\n]*', '', x, flags=re.MULTILINE) for x in token]
                token = [re.sub(r'[^A-Za-z]+', '', x) for x in token]
                token = [x for x in token if not x in self.GlobalStopwords]
                token = [self.GlobalStemmer.stem(x) for x in token]


                #creating empty dictionary
                WordId = {}

                #creating variable for word position
                position = 1

                #iterating through each word
                for word in token:
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

        path = os.path.join(self.path, filename)
        if(change):
            # path = os.path.join(self.path, filename)
            with open(path, 'wb') as file:
                pickle.dump(ForwardIndexDictionary, file)

            with open(DocHistoryPath, 'wb') as file:
                pickle.dump(DocHistory, file)

        #returning
        return path

        