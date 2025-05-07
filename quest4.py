aGet = int(input())
bGet = int(input())
a = aGet
b = bGet
if a%b == 0:
    print(f'não são bros, {b} é divisor de {a}')
while a%b != 0:
    i = a
    a = b
    b = i%b
    if b == 1:
        print('são bros')
        break
    elif a%b == 0:
       print(f'não são bros, pois {aGet} e {bGet} tem como divisor {b}')
