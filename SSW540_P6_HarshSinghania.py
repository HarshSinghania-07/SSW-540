'''
Author - Harsh Singhania
CWID - 20007289
SSW 540 - P6
Slices and Dices

'''
from typing import List
def average(numbers: float) -> float:
    """Function for calculating the average."""
    return sum(numbers) / len(numbers)
try:
    string: str = input('Enter the file name (include path if file is outside directory): ')
except EOFError:
    print('EOF command given. Quitting...bye!')
    exit()
except:
    print('This input is invalid! Please try again.')
    exit()
try:
    file = open(string)
except FileNotFoundError:
    print('This file does not exist in the directory:', string)
    exit()
except:
    print('An error occurred opening this file! Please try again.')
    exit()

items: List = []
for line in file:
    line = line.rstrip()
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    line = line.split(':')[1]
    try:
        number: float = float(line)
        items.append(number)
    except:
        print('Bad data was detected! Please check your file and try again.')
        exit()
if len(items) == 0:
    print('The program did not find any matching lines! Please check your file and try again.')
    exit()
output = average(items)
output = round(output, 4)

print(f'Average spam confidence: {output}...')