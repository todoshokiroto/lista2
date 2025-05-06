n = int(input())
cont = 2
encont = 0
while encont < n:
    soma = 0
    for i in range(1,cont):
        if cont%i== 0:
            soma +=i
    if soma == cont:
        encont +=1
        print(cont)
    cont+=1