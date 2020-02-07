s = input()
l = len(s)
a=0
b=0
for i in range(0,l):
    if s[i] == 'p':
        a = i
        break
for i in range(0,l):
    if s[i] == 'm':
        b = i
a+=1
b+=1
print('First occurence of p is = {}'.format(a))
print('Last occurence of m is = {}'.format(b))
