def tokenize(lines):

	words = []

	for line in lines:

		start = 0
		while start < len(line):

			while line[start].isspace():
				start = start + 1

			end = start
			if line[start].isalpha():
				while line[end].isalpha():
					end += 1

			elif line[start].isdigit():
				while line[end].isdigit():
					end += 1

			words.append(line[start:end])
			start = end
			start += 1
	return words

# def countWords(words, stopWords):
# 	pass
#
# def printTopMost(frequencies, n):
# 	pass


# def tokenize(lines):
#
# 	words = []
#
# 	for line in lines:
#
# 		start = 0
# 		while start < len(line):
#
# 			while line[start].isspace():
# 				start = start + 1
#
# 			if(line[start].isalpha()):
# 				print(f"{line[start]} is a letter")
#
# 			elif(line[start].isdigit()):
# 				print(f"{line[start]} is a digit")
#
# 			else:
# 				print(f"{line[start]} is a symbol")
# 			start = start + 1
# 	return words
