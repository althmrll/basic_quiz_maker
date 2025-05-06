#QUIZ MAKER
#Imports
import tkinter as tk_module
from tkinter import filedialog
import time

#Definitions
def choose_file():
    global chosen_file
    quiz_checker_window.withdraw()  # Hide the main window
    chosen_file = filedialog.askopenfilename()
    if chosen_file:
        confirm_chosen_file

    else:
        no_file_chosen = tk_module.Toplevel()
        no_file_chosen.geometry("300x200") 
        exit_text= tk_module.Label(no_file_chosen, text='No file Chosen, exiting the program') #Confirm user's chosen file
        exit_text.pack()
        time.sleep(2)
        no_file_chosen.withdraw

#Confirm File
def confirm_chosen_file():
    confirm_chosen_file = tk_module.Toplevel()
    confirm_chosen_file.title("Confirm Chosen File")
    confirm_chosen_file.geometry("300x200") 
    printed_text= tk_module.Label(confirm_chosen_file, text="Chosen file:"+chosen_file) #Confirm user's chosen file
    printed_text.pack()
    confirm_button = tk_module.Button(quiz_checker_window, text="Confirm", command=main_quiz)
    confirm_button.pack()
    confirm_chosen_file.mainloop()

def main_quiz():
    file = open(chosen_file,'r')


#Main Program
quiz_checker_window = tk_module.Tk()
quiz_checker_window.title("Quiz Checker")
quiz_checker_window.geometry("600x400") 
menu_content = tk_module.Label(quiz_checker_window, text="QUIZ CHECKER\nThis quiz checker was made so you can answer the quiz" \
"you created using basic quiz maker. To start click 'CHOOSE FILE' button below.") #Ask user the quiz they want to answer.
menu_content.pack()

choose_quiz_button = tk_module.Button(quiz_checker_window, text="Choose Quiz", command=choose_file)
choose_quiz_button.pack()

quiz_checker_window.mainloop()
#Print one question with choices for user to answer
#Make user press 'submit' (or enter) button.
#After submitting, show user the correct answer
#Add 1 to number of corrects (if correct) and the number of questions answered over the total number of questions.
#Flash ending message, positive if passed, negative if failed. (try adding multiple ending mesages done at random)
#Add choice wether to exit the program or answer another quiz.