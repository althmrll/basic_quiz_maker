import os
import tkinter as tk_module
from tkinter import filedialog

#DEFINITIONS
def center(center_text):
    screen_size=os.get_terminal_size().columns
    return center_text.center(screen_size)

def choose_file():
    chosen_file = filedialog.askopenfilename()
    if chosen_file:
        choose_file_window.withdraw
        file=open(chosen_file,"r")
        main_quiz()

def main_quiz():
    print("hehe")

#FIXED VARIABLES
program_title=""
opening_message=""
centered_title=center(program_title)

#QUIZ CHECKER (main program)
choose_file_window = tk_module.Tk()
choose_file_window.title("QUIZ CHECKER")
choose_file_window.geometry("600x400") 
opening_message = tk_module.Label(choose_file_window, text="QUIZ CHECKER\nThis program is used so you can answer the quiz you" \
"just created. You can also use this so other people can answer your created quiz. Click the button below to choose which" \
"quiz you want to answer.") #Ask user the quiz they want to answer.
opening_message.pack()

choose_quiz_button = tk_module.Button(choose_file_window, text="Choose Quiz", command=choose_file)
choose_quiz_button.pack()

#Print one question with choices for user to answer
#Make user press 'submit' (or enter) button
#After submitting, show user the correct answer
#Add 1 to number of corrects (if correct) and the number of questions answered over the total number of questions.
#Flash ending message, positive if passed, negative if failed. (try adding multiple ending mesages done at random)
#Add choice wether to exit the program or answer another quiz.