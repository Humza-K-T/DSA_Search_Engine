# Data Structures & Algorithms End Semester Project Fall-2021

# Group Members
    Humza Khawar 343114
    M. Huzaifa   332839


# About The Project
    Simple Python based web server to answer search queries.
    To set it up you need to install some python linraries(refer to setmeup.txt)
    Run RUNSERVER.PY and open (CTRL+CLICK) URL OR PASTE THIS(http://127.0.0.1:5000/)
    Before searching anything please make sure you have created lexicon/forward index/ inverted index
    Upload file option(bottom right) is given on search page


# Working
    Everythig starts with document uploadation.
    Soon after you upload document the lexicon, forward & inverted index are created.

# Lexicon   
    Lexicon is stored in dictionary

# Forward Index
    After lexicon generation, inverted index in created. As searching is done on inverted index, therefore while creating forward index we eliminated duplicates by creating buckets on docID. We have also included threading to make process faster.

# Inverted Index   
    For generating Inverted Index we again involved threading. The dataset is divided, multiple(2) threads are created and temporary inverted index is created,afterward we combine these temporay index. After combining temporary indexex are deleted. Information about hitlists canbe obtained from forward index.

# Search
    For searching enter the required word or phrase in text box, that word or phrase(if phrase divide in small words) is passed to inveretd index to get result.

# Frontend
    Frontend is mostly in HTML, CSS & JAVASCRIPT

# Backend
    Backend is in Python.