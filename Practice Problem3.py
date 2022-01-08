#Foods and Calories
# Take the size of the list from the user

# reverse2 = mylist[:]
# reverse2.reverse()

print("Enter the numbers of the list one by one\n")
size = int(input("Enter the size of the list.\n"))

# Initialize a blank list
mylist = []
number = 0

# Take the input from the user one by one
for i in range(size):
    number = number + 1
    mylist.append(input(f"{number}. Enter list element: "))

reverse1 = list(reversed(mylist))

reverse2 = mylist[::-1] 

reverse3 = mylist[:]
length = len(reverse3) // 2
for i in range(length):
    reverse3[i], reverse3[len(reverse3) -i -1] = reverse3[len(reverse3) -i -1], reverse3[i]

print(f"My first reversed list is\n{reverse1}")
print(f"My Second reversed list is\n{reverse2}")
print(f"My Third reversed list is \n{reverse3}")

if reverse1 == reverse2 and reverse2 == reverse3:
    print("All lists are same")