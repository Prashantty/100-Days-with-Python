#dicision making 

print("welcome to our ride")
height=int(input("Enter your Height!!"))

if height>=120:
    print("you can enjoy the ride!!")
    age=int(input("Enter your age !!"))
    if age<12:
        bill=100
        print("your ticket price is Rs=100")
    elif age<=18:
        bill=120
        print("your ticket price is Rs=120")
    else:
        bill=150
        print("your ticket price is Rs=150")
    pics=input("Want to click pictures if Yes wite 'y' or if no then 'n'").lower()
    if pics == 'y':
        bill=bill+50
    print(f"Your total bill is Rs={bill}")
    print("Thank You")        
else:
    print("sorry !! you cannot enjoy the ride!")
