#random order

name=input("give some name seperated by comma ana space")
name1=name.split(", ")
length= len(name1)
choice=random.randint(0,length-1)
person=name1[choice]
print(person+" is paying the bill for all")
