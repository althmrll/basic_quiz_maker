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
    global score
    asked_question=0
    fraction=asked_question/len(answer)
    percentage=fraction*100
    score=0
    questions_asked=[]
    while asked_question!=len(question_with_choice):
        random_index=random.randint(0,len(question_with_choice)-1)

        while True:
            if question_with_choice[random_index] in questions_asked:
                return False
            else:
                print(questions_asked, "questions asked out of", len(answer))
                print(f"Score:{score}({percentage} % done)")
                print(question_with_choice[random_index])
                questions_asked.append(question_with_choice[random_index])
                user_answer=input("Your answer:")
                user_answer=user_answer.upper()

                if user_answer==answer[random_index]:
                    print("Correct!!")
                    asked_question+=1
                    score=score+1
                    break
                else:
                    print("Wrong, the correct answer is", answer[random_index])
                    asked_question+=1
                    break
    finish

def finish():
    if score>len(answer)/2:
        print("You have finished the quiz and answered", score, "questions out of", len(answer), "Congrats!")
        replay
    else:
        print("You have finished the quiz and answered", score, "questions out of", len(answer), "Better luck next time!")
        replay

def replay():
    while True:
        replay=input("Do you want to answer another quiz?(Y/N)")
        replay=replay.upper()
        if replay=="Y":
            score=0
            print("1: Replay Quiz\n2:Choose Another Quiz")
            while True:
                replay_choice=input("Your Choice:")
                if replay_choice==1:
                    choose_file
                elif replay_choice==2:
                    choose_file
                else:
                    print("Invalid Input, Reasking Question...")
                    return False

        elif replay=="N":
            print("Goodbye!")
            exit

        else:
            print("Invalid Output, Reasking Question...")
            return False
        
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