b = []
for i in range(9):
    c = int(input())
    b.append(c) 
maxvalue = max(b)
indexvalue = b.index(maxvalue)
print(maxvalue,indexvalue+1)
