import sys
import wordfreq
import urllib.request 

def main():
	stopwords = open(sys.argv[1])
	stopword_lines = stopwords.readlines()

	response = urllib.request.urlopen(sys.argv[2])
	lines = response.read().decode("utf8").splitlines()

	count = int(sys.argv[3])

	result = wordfreq.tokenize(lines)
	words = wordfreq.countWords(result, stopword_lines)
	wordfreq.printTopMost(words, count)

	stopwords.close()
	response.close()

if __name__ == "__main__":
	main()
	


