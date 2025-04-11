import os

def option_one():
    options = []
    question_with_choice=""
    f = open("Untitled Quiz.txt", "w")
    f.write("(IMPORTANT NOTE: Please change the filename of this quiz after checking as it may be deleted when creating"
            " a new one. Delete this notice after. Thank you!)\n\n")

    while True:
        question=input("Question:") #Asks user for input
        question_with_choice+=question+"\n"#Adds new line so choices will be written below the question"
        option_count = 0
        options.clear() #clears items in options list, so the number from preceding numbers re not printed
                        #again in the following numbers.

        while option_count!=4:#So user will be asked for 4 options
            option = input("Add option:")#Ask user for option
            options.append(option)#Adds user's input into 'options' list
            option_count = option_count + 1 #Adds one count to inputted options to keep tract how any are added.

        for options_item_index, option in enumerate(options):
            question_with_choice += f"{chr(ord('a')+options_item_index)}. {option} \n"
        f.write(question_with_choice)

        while True:
            ask = input("Add another question?(Y/N)")
            if ask == "Y" or ask == "y":
                new_line="\n"
                f.write(new_line)
                question_with_choice=""
                break

            elif ask == "N" or ask == "n":
                print("\nThank you for using basic quiz maker. Be sure to rename your file or else it will"
                        "be replaced if you make a new quiz.FOr now, a notepad file will open which contians all the"
                      "questions that you have inputted. Thank you!\n")
                f.close()
                os.startfile('Untitled Quiz.txt')
                break

            else:
                print("you can only answer Y or N")
                continue
        if ask == "Y" or ask == "y":
            continue
        elif ask == "N" or ask == "n":
            break

def option_two():
    options = []
    question_with_choice=""
    f = open(filename, "a")
    space="\n"
    f.write(space)
    f.write("(This is the start of your editing using quiz maker. Delete this after checking. Thank you!)\n\n")

    while True:
        question=input("Question:") #Asks user for input
        question_with_choice+=question+"\n"#Adds new line so choices will be written below the question"
        option_count=0
        options.clear() #clears items in options list, so the number from preceding numbers re not printed
                        #again in the following numbers.

        while option_count!=4:#So user will be asked for 4 options
            option = input("Add option:")#Ask user for option
            options.append(option)#Adds user's input into 'options' list
            option_count = option_count + 1 #Adds one count to inputted options to keep tract how any are added.

        for options_item_index, option in enumerate(options):
            question_with_choice += f"{chr(ord('a')+options_item_index)}. {option} \n"
        f.write(question_with_choice)

        while True:
            ask = input("Add another question?(Y/N)")
            if ask == "Y" or ask == "y":
                new_line="\n"
                f.write(new_line)
                question_with_choice=""
                break

            elif ask == "N" or ask == "n":
                print("\nThank you for using basic quiz maker. The file you have edited will now be opened so you can"
                      "check the changes.\n")
                f.close()
                os.startfile(filename)
                break

            else:
                print("you can only answer Y or N")
                continue
        if ask == "Y" or ask == "y":
            continue
        elif ask == "N" or ask == "n":
            break

#Menu
option_count = 0
print("BASIC QUIZ MAKER")
print("To get started\n"
      "1:Create Quiz\n"
      "2:Edit Existing Quiz\n"
      "3:Exit")

#Main Prompt
while True:
    try:
        choice = (int(input("\nWhat do you want to do? Pick 1, 2, or, 3:")))
        if choice==1:
            print("\n----------\n\nYou have chosen 'CREATE QUIZ'\n")
            option_one()
            break

        if choice==2:
            print("\n----------\n\nYou have chosen 'EDIT EXISTING QUIZ'\n")
            filename=input("input filename of quiz you want to edit(be mindful with the cases and spaces):")
            filename=filename+'.txt'
            option_two()
            break

        elif choice==3:
            print("\nYou have chosen 'EXIT'\n\nGoodbye!")
            break

        else:
            print("\nYou can only pick between 1, 2, and 3.\n\n----------\n")

    except ValueError:
        print("\nYou can only pick between 1, 2, and 3.\n\n----------\n")