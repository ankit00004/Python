n = int(input("Enter minimum number:"))
m = int(input("Enter maximum number:"))
if(n % 5 == 0 and n % 9 == 0):
    if (m % 5 == 0 and m % 9 == 0):

        for i in range(n, m):
            if(i % 5 == 0 and i % 9 == 0):
                print(i)
