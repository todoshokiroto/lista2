#escrita dos termos de Fibonnaci menores que L
l = int(input())

#processamento dos dois primeiros termos
termo1 = 1
if termo1 <= l:
    print(termo1)

termo2 = 2
if termo2 <= l:
    print(termo2)

#processamento dos termos restantes
while l>= termo1 + termo2:
    termoAt = termo1+termo2
    print(termoAt)
    termo1 = termo2
    termo2 = termoAt