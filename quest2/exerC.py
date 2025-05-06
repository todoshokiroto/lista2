n = int(input())
var = 1
for i in range(50):
    if (i+1)%2 == 0:
        print(var * n)
    else:
        print(var + n)
    var +=4
    