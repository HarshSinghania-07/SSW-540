"""
Author: Harsh Singhania
CWID - 20007289
SSW 540
P7 - Finding and counting unique items

"""
import re
from collections import Counter
from typing import List

def valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)
try:
    string = input('Enter the file name (include path if file is outside directory): ')
except EOFError:
    print('EOF command given. Quitting...bye!')
    exit()
except:
    print('This input is invalid! Please try again.')
    exit()
try:
    file = open(string)
except FileNotFoundError:
    print('File cannot be opened:', string)
    exit()
except:
    print('An error occurred opening this file! Please try again.')
    exit()

items = set()

for line in file:
    line = line.rstrip()
    if not line.startswith('From:'): continue
    try:
        line = line.split(': ')[1]
        if not valid_email(line):
            raise Exception('Malformed email detected!')
        items.add(line)
    except:
        print('Bad data was detected! Please check your file and try again.')
        exit()
if len(items) == 0:
    print('The program did not find any matching lines! Please check your file and try again.')
    exit()

output = len(items)
print(f'There are {output} unique senders in this file.')
# print(items)
print(Counter(items).keys())      # equals to list(set(words))
# print(Counter(items).values())    # counts the elements' frequency
