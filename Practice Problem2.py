
if __name__ == '__main__':
    apples = int(input("Enter the number of apples you wanna give"))
    mn = int(input("Enter the mn number"))
    mx = int(input("Enter the mx number"))
    divisors = []
    not_divisors = []
    for i in range(mn, mx+1):
        if i%apples == 0:
            divisors.append(i)
            print(f"{i} is a divisor of {apples}")
        elif i%apples != 0:
            not_divisors.append(i)
            print(f"{i} is not a divisor of {apples}")
    print(f"This is the list of numbers that are divisors of {apples}:\n{divisors}\nThis is the list of the numbers that are not divisors of {apples}:\n{not_divisors}")