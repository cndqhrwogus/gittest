a = int(input())
b = 0
count = 0
b = a
while True:
    c = b//10
    d = b%10
    e = c+d
    b = (d*10)+(e%10)
    count = count+1
    if a == b:
        break
print(count)