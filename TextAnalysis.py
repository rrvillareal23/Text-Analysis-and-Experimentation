
import os
import nltk
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords
from time import sleep
from prettytable import PrettyTable

# Download the 'stopwords' and 'punkt' resources
nltk.download('stopwords')
nltk.download('punkt')

stopSet = set(stopwords.words('english'))

class classNLTKQuery:
    ''' NLTK Query Class '''
    def __init__(self):
        self.transcript_file = open("transcript.txt", "w")  # Open a file for writing

    def textCorpusInit(self):
        thePath = os.getcwd()  # Use the current working directory
        try:
            self.Corpus = PlaintextCorpusReader(thePath, '.*\.txt')
            self.write_to_transcript("Processing Files : ")
            self.write_to_transcript(str(self.Corpus.fileids()))
            self.write_to_transcript("Please wait ...")
            self.rawText = self.Corpus.raw()
            self.tokens = nltk.word_tokenize(self.rawText)
            self.TextCorpus = nltk.Text(self.tokens)
        except Exception as e:
            self.write_to_transcript(f"Error in textCorpusInit: {e}")
            return "Corpus Creation Failed"

        self.ActiveTextCorpus = True

        return "Success"

    def write_to_transcript(self, text):
        print(text)
        self.transcript_file.write(text + "\n")

    def printCorpusLength(self):
        self.write_to_transcript("\n\nCorpus Text Length: " + '{:,}'.format(len(self.rawText)))

    def printTokensFound(self):
        self.write_to_transcript("\n\nTokens Found: " + '{:,}'.format(len(self.tokens)))

    def printVocabSize(self):
        vocab_size = len(set(self.tokens))
        self.write_to_transcript("\n\nVocabulary Size: " + str(vocab_size))

    def printCollocation(self):
        self.write_to_transcript("\n\nCompiling Top 100 Collocations ...")

    def searchWordOccurrence(self):
        test_words = ['GLOVE', 'GUN', 'BRONCO', 'BLOOD', 'GUILTY']
        self.write_to_transcript("\n\nOccurrences of Specific Test Words:")
        for word in test_words:
            occurrences = self.tokens.count(word)
            self.write_to_transcript(f"Occurrences of '{word}': {occurrences}")

    def generateConcordance(self):
        test_words = ['GLOVE', 'GUN', 'BRONCO', 'BLOOD', 'GUILTY']
        self.write_to_transcript("\n\nConcordance for Specific Test Words:")
        for word in test_words:
            self.write_to_transcript(f"Concordance for '{word}':")
            self.TextCorpus.concordance(word, width=80, lines=100)

    def generateSimilarities(self):
        seed_word = 'GLOVE'
        self.write_to_transcript(f"\n\nSimilarities for Specific Test Words (using '{seed_word}' as seed):")
        for word in ['GLOVE', 'GUN', 'BRONCO', 'BLOOD', 'GUILTY']:
            if word != seed_word:
                self.write_to_transcript(f"Similarities between '{seed_word}' and '{word}':")
                self.TextCorpus.similar(word)

    def printWordIndex(self):
        test_words = ['GLOVE', 'GUN', 'BRONCO', 'BLOOD', 'GUILTY']
        self.write_to_transcript("\n\nWord Index for Specific Test Words:")
        for word in test_words:
            try:
                index = self.tokens.index(word)
                self.write_to_transcript(f"Word Index of '{word}': {index}")
            except ValueError:
                self.write_to_transcript(f"Word '{word}' not found in the corpus.")

    def printVocabulary(self):
        self.write_to_transcript("\n\nCompiling Vocabulary Frequencies")
        tbl = PrettyTable(["Vocabulary", "Occurs"])
        word_freq = nltk.FreqDist(self.tokens)
        for word, freq in word_freq.items():
            tbl.add_row([word, freq])
        self.write_to_transcript(str(tbl))

    def printMenu(self):
        self.write_to_transcript("==========NLTK Query Options =========")
        self.write_to_transcript("[1]    Print Length of Corpus")
        self.write_to_transcript("[2]    Print Number of Token Found")
        self.write_to_transcript("[3]    Print Vocabulary Size")
        self.write_to_transcript("[4]    Search for Word Occurrence")
        self.write_to_transcript("[5]    Generate Concordance")
        self.write_to_transcript("[6]    Generate Similarities")
        self.write_to_transcript("[7]    Print Word Index")
        self.write_to_transcript("[8]    Print Vocabulary")
        self.write_to_transcript("\n[0]    Exit NLTK Experimentation\n")
        self.write_to_transcript('Enter Selection (0-8) >> ')

    def getUserSelection(self):
        self.printMenu()
        while True:
            try:
                sel = input()
                menuSelection = int(sel)
            except ValueError:
                self.write_to_transcript('Invalid input. Enter a value between 0-8.')
                continue

            if not menuSelection in range(0, 9):
                self.write_to_transcript('Invalid input. Enter a value between 0 - 8.')
                continue

            return menuSelection

    def close_transcript(self):
        self.transcript_file.close()

if __name__ == '__main__':
    oNLTK = classNLTKQuery()
    result = oNLTK.textCorpusInit()

    if result == "Success":
        menuSelection = -1
        while menuSelection != 0:
            if menuSelection != -1:
                oNLTK.printMenu()
                oNLTK.write_to_transcript("\n")
                oNLTK.write_to_transcript('==========NLTK Query Options =========')
                oNLTK.write_to_transcript('Enter Selection (0-8) >> ')

            menuSelection = oNLTK.getUserSelection()

            if menuSelection == 1:
                oNLTK.printCorpusLength()

            elif menuSelection == 2:
                oNLTK.printTokensFound()

            elif menuSelection == 3:
                oNLTK.printVocabSize()

            elif menuSelection == 4:
                oNLTK.searchWordOccurrence()

            elif menuSelection == 5:
                oNLTK.generateConcordance()

            elif menuSelection == 6:
                oNLTK.generateSimilarities()

            elif menuSelection == 7:
                oNLTK.printWordIndex()

            elif menuSelection == 8:
                oNLTK.printVocabulary()

            elif menuSelection == 0:
                oNLTK.write_to_transcript("Goodbye\n")

            elif menuSelection == -1:
                continue

            else:
                oNLTK.write_to_transcript("Unexpected error condition")
                menuSelection = 0

            sleep(3)

        oNLTK.close_transcript()

    else:
        oNLTK.write_to_transcript("Closing NLTK Query Experimentation")