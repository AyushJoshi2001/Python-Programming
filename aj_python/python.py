s = input('Enter string:').split(' ')
l=0
for i in s:
    if i == 'python':
        l+=1
if l>0:
    print('python is present.')
else:
    print('python is not present.')
