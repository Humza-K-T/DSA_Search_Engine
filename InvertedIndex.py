
import pickle
import os
import ntpath
from tqdm import tqdm

from ProjectConfiguration import FORWARDINDEXPATH

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
        """
        parameters: forward_index_path - The path to the forward index
        that needs to be inverted.

        Invert this forward index and store it in self.temp_path. If a bucket
        already exists there don't over write it.

        return: void

        This method expects to be called by multiple threads.
        """
        with open(ForwardIndexPath, 'rb') as forward_index_file:
            forward_index = pickle.load(forward_index_file)
            inverted_indexes = [{} for i in range(self.lexiconsize // self.barrelsize + 1)]

            for document in tqdm(forward_index):
                for word_id in forward_index[document]:

                    # Find concerned barrel
                    barrel_index = word_id // self.barrelsize

                    # inverted_indexes[barrel_index][word_id][document] = forward_index[document][word_id]

                    if word_id in inverted_indexes[barrel_index]:
                        inverted_indexes[barrel_index][word_id][document] = forward_index[document][word_id]
                        # inverted_indexes[barrel_index][word_id].append({document: forward_index[document][word_id]})
                    else:
                        inverted_indexes[barrel_index][word_id] = { document: forward_index[document][word_id] }
                        # inverted_indexes[barrel_index][word_id] = [{document: forward_index[document][word_id]}]

            # Saving inverted index barrels which are not empty
            for i, inverted_index_barrel in enumerate(inverted_indexes):
                if not len(inverted_index_barrel) == 0:
                    filename = os.path.join(self.temppath, f"{i:03}_inverted_{ntpath.basename(ForwardIndexPath)}")
                    with open(filename, 'wb+') as inverted_index_file:
                        pickle.dump(inverted_index_barrel, inverted_index_file)

        # return filename

    #end of function
    

    #start of function
    #fun merge takes self instance
    #returns nothing

    def MergeIndex(self):

        """
        Merge the temporary inverted indexes in self.temp_path with
        the inverted index in self.path and save them.

        This function expects to be called by the main thread.
        """
        temp_inverted_indexes = os.listdir(self.temppath)

        for i in range(self.lexiconsize // self.barrelsize + 1):
            concerned_indexes = [temp_index for temp_index in temp_inverted_indexes if temp_index.startswith(f"{i:03}_inverted_")]
            
            # If for i'th barrel no temp indexes exist continue
            if not len(concerned_indexes): continue

            # Open barrel
            filename = os.path.join(self.path, f"{i:03}_inverted")
            inverted_index = {}
            if os.path.exists(filename):
                with open(filename, 'rb') as inverted_index_file:
                    inverted_index = pickle.load(inverted_index_file)

            # For each temp index, append its content to main barrel
            for concerned_index in concerned_indexes:
                with open(os.path.join(self.temppath, concerned_index), 'rb') as temp_index_file:
                    temp_index = pickle.load(temp_index_file)
                    for word_id in temp_index:
                        # TODO: What if temp_index[word_id] i.e. that document and its hit list already exists?? 
                        if word_id in inverted_index:
                            inverted_index[word_id].update(temp_index[word_id])
                        else:
                            inverted_index[word_id] = temp_index[word_id]

                # Delete temp index
                os.remove(os.path.join(self.temppath, concerned_index))
            
            # Save updated index
            with open (filename, 'wb') as inverted_index_file:
                pickle.dump(inverted_index, inverted_index_file)
                
   #end of function


    #start of function
    #fun retrive takes self instance & wordid
    #returns if condition satisfied            

    def retrieve(self, word_id):
        """
        parameters: word_id - Word id for which to return inverted_index

        return: list of documents and the hitlists for that word_id
        """

        # Find concerned barrel
        # TODO: What if barrel does not exist
        barrel_index = word_id // self.barrelsize
        filename = os.path.join(self.path, f"{barrel_index:03}_inverted")

        with open(filename, 'rb') as inverted_index_file:
            inverted_index = pickle.load(inverted_index_file)

            if word_id in inverted_index:
                return inverted_index[word_id]

        return None

    #end of function