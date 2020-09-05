arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]
odd = []

for x in range(0, len(arr)):
    total = 0
    if arr[x]%2 != 0:
        odd.append(arr[x])
        total = sum(odd)
        

print(total)




