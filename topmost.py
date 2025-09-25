import sys
import wordfreq
def main():
	stopwords = sys.argv[1]
	data = sys.argv[2]
	count = sys.argv[3]

	result = wordfreq.tokenize(data)
	words = wordfreq.countWords(result, stopwords)
	wordfreq.printTopMost(words, count)

if __name__ == "__main__":
	main()
	


