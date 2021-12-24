'''

AUTHOR- HARSH SINGHANIA

ASSIGNMENT 3: "TAKING 3 NUMBERS FROM USER AND PRINTING THE LARGEST AMONGST THEM". CREATED A FUNCTION CALLED MAXOFTHREE TO DETERMINE LARGEST VALUE.
USING IF/ELSE STATEMENTS FOR COMPARING NUMBERS.

CWID- 20007289

'''
import sys

def MaxOfThree(a,b,c) -> None:
    """This function compares the 3 numbers and prints the largest using IF/ELSE statements."""
    if a>b and a>c:
        print ("\nLargest number amongst {} {} {} is {}".format(a,b,c,a))
    elif b>c and b>a:
        print ("\nLargest number amongst {} {} {} is {}".format(a,b,c,b))
    else:
        print ("\nLargest number amongst {} {} {} is {}".format(a,b,c,c))
        
while True:
    try:
        a: int = int(input("Enter number: "))
        b: int = int(input("Enter number: "))
        c: int = int(input("Enter number: "))
        MaxOfThree(a,b,c)
        break
    except ValueError:
        print("INVALID INPUT. Please enter integers values ONLY.")
