import os
import tkinter as tk_module
from tkinter import filedialog

#DEFINITIONS
def center(center_text):
    screen_size=os.get_terminal_size().columns
    return center_text.center(screen_size)

def start_program():
    start=input("")
    while True:
        if start == "":
            choose_file()
        else: 
            start=input("Press 'ENTER' to start the game.")

def choose_file():
    chosen_file = filedialog.askopenfilename()
    if chosen_file:
        print("hehe")

#FIXED VARIABLES
program_title="QUIZ CHECKER"
opening_message="\nThis program is used so you can answer the quiz you just created. You can also use this so other people can answer your created quiz. Press 'ENTER' to choose which quiz you want to answer."
centered_title=center(program_title)

#QUIZ CHECKER (main program)
print(centered_title)
print(opening_message)
start_program()

#Print one question with choices for user to answer
#Make user press 'submit' (or enter) button
#After submitting, show user the correct answer
#Add 1 to number of corrects (if correct) and the number of questions answered over the total number of questions.
#Flash ending message, positive if passed, negative if failed. (try adding multiple ending mesages done at random)
#Add choice wether to exit the program or answer another quiz.