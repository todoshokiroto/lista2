jogA = 800
taxaA = .03
jogB = 2000
taxaB = .015
anos = 0
while jogA < jogB:
    jogA += jogA*taxaA
    print(jogA)
    jogB += jogB*taxaB
    print(jogB)
    anos+=1
print(anos)