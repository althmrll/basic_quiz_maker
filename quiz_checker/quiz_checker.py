import os

#DEFINITIONS
def center(center_text):
    screen_size=os.get_terminal_size().columns
    return center_text.center(screen_size)

#FIXED VARIABLES
program_title="QUIZ CHECKER"
opening_message="\n\nThis program is used so you can answer the quiz you just created. You can also use this so other people can answer your created quiz. Press 'ENTER' to choose which quiz you want to answer.\n\n"
centered_title=center(program_title)

#QUIZ CHECKER
print(centered_title)
print(opening_message)
#Ask user the quiz they want to answer (use pop-up?)
#Print one question with choices for user to answer
#Make user press 'submit' (or enter) button
#After submitting, show user the correct answer
#Add 1 to number of corrects (if correct) and the number of questions answered over the total number of questions.
#Flash ending message, positive if passed, negative if failed. (try adding multiple ending mesages done at random)
#Add choice wether to exit the program or answer another quiz.