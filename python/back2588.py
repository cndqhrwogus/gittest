a = input()
b = input()
a = int(a)
c= []
c.append(a*int(b[2]))
c.append(a*int(b[1]))
c.append(a*int(b[0]))
c.append(a*int(b))
for number in range(len(c)):
    print(c[number])