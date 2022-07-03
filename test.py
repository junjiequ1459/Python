
for number in range(2,101):
    for x in range(2,number):
        if number % x == 0:
            break
    else:
        print(number)
else:
    print("Program done")





def main():
    pass
if __name__ == '__main__':
    main()