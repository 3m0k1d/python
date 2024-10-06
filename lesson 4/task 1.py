n = input()
n = n.replace('н','!')
x = ''
z = []
for i in range(len(n)):
    if n[i] == '!':
        x += n[i]
    else:
        z.append(len(x))
        x = ''
print(f'{n}, количество букв н: {max(z)}')

s = '12(asdad)52!'
x = []
z = ''
x.append(s.index('('))
x.append(s.index(')'))
for i in range(min(x),max(x)+1):
    z += s[i]
print(z[1:-1])

s = input().split(' ')
nach = 'а'
kon = 'я'
l = []
z = []
for x in s:
    if x.startswith(nach):
        l.append(x)
    if x.endswith(kon):
        l.append(x)
for i in range(len(l)-1):
    if l[i] == l[i+1]:
        z.append(l[i])
print(z)
