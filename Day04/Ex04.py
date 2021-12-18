# rows and columns

row1=["😃","😃","😃"]
row2=["😃","😃","😃"]
row3=["😃","😃","😃"]

row=[row1,row2,row3]

print(f"{row1}\n{row2}\n{row3}")

position=(input("Enter the positon where you want to change\t"))

row[int(position[0])-1][int(position[1])-1]= "🥰"
print(f"{row1}\n{row2}\n{row3}")
