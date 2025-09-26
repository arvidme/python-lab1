def tokenize(lines):
	words = []
	for line in lines:
		start = 0
		line = line.lower()
		while start < len(line):
			end = start
			if line[start].isalpha():
				while end < len(line) and line[end].isalpha():
					end += 1
				words.append(line[start:end])
				start = end

			elif line[start].isdigit():
				while end < len(line) and line[end].isdigit():
					end += 1
				words.append(line[start:end])
				start = end

			elif line[start].isspace():
				start += 1
			else:
				words.append(line[start])
				start += 1
	return(words)


def countWords(words, stopWords):

	stopWords = stopWords.readlines()
	for i, stopword in enumerate(stopWords):
		stopWords[i] = stopword.strip()

	count = {}
	for word in words:
		if word not in stopWords:
			if word not in count:
				count[word] = 1
			else:
				count[word] += 1
	return count


def printTopMost(frequencies,n):

	sortedW = sorted(frequencies.items(), key=lambda x: (-x[1], x[0]))[:n]
	count = 0
	for word,freq in sortedW:
		print(word.ljust(20) + str(freq).rjust(5))
