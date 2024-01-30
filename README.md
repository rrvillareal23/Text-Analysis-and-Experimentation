# NLTK Text Analysis and Experimentation

This repository contains a Python script that utilizes the Natural Language Toolkit (NLTK) for text analysis and experimentation. The script provides an interactive interface for exploring various aspects of a given text corpus, including corpus length, token count, vocabulary size, word occurrences, concordance, similarities, word index, and vocabulary frequencies.

## Features

1. **Text Corpus Initialization:**
   - The script initializes a text corpus using NLTK's capabilities, reading text files from the current working directory.

2. **Text Analysis Options:**
   - Users can interactively choose from a menu of options to perform different analyses on the text corpus.

3. **Analysis Functions:**
   - The script offers functions to print the length of the corpus, the number of tokens found, vocabulary size, occurrences of specific words, concordance for specific words, similarities between words, word index for specific words, and vocabulary frequencies.

4. **Interactive Menu:**
   - Users are presented with an interactive menu to select the type of analysis they want to perform.

5. **Transcript Logging:**
   - The script logs the analysis results into a 'transcript.txt' file, providing a record of the performed analyses.

6. **Graceful Exit:**
   - Users can exit the experimentation at any time, and the script closes the transcript file.

## Dependencies

- **NLTK:** Natural Language Toolkit for natural language processing.
- **PrettyTable:** Used for creating well-formatted tables for displaying vocabulary frequencies.

## Usage Instructions

1. Ensure NLTK and PrettyTable libraries are installed (`pip install nltk prettytable`).
2. Run the script, and it will guide you through various options for analyzing the provided text corpus.
3. Explore corpus length, token count, vocabulary size, and other linguistic aspects interactively.
4. Results are logged in 'transcript.txt' for reference.

**Note:** This script is designed for experimentation and exploration of text data using NLTK. It provides insights into the structure and characteristics of the given corpus.
