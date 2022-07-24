class Apple:
    def __init__(self,color,flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self):
        return "THIS APPLE IS {} and its flavor is {}".format(self.color,self.flavor)



rex = Apple("red","sweet")


print(rex)



def main():
    pass
if __name__ == '__main__':
    main()

