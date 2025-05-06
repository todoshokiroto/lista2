1
n = int(input())
for i in range(n):
    if(i * (i+1) * (i+2) == n):
        print(f'{i} x {i+1} x {i+2} = a {n}')
        break
    if i == n-1:
        print('não é')
