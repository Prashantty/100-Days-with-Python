# using for loop (max)

score = input("Enter some different Heights!!\n").split()
for n in range(0, len(score)):
    score[n]=int(score[n])
print(score) 
length_height=len(score)  
print(max(score)) 
max_score=0
for n in score:
    if n>max_score:
        max_score=n

print(max_score)
