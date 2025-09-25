#for loop for adding first 5 natural numbers
sum = 0
for i in range(1, 6):
    sum+=i #sum = sum + i
print('Sum', sum)

#Printing numbers in reverse order:
for i in range(5, 0, -1):
    print(i)
#Print square bumbers from 1 to 5 
for i in range(1, 6):
    print('Square of i', i, 'is', i*i)

#EVEN AND POSITIVE SIMPLE LOGIN SYSTEMS
num = int(input("Enter A Number: "))

if (num >0) & (num % 2 ==0):
    print(True)
else:
    print(False)