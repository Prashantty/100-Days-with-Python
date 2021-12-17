
# tip calculator 

print("Welcome to the tip calculator \n")
bill=float(input("what is your total bill in Rs::"))
tip=int(input("So what % would you like to give as tip:: 10 ,12 or15 --"))
people=int(input("how many people to split the bill::"))

bill1=tip/100*bill+bill
split=round(bill1/people,2)
print(f"Each person has to pay Rs{split}")
