#dictonary = A changeable, unordered collection of unique key:value pair, fast because they use hashing. allows us to access a value quickly

captial = {"USA":"Washington Dc",
           "India":"New Dehli",
           "China":"Beijing",
           "Russia":"Moscow"}


print(captial.get("Germany"))   # see if key in dic
print(captial.keys())           # prints all keys
print(captial.value())          # prints all value
print(captial.items())          # prints key and values

# for line 12 can also use for loop

for key,value in captial.items():
    print(key,value)

captial.update({"Germany":"Berlin"})  # update dictionary
captial.update({"USA":"Las Vegas"})   # updated only value
captial.pop("China")                  # Removes key:value pair
captial.clear()                       # Clears dic



def main():
    pass
if __name__ == '__main__':
    main()