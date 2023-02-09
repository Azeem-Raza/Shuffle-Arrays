number1 = [2,5,1,3,4,7]
number2 = [1,1,2,2]
number3 = [1,2,3,4,4,3,2,1]
n1,n2,n3= 3,2,4

res1=[]
res2=[]
res3=[]

for i in range (n1):
    res1.append(number1[i])
    res1.append(number1[i+n1])

print("Shuffle of number1: ", res1)


for index in range (n2):
    res2.append(number2[index])
    res2.append(number2[index+n2])

print("Shuffle of number2: ", res2)

for index in range (n3):
    res3.append(number3[index])
    res3.append(number3[index+n3])

print("Shuffle of number3: ", res3)
