a = int(input())
for i in range(a-1,-1,-1):
    print(' '*i,end='')
    for c in range(a,i,-1):
        print('*',end='')
    print()