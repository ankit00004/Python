n = int(input("Enter starting number:"))
m = int(input("Enter last number:"))
for i in range(n, m+1):
    if(i % 2 == 1):
        print("Odd number is :", i)
        flag = 1
        print("Even number is :", i)

for a in range(n, m+1):
    if(a % 2 == 0):
        print("Even number is :", a)
