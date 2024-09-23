s = '12(asdad)52!'
x = []
z = ''
x.append(s.index('('))
x.append(s.index(')'))
for i in range(min(x),max(x)+1):
    z += s[i]
print(z[1:-1])