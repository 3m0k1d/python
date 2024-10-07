def acos(x, y):
    return x / ((x**2 + y**2)**0.5)
x1, x2 = map(float, input().split())
y1, y2 = map(float, input().split())
z1, z2 = map(float, input().split())
res = [x1, x2]
acosx = acos(x1, x2)
acosy = acos(y1, y2)
if acosy > acosx:
    acosx = acosy
    res = [y1, y2]
acosz = acos(z1, z2)
if acosz > acosx:
    acosz = acosz
    res = [z1, z2]
print(*res)

def delit(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True
n = int(input('введите количество чисел: '))
res = []
for z in range(2, n+1):
    b1n = ''
    if delit(z) == True:
        if b1n+str(bin(z)[2:]) == b1n+str(bin(z)[2:])[::-1]:
            res.append(z)
            res.append(bin(z)[2:])
print(res)