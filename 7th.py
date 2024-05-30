n = int(input("Enter starting number:"))
m = int(input("Enter last number:"))

for i in range(n, m+1):
    if i > 1:
        for a in range(2, i):
            if(i % a) == 0:
                print(i)
