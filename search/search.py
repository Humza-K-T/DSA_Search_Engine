class Search:

	def __init__(self, lexicon, inverted_index):
		self.lexicon = lexicon
		self.inverted_index = inverted_index


	def search(self, query, n=10):

		search_word_ids = [self.lexicon.SearchWordId(word) for word in self.lexicon.CreateTokens(query)]
		inverted_index_entries = [self.inverted_index.retrieve(word_id) for word_id in search_word_ids if word_id != -1]

		docs_with_score = []
		if len(inverted_index_entries)==0 or inverted_index_entries[0] == None: return docs_with_score
		for i, iie in enumerate(inverted_index_entries):
			for doc in iie:
				current_doc_hitlists = [iie[doc]]
				for remaining_iie in inverted_index_entries[i + 1:]:
					if doc in remaining_iie:
						current_doc_hitlists.append(remaining_iie[doc])
						del remaining_iie[doc]
				
				docs_with_score.append((doc, self.query_relavence_score(current_doc_hitlists)))


		sorted(docs_with_score, key=lambda x: x[1])
		docs_with_score.sort(key=lambda x: x[1], reverse=True)

		return docs_with_score[:n]


	def query_relavence_score(self, hitlists):

		score = 0

		n = len(hitlists)
		hitlist_lens = [len(hitlist) for hitlist in hitlists]
		hitlist_is = [0] * n

		joined_hits = []

		while hitlist_is != hitlist_lens:
			terminal_positions = []
			taken_from = []

			for i in range(n):
				if hitlist_is[i] == len(hitlists[i]): continue
				terminal_positions.append(hitlists[i][hitlist_is[i]])
				taken_from.append(i)

			minimum = min(terminal_positions)
			minimum_index = terminal_positions.index(minimum)
			hitlist_is[taken_from[minimum_index]] += 1

			joined_hits.append((minimum_index, minimum))

		prev_hit = joined_hits[0]

		for hit in joined_hits[1:]:
			score += 1
			if hit[0] != prev_hit[0]: 
				dist = hit[1] - prev_hit[1]
				score += 100 / (dist + 1)
			prev_hit = hit

		return score
		

