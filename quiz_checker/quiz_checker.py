#QUIZ CHECKER
import tkinter as tk_module

#Ask user the quiz they want to answer (use pop-up?)
window=tk_module.Tk()
window.title("Quiz Checker")
window.geometry("600x400") 
label = tk_module.Label(window, text="QUIZ CHECKER\nThis quiz checker is partnered with the Basic Quiz Creator. If you have no" \
"quiz available, Create one now. Or you can click the button below so you can choose which quiz to answer.")
label.pack()
window.mainloop()

#Print one question with choices for user to answer
#Make user press 'submit' (or enter) button.
#After submitting, show user the correct answer
#Add 1 to number of corrects (if correct) and the number of questions answered over the total number of questions.
#Flash ending message, positive if passed, negative if failed. (try adding multiple ending mesages done at random)
#Add choice wether to exit the program or answer another quiz.