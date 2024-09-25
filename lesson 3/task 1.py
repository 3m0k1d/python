n = int(input())
x = ''
if n > 100:
    print('ошибка')
else:
    for i in range(1,n+1):
        x += str(i**3)
        x += ' '
print(x)

for x in range(1,10):
    for i in range(1,10):
        print(f'{x} x {i} = {x*i}')
    print()