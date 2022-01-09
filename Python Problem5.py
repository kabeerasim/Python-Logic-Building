# Calculates the next palindrome of a given number

#Takes a n number and run it until it is not equal to its next palindrome
def next_palindrome(n):
    n = n+1
    while not is_palindrome(n):
        n += 1
    return n

#Takes a n number whenever it is called
#Return that number's if it is next palindrome.
def is_palindrome(n):
    return str(n) == str(n)[::-1]

if __name__ == '__main__':
    size = int(input("Enter the size of your list:\n"))
    num_list = []
    for i in range(size):
        num_list.append(int(input("Enter the number of your list:\n")))
    print(f"You have entered {num_list}")

    print(f"Output List:\n {[num_list[i] if num_list[i] < 10 else next_palindrome(num_list[i]) for i in range(size)]}")