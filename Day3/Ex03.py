# leap year

year=int(input("Enter the year Which you want to check!!"))

if year%4==0:
    if year%100==0:
        if year%400==0:
            print("Yes this is leap year!")
        else:
            print("This is 2not a leap year!")
    print("yes this is leap year!")
else:
    print("This is not a leap year!")                
