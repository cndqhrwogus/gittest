n = 12345
a = 0
test = list(str(n))
test1 = list(map(int,test))
answer = []
for a in range(len(test1)-1,-1,-1):
    answer.append(test1[a])
print(answer)
