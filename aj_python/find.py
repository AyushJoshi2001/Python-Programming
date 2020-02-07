s = input()
l=0
for i in s:
    if i == 'p' or i=='P':
        l+=1
if l>0:
    print('p is present.')
else:
    print('p is not present.')
