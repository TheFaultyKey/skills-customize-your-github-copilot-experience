# 📘 Assignment: Python Text Processing

## 🎯 Objective

Students will practice string manipulation, file I/O, and basic text analysis in Python by building utilities to clean and analyze plain text files.

## 📝 Tasks

### 🛠️ Read and Clean Text File

#### Description
Write a function that reads a text file, normalizes whitespace, converts text to lowercase, and removes punctuation.

#### Requirements
Completed program should:

- Read an input text file specified by the user
- Normalize whitespace and convert to lowercase
- Remove punctuation characters
- Save the cleaned text to an output file

### 🛠️ Compute Word Frequencies

#### Description
Analyze the cleaned text to compute the frequency of each word and output the top N most frequent words.

#### Requirements
Completed program should:

- Count occurrences of each word in the cleaned text
- Allow the user to request the top N most common words
- Print and save the results in a readable format (CSV or plain text)

## 📦 Starter Files

- `starter-code.py` — a starter script with helpers and an entry point

## 📤 Deliverables

- A working Python script that performs the tasks above
- A short README explaining how to run the script and sample output

## ✅ How to run

1. Place a `.txt` file in the same folder (or provide a path).
2. Run:

```
python3 starter-code.py input.txt cleaned.txt --top 10
```

The script will produce `cleaned.txt` and print the top 10 words with counts.

## 🔢 Learning Outcomes

- Practice reading and writing files in Python
- Learn common string operations and text normalization
- Perform basic frequency analysis and produce simple reports
