def option_one():
    while True:
        question=input("Question:")
        f.write(question)

        while option_count!=4:
            option = input("Add option:")
            f.write(option)
            option_count = option_count + 1

#Menu
option_count = 0
print("BASIC QUIZ MAKER")
print("To get started\n"
      "1:Create Quiz\n"
      "2:Exit")
choice=(int(input("What do you want to do? Pick 1 or 2:")))

#Main Prompt
while True:
    try:
        if choice==1:
            f=open("quiz_maker.txt", "w")
            option_one()

            ask = input("Add another question?(Y/N)")
            if ask=="Y" or ask=="y":
                continue
            if ask=="N" or ask=="n":
                f.close()
                f.open("quiz_maker.txt")
                break

        elif choice==2:
            print("Goodbye!")
            break

    except:
        print("You can only pick between 1 and 2.")