import pickle
import os
import ntpath
from tqdm import tqdm

class InvertedIndex:

    #start of function
    #acts as constructor
    #fun init, takes self,path,temppath,barrelsize,lexiconsize

    def __init__(self, path, temporarypath, sizeoflexicon, sizeofbarrel):

        self.path = path
        self.temppath = temporarypath
        self.lexiconsize = sizeoflexicon
        self.barrelsize = sizeofbarrel

    #end of constructor


    #start of function
    #fun CreateForwardIndex, takes self instance, document path & name of file
    #returns name of file

    def CreateInvertedIndex(self, ForwardIndexPath):
       
        with open(ForwardIndexPath, 'rb') as ForwardIndexData1:

            ForInd1 = pickle.load(ForwardIndexData1)
            InvInd1 = [{} for i in range(self.lexiconsize // self.barrelsize + 1)]

            for document in tqdm(ForInd1):
                for word_id in ForInd1[document]:

                    BarInd1 = word_id // self.barrelsize

                    if word_id in InvInd1[BarInd1]:
                       InvInd1[BarInd1][word_id][document] = ForInd1[document][word_id]
                    else:
                        InvInd1[BarInd1][word_id] = { document: ForInd1[document][word_id] }
     
            for i, InvIndBar in enumerate(InvInd1):
                if not len(InvIndBar) == 0:
                    filename = os.path.join(self.temppath, f"{i:03}_inverted_{ntpath.basename(ForwardIndexPath)}")

                    with open(filename, 'wb+') as InvertedIndexData:
                        pickle.dump(InvIndBar, InvertedIndexData)

        #returning
        return filename

    #end of function
    

    #start of function
    #fun merge takes self instance
    #returns nothing

    def MergeIndex(self):

        InvIndTemp = os.listdir(self.temppath)

        for i in range(self.lexiconsize // self.barrelsize + 1):
            concerned_indexes = [temp_index for temp_index in InvIndTemp if temp_index.startswith(f"{i:003}_inverted")]
            
            if not len(concerned_indexes):
                continue

            filename = os.path.join(self.path, f"{i:003}_inverted")

            #creating empty dictionary
            InvInd2 = {}
            
            if os.path.exists(filename):
                if os.path.getsize(filename)>0 :  
                    with open(filename, 'rb') as InvertedIndexData2:
                        InvInd2 = pickle.load( InvertedIndexData2)


            #iterating through each
            for concerned_index in concerned_indexes:
                with open(os.path.join(self.temppath , concerned_index), 'rb') as TemporaryIndexData:
                    TempInd = pickle.load(TemporaryIndexData)

                    #iterating through each
                    for word_id in TempInd:

                        if word_id in InvInd2:
                            InvInd2[word_id].update(TempInd[word_id])
                        else:
                            InvInd2[word_id] = TempInd[word_id]


                os.remove(os.path.join(self.temppath, concerned_index))
            
            with open (filename, 'wb') as InvertedIndexData3:
                pickle.dump( InvInd2, InvertedIndexData3)

    #end of function


    #start of function
    #fun retrive takes self instance & wordid
    #returns if condition satisfied            

    def retrieve(self, wordid):

        BarInd2 = wordid // self.barrelsize
        filename = os.path.join(self.path, f"{BarInd2:003}_inverted")

        with open(filename, 'rb') as InvertedIndexData4:
            InvInd3 = pickle.load(InvertedIndexData4)

            if wordid in InvInd3:
                return InvInd3[wordid]

        return None

    #end of function