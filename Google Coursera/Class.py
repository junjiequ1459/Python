
class Cat:
    name = "Rex"
    def speak(self):
        print("hi my name is {}".format(self.name))


cat = Cat()

cat.speak()

class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age

Rex = Cat("REX",21)


print(Rex.name)




def main():
    pass
if __name__ == '__main__':
    main()