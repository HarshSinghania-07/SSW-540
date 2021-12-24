"""

Author: Harsh Singhania
CWID - 20007289
SSW 540
P8 - Classic Books
There are 4 parts to this assignment: 
1 - Total words
2 - Total distinct words
3 - The top 25 most frequent words and counts (You do NOT need to handle ties.  Just pick the top 25)
4 - Character frequency sorted from most frequent to least frequent characters

"""

import os
import sys
import string

print ("-----Program to provide the summary of text file------")
def getDictionary(fileContent):
    wordsDict = dict()
    for word in fileContent:
        wordsDict[word] = wordsDict.get(word, 0) + 1
    return wordsDict

def getDictSortedWithValues(wordsDict):
    wordList = list()
    for key, value in wordsDict.items():
        wordList.append((value, key))
    wordList.sort(reverse=True)
    return wordList

def getCountofAllWords(fileContent):
    print ("\nTotal number of words in file: ", len(fileContent))

def getCountofDistinctWords(fileContent):
    wordsDict = getDictionary(fileContent)
    print ("\nTotal number of distinct words in file: ", len(wordsDict))

def getTo25FrequentWords(fileContent):
    wordsDict = getDictionary(fileContent)
    wordList = getDictSortedWithValues(wordsDict)
    print ("\nTop 25 most frequesnt words are: ")
    for value, key in wordList[:25]:
        print (key, value)

def getCharacterFrequency(fileContent):
    charDict = dict()
    fileStr = ''.join(fileContent)
    for i in range(0, len(fileStr)):
        char = fileStr[i]
        if str.isalpha(char):
            charDict[char] = charDict.get(char, 0) + 1
    charDict = getDictSortedWithValues(charDict)
    print ("\nCharacter frequency in descending order: ")
    for value, key in charDict:
        print (key, value)

fileName = input("Enter the file name: ")
try:
    fHandle = open(fileName, 'r')
    strFile = fHandle.read()
except IOError:
    print ("Error: can\'t find file or read data")
    sys.exit()

if os.stat(fileName).st_size != 0:  
    fileContent = strFile.translate(string.punctuation).lower().split()
    getCountofAllWords(fileContent)
    getCountofDistinctWords(fileContent)
    getTo25FrequentWords(fileContent)
    getCharacterFrequency(fileContent)
else:
    print ("Oops!!!This file is empty")