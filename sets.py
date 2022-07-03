#7/3/22
#set = collection which is unordered, unindexed. No dupes

utensils = {"fork","spoon","knife"}
dishes = {"bowl","plate","cup","knife"}

utensils.add("napkins")                 #adds element
utensils.remove("fork")                 #removes element
utensils.clear()                        #clears set
dishes.update(utensils)                 #adds one set set to another
dinner_table = utensils.union(dishes)   #combine set

print(utensils.difference(dishes))      # show differences

print(utensils.intersection(dishes))    # show same values


def main():
    pass
if __name__ == '__main__':
    main()