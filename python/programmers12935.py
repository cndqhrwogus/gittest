arr =[10]
if len(arr) == 1:
    arr.clear()
    arr.append(-1)
    print(arr)
else: 
    min_value = min(arr)
    arr.remove(min_value)
    print(arr)