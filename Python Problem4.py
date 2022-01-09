# The Next Palindrome
try:
    times = int(input("How many numbers you want to give?\n"))
    digits = 1
    List = []
    for i in range(times):

        Userinput = int(input(f"{digits}. Enter your number:\n "))
        blank = Userinput
        digits += 1
        while True:
            Userinput+=1
            t = str(Userinput)
            if t == t[::-1]:
                print(f"The next Palindrome for '{blank}'  is '{t}'")
                break
            else:
                continue
        List.append(Userinput)
        
        
    print(f"Your List of 'Next Palindromes' is: \n{List}")

except Exception as f:
    print(f"{f}\nStrings are not allowed")

    
        



    
