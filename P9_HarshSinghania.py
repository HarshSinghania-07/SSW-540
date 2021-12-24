'''
Author - Harsh Singhania
SSW 540 - P9: Regular Expression
CWID - 20007289

Writing a python script using regular expression to find all the capitalized words in a given file. Handling exceptions for no capitalized words present in the file or the file 
mentioned doesn't exist.

'''
import re 

def capWords(fileTxt):
    """FUNCTION TO FIND ALL CAPITALIZED WORDS FROM THE FILE INPUT. MAKING USE OF YIELD FOR EXTRACTING WORDS."""
    for word in fileTxt:
        p = re.compile(r'[A-Z][a-z]*') 
        yield from p.findall(word) 

try:
    """HANDLING ALL EXCEPTIONS MENTIONED IN THE PROBLEM STATEMENT. IF THE FILE NAME MENTIONED IS WRONG.
       ALSO, IF THERE ARE NO CAPITALIZED WORDS PRESENT IN THE FILE."""
    file = open(input("Enter file name:"))
    upperWord = list(capWords(file))
    if len(upperWord) == 0:
        print("Sorry. No capitalized words were found in this file.") 
    else:
        print(sorted(upperWord)) 
except IOError:
    print("The file name entered is invalid or does not exist.")
