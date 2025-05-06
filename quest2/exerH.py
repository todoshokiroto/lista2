n = int(input())
arr = []
crescente = True
for i in range(n):
    item = float(input())
    arr.append(item)
    if i > 0:
        if arr[i] < arr[i-1]:
            crescente = False

if crescente:
    print("ordem crescente")
else:
    print("não esta em ordem crescente")

