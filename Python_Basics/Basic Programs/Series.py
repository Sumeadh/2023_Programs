# 1)1+(1+2)+(1+2+3)...
'''
n=int(input('enter the value of n'))
cnt=0
Sum=0
while cnt<n:
    tsum=0
    for i in range(cnt+2):
        tsum+=i
    Sum+=tsum
    cnt+=1
print(Sum)
'''
# 2)e^x
'''
n=int(input('enter the value of n'))
x=int(input('enter the value of x'))
cnt=0
Sum=0
while cnt<n:
    tsum=1
    for i in range(1,cnt+2):
        tsum*=i
    print(i)
    Sum+=(x**i)/tsum
    cnt+=1
print(Sum)
'''
# 3)cos(x)
'''
n=int(input('enter the value of n'))
x=int(input('enter the value of x'))
cnt=0
Sum=0
while cnt<n:
    tsum=1
    i=0
    for i in range(1,cnt*2+1):
        tsum*=i
    if i%4==0:
        Sum+=(x**i)/tsum
    else:
        Sum-=(x**i)/tsum
        #print(Sum)
    cnt+=1
print(Sum)
'''
# 4)sinx
# x (0) -x^3/3! (1) + x^5/5! (2)...
'''
n=int(input('enter the value of n'))
x=int(input('enter the value of x'))
Sum=0
for i in range(n):
    fact=1
    for j in range(1,(i*2+1)+1):
        fact*=j
    Sum+=((-1)**i)*(x**j)/fact
print(Sum)
'''
# 5)log(1+x)
# x-x^2/2+x^3/3...
'''
n=int(input('enter the value of n'))
x=int(input('enter the value of x'))
Sum=0
for i in range(1,n+1):
    Sum+=(-1)**(i+1)*x**i/i
print(Sum)
'''
