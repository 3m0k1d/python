n = input()
n = n.replace('!','.')
x = ''
z = []
for i in range(len(n)):
    if n[i] == 'н':
        x += n[i]
    else:
        z.append(len(x))
        x = ''
print(max(z))