#index op [] = gives access to a sequence's element (str,list,tuples)

name = 'junjie qu'

if name[0].islower():
    name = name.capitalize()

print(name)

first_name = name[:6]
last_name = name[7:]
print(first_name)
print(last_name)


def main():
    pass
if __name__ == '__main__':
    main()