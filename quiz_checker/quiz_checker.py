import os
import tkinter as tk_module
from tkinter import filedialog
import random
global questions_asked

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

def question_with_choice_formatting():
    find_word="Correct Answer:"
    format_question_and_options=[]
    lines = file.readlines()

    for indiv_lines in lines:
        if indiv_lines!="\n":
            if indiv_lines.startswith(find_word):
                formatted_answer=str(indiv_lines)
                formatted_answer=formatted_answer.replace(find_word,"").replace("\n","").upper()
                answer.append(formatted_answer)
            else:
                format_question_and_options.append(indiv_lines)

        elif indiv_lines=="\n" or indiv_lines=="":
            formatted_question_and_option="".join(format_question_and_options)
            question_with_choice.append(formatted_question_and_option)
            format_question_and_options.clear()
    formatted_question_and_option="".join(format_question_and_options)
    question_with_choice.append(formatted_question_and_option)

def ask_question_and_answer():
    global shuffled_answers
    answer_key= list(zip(question_with_choice, answer))
    shuffled=random.shuffle(answer_key)
    shuffled_questions, shuffled_answers = zip(shuffled)
    question_count=0
    while question_count!=len(shuffled_questions):
        for questions in shuffled_questions:
            print(question_count,"/", len(shuffled_questions))
            print(questions)
            answer=input("Your answer:")
            question_count+=1
            check_answer()


def check_answer():
    if answer==shuffled_answers:
        print("Correct!!")
    else:
        print("Wrong, Correct answer is", shuffled_answers)

def main_quiz():
    global file
    choose_file_window.withdraw()
    file=open(chosen_file,"r")
    question_with_choice_formatting()
    ask_question_and_answer()

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