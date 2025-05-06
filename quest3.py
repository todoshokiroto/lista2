import random
acertos = 1
for i in range(3):
    x = random.randint(1,100)
    y = random.randint(1,100)
    erro = True
    while erro:
        print(f'quanto é o poder {x} multiplicado pela resistencia {y} da carta ?')
        resp = int(input())
        if resp == (x*y):
            print(f'acertou {acertos} vez/vezes,faltam {3-acertos}')
            erro = False
            acertos +=1
        else:
            print("errado, tente denovo")


