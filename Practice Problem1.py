#Tell users when they'll be 100 years old

detection = ''


def calc(detection, Userinput):
    if detection == 'age':

        years = 0
        var = int(Userinput) #age
        if var >= 120:
            print("You are already above hundred. ;)")
            exit()

        elif var >= 300:
            print("You seems to be the oldest person alive. ;) ")

        while var != 100:
            var = var + 1
            years = years + 1
        print(f"You will take {years} years to be 100. ;)")    

    elif detection == 'year':

        years = 0
        var = int(Userinput)
        current_year = 2022
        age = current_year - var #age
        if var > current_year :
            print("You are not born yet.")
            exit()
        elif var == current_year:
            print("You will take literally 100 years to be hundred.")
        if var <= 1890:
            print("You seems to be the oldest person alive.")
            exit()

        while age != 100:
            age = age + 1
            years = years + 1
        print(f"You will take {years} years to be 100.") 

    

if __name__ == '__main__':
    Userinput = str(input("Enter your AGE or your YEAR OF BIRTH here.\nAge: xx\nYear: xxxx\n"))
    if  len(Userinput) == 2 or len(Userinput) == 3:
        detection = 'age'

    elif len(Userinput) == 4:
        detection = 'year'


    Userinput2 = input("Do you want to check in which year you'll become 100 years old?\n")
    if Userinput2 == 'yes':
        calc(detection, Userinput)

    elif Userinput2 == 'no':
        print("No Problem")

    else:
        print("Please tell us via 'yes' or 'no'.")
        