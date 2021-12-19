#for loop Day05 and Ex02

height = input("Enter some different Heights!!\n").split()
for n in range(0, len(height)):
    height[n]=int(height[n])
print(height) 
length_height=len(height)
sum1=sum(height)
print(sum1)

Another way

sum=0
avg=0
for i in height:
    sum=sum+i
avg=round(sum/length_height)
print(f"sum of all height is := {sum}")

print(f"Average of all height is := {avg}")
