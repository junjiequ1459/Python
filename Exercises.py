'''1) Write a short guessing game program using a while loop. The user should be prompted to guess a number between 1 and 100, and you should tell them whether their guess was too high or too low after each guess. The loop should keeping running until the user guesses the number correctly.

2) Use a loop and the continue keyword to print out every character in the string "Python", except the "o".

Remember that strings are collections, and they are iterable, so you can iterate over the string, which will yield one character at a time.

3) Using one of the examples from earlier—or a solution entirely of your own—create a program that prints out every prime number between 1 and 100.'''

#1
answer = 69
user_number = int(input("please enter a number"))

while user_number != answer:
    if user_number < 0 or user_number > 100:
        print("not valid input")
        user_number = int(input("please enter a number"))
    if answer > user_number:
        print("guess higher")
        user_number = int(input("please enter a number"))
    elif answer < user_number:
        print("guess lower")
        user_number = int(input("please enter a number"))

print("thats the right answer")


#2

for i in "python":
    if i == 'o':
        continue
    print(i,end = '')
print('\n')


number = 2
while number < 101:
    for i in range(2,number):
        if number % i == 0:
            break
    else:
        print(number)
    number = number + 1











def main():
    pass
if __name__ == '__main__':
    main()