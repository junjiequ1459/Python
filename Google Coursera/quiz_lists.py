filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = []

for file in filenames:
    if file[-3:] == "hpp":
        newfilenames.append(file[:-3] + "h")
    else:
        newfilenames.append(file)



#print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

def pig_latin(text):
    newlist = []
    # Separate the text into words
    words = text.split()
    for word in words:
        # Create the pig latin word and add it to the list
        newlist.append(word[1:])
        # Turn the list back into a phrase
    return newlist


print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun"))  # Should be "rogrammingpay niay ythonpay siay unfay"







def main():
    pass
if __name__ == '__main__':
    main()


