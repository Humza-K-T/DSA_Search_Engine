

class Search:
	"""Perfoms search operations"""

	#constructor
	#takes 3 args,takes self instance, lexicon  & inverted index.
	def __init__(self, lexicon, invertedindex):
		"""Constructor, takes self instance, lexicon  & inverted index."""
		self.lexicon = lexicon
		self.invertedindex = invertedindex

	#end of constructor

	#function seearch
	#takes 3 args, self instance, query & maxwords

	def search(self, query, n=10):

		wordids = [self.lexicon.SearchWordId(word) for word in self.lexicon.CreateTokens(query)]
		searchinvertedindex = [self.invertedindex.retrieve(wordid) for wordid in wordids if wordid != -1]

		#creating empty dictionary
		search = []

		#checking if length is 0 or not, if zero or null, returning dictionary
		if len(searchinvertedindex)==0 or searchinvertedindex[0] == None: return search
		for i, enuminverind in enumerate(searchinvertedindex):
			for document in enuminverind:
				hitlist = [enuminverind[document]]
				for remaininginvertedindex in searchinvertedindex[i + 1:]:
					if not(document  == None) and (document in remaininginvertedindex):
						hitlist.append(remaininginvertedindex[document])
						del remaininginvertedindex[document]
				
				search.append((document, self.HitlistScore(hitlist)))

		sorted(search, key=lambda x: x[1])
		search.sort(key=lambda x: x[1], reverse=True)

		return search[:n]


	def HitlistScore(self, hitlists):
		""" Looks for hitlists, takes sef & hitlists, check how many times word appears"""
		hitlistscore = 0

		number = len(hitlists)
		hitlistlength = [len(hitlist) for hitlist in hitlists]
		hitlist= [0] * number

		#empty dictionary
		merged= []

		while hitlist != hitlistlength:
			#empty dictionary
			position = []
			source = []

			for i in range(number):
				if hitlist[i] == len(hitlists[i]): continue
				position.append(hitlists[i][hitlist[i]])
				source.append(i)

			minimum = min(position)
			minind = position.index(minimum)
			hitlist[source[minind]] += 1

			#merging
			merged.append((minind, minimum))

		lasthit = merged[0]

		#if hits, increment
		for hit in merged[1:]:
			hitlistscore += 1
			if hit[0] != lasthit[0]: 
				dist = hit[1] - lasthit[1]
				hitlistscore += 100 / (dist + 1)
			lasthit = hit

		#returnig score
		return hitlistscore
		

