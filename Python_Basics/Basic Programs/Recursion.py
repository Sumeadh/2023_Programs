#binary to decimal
#111.1111--->8.8
'''
def binToDec(x):
    
    if x == 1 or x == 0:
        return x
    
    l = len(str(x))
    firstDigit = x//pow(10,l-1)
    print(firstDigit)
    return (pow(2,l-1) * firstDigit)+ binToDec(x%pow(10,l-1))

binary = int(input('Enter a Binary number: '))
decimal = binToDec(binary)

print("Decimal of {p} is {q} ".format(p=binary, q=decimal))
'''
# decimal to binary
# (32)10-->(11111)2

'''
def dec_bin(n):
    if n>1:
        return dec_bin(n//2)+str(n % 2)
    else:
        return str(n)
ans=dec_bin(32)
print(ans)
'''

# nCr--> n!/(n-r)!r!
'''
def nCr(n,r):
    if n-r>=0 and n>=0 and r>=0:
        if r==0:
            return 1
        if r==1:
            return n
        else:
            return n/r*nCr(n-1,r-1)
    else:
        return None
n=int(input("Enter the value of n"))
r = int(input("Enter the value of r"))
a=nCr(n,r)
print(a)
'''
