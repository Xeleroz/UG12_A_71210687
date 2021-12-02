a = input("Input: ")
print("Output: ")

for i in range(len(a)):
	print(a[0:i+1])

for b in range(len(a)):
	print(a[0:len(a)-1-b])