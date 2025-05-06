for i in range(1000):
    if(i>=100):
        n1 = i//100
        n2 = (i%100)//10
        n3 = (i%100)%10
        if (n1**3 + n2**3 + n3**3) == i:
            print(i)
