'''
AUTHOR: HARSH SINGHANIA

P2- CONVERT NUMERIC SCORE TO GRADES. WE ASK THE USER FOR SCORE INPUT AND USING IF/ELSE STATEMENTS DETERMINE THE GRADE GIVEN IN THE PROBLEM STATEMENT.
ALSO USING TRY/EXCEPT FOR WHEN USER ENTERS A INVALID SCORE.

CWID- 20007289

'''

import sys 
while True:
    def Compute_Grade(score) -> None:
        """DEFINING THE GRADE SCALE FOR RESPECTIVE SCORES GIVEN BY THE USER."""
        if score>92 and score<101:
            print ("Your grade is A.")
        elif score<92 and score>89:
            print("Your grade is A-.")
        elif score<89 and score >86:
            print("Your grade is B+.")
        elif score<86 and score>82:
            print("Your grade is B.")
        elif score<82 and score>79:
            print("Your garde is B-.")
        elif score<79 and score>69:
            print("Your garde is C.")
        elif score<70 and score>0:
            print("Your grade is F.")
        else:
            print("Invalid score. Score range is 0-100. Please try again!")

    """USING TRY/EXCEPT BLOCK TO VERIFY IF THE SCORE ENTERED BY USER IS VALID. IF NOT WILL BE ASKED TO INPUT AGAIN."""
    try:
        score: float = float(input("Enter your score: "))
        Compute_Grade(score)
        break
    except ValueError as e:
        print("Not a valid score. Please enter again!")            