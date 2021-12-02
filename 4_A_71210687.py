a = int(input("Input : "))
print("Output : ")
k = 2
for row in range(1,a+1):
    for col in range(1,2*a):
        if row == a and col != k:
            print("*", end="")
            k = k+2
        elif row + col == a+1 or col - row == a-1:
            print("*",end="")
        else:
            print(end=" ")
    print()