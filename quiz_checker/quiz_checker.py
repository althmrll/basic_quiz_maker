import os
import tkinter as tk_module
from tkinter import filedialog
import random

#LIST
question_with_choice=[]
answer=[]

#DEFINITIONS
def center(center_text):
    screen_size=os.get_terminal_size().columns
    return center_text.center(screen_size)

def choose_file():
    global chosen_file
    chosen_file = filedialog.askopenfilename()
    if chosen_file:
        main_quiz()

def question_formatting():
    for line in file:
        line = file.readlines()
        if line == "\n":
            StopIteration
            print (line)
            continue

def ask_question():
        global question_and_answer_number
        question_and_answer_number=random.random(question_with_choice)
        print (question_with_choice[question_and_answer_number])#Print one random question with choices for user to answer
        input_answer

def input_answer():
    answer=input("Answer:")
    answer=answer.upper
    check_if_correct

def format_correct_Answer():
    find_word="Correct Answer:"
    for answer_line in chosen_file:
        if find_word in answer_line:
            correct_answer=answer_line.replace("Correct Answer:","")
            correct_answer=correct_answer.upper
            answer.append(correct_answer)

def check_if_correct():
    correct_answer=answer[question_and_answer_number]
    if answer==correct_answer:#After submitting, show user the correct answer
        print("You are correct!")
    else:
        print("Wrong, Correct asnwer is", correct_answer)

def main_quiz():
    global file
    choose_file_window.withdraw()
    file=open(chosen_file,"r")
    question_formatting()

#QUIZ CHECKER (main program)
choose_file_window = tk_module.Tk()
choose_file_window.title("QUIZ CHECKER")
choose_file_window.geometry("1000x100") 
opening_message = tk_module.Label(choose_file_window, text="QUIZ CHECKER\nThis program is used so you can answer the quiz you " \
"just created uisng basic quiz creator. You can also use this so other people can answer your created quiz.\n Note that" \
"this will not work if you use other quizzes, not created using basic quiz maker. Otherwise, click the button below to" \
"choose which quiz you want to answer.") #Ask user the quiz they want to answer.
opening_message.pack()

choose_quiz_button = tk_module.Button(choose_file_window, text="Choose Quiz", command=choose_file)
choose_quiz_button.pack()

choose_file_window.mainloop()

#Add 1 to number of corrects (if correct) and the number of questions answered over the total number of questions.
#Flash ending message, positive if passed, negative if failed. (try adding multiple ending mesages done at random)
#Add choice wether to exit the program or answer another quiz.