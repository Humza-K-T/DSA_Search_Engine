import os

PROJECTPATH = os.getcwd()

INPUTPATH= os.path.join(PROJECTPATH, "Dataset")
OUTPUTPATH = os.path.join(PROJECTPATH, "Output")
UPDATED_JSONS=os.path.join(OUTPUTPATH,"UpdatedJsons")


LEXICONPATH = os.path.join(PROJECTPATH, "Output/Lexicon/Lexicon")
FORWARDINDEXPATH = os.path.join(PROJECTPATH, "Output/ForwardIndex")
INVERTEDINDEXPATH = os.path.join(PROJECTPATH, "Output/InvertedIndex")
TEMPORARYINVERTEDINDEXPATH = os.path.join(PROJECTPATH, "Output/InvertedIndex/Temporary")

MAXIMUMSIZE = 512

def InputPath(start=None, end=None,useNewJsons=False):

    if (useNewJsons):
        for batch in os.listdir(UPDATED_JSONS)[start:end]:
            #for filepath in os.listdir(os.path.join(INPUTPATH, batch)):
                yield os.path.join(UPDATED_JSONS, batch)
    else:
            for batch in os.listdir(INPUTPATH)[start:end]:
            #for filepath in os.listdir(os.path.join(INPUTPATH, batch)):
                yield os.path.join(INPUTPATH, batch)