#1)
'''
def armstrong(n,temp,Sum=0):
    if temp==0:
        if n==Sum:
            return 'Is Armstrong'
        else:
            return 'Not Armstrong'
    Sum+=(temp%10)**3
    temp=temp//10
    return armstrong(n,temp,Sum)
n=int(input('enter a number'))
print('The armstrong numbers are')
for i in range(n+1):
    if armstrong(i, i) == 'Is Armstrong':
        print(i)
'''
#2)nCr
#3)Passphrase Generator