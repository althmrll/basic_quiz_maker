def option_one():
    options = []
    question_with_choice=""
    f = open("Untitled Quiz.txt", "w")

    while True:
        question=input("Question:")
        question_with_choice+=question+"\n"
        option_count = 0
        options.clear()

        while option_count!=4:
            option = input("Add option:")
            options.append(option)
            option_count = option_count + 1

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
                        "be replaced if you make another one.")
                f.close()
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
      "2:Exit")

#Main Prompt
while True:
    try:
        choice = (int(input("\nWhat do you want to do? Pick 1 or 2:")))
        if choice==1:
            print("\n----------\n\nYou have chosen 'CREATE QUIZ'\n")
            option_one()
            break

        elif choice==2:
            print("\nGoodbye!")
            break

        else:
            print("\nYou can only pick between 1 and 2.\n\n----------\n")

    except ValueError:
        print("\nYou can only pick between 1 and 2.\n\n----------\n")