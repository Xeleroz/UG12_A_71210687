n = input("Masukkan deret angka: ")
a = n.split(",")
jum = 0

for i in a:
	if int(i)%2 == 0:
		g = + int(i)
	else:
		g = - int(i)
	jum = jum + g
print("Total: ",end="" )

c = ""
for i in a:
	
	if int(i)%2 == 0:
		hasil = (" + "+str(i))
	else:
		hasil = (" - "+str(i))
	c = c+hasil

if c[1] == "+":
	print(c[2:len(c)])
else:
	print(c)

print("Hasil perhitungan di atas ialah: ", end=" " )
print(jum)