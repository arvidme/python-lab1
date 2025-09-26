import sys
import wordfreq

def main():
	stopwords = open(sys.argv[1])
	data = open(sys.argv[2])
	count = int(sys.argv[3])

	result = wordfreq.tokenize(data)
	words = wordfreq.countWords(result, stopwords)
	wordfreq.printTopMost(words, count)

	stopwords.close()
	data.close()


if __name__ == "__main__":
	main()
	


