#1) Time-->Seconds
'''
h=int(input('Enter the number of hours'))
m=int(input('Enter the number of minutes'))
s=int(input('Enter the number of seconds'))
print(h*60*60+m*60+s)
'''
#2)Area of Tiles
'''
l=int(input('Enter the length of tiles'))
b=int(input('Enter the breadth of tiles'))

L=int(input('Enter the length of room'))
B=int(input('Enter the breadth of room'))

x=int(input('Enter the cost per tiles'))

print('Total Cost is :',x*(L*B)/(l*b))
'''
#3)Speed Distance
'''
q=int(input('Enter the speed'))
d=int(input('Enter the distance'))
print('time taken is:',d/q)
'''
#4)Area Of Triangle
'''
b=int(input('Enter the base'))
h=int(input('Enter the height'))
print('time taken is:',(1/2)*b*h)
'''

#5)Date Validation
'''
ans='y'
while ans=='y':
    d=int(input('Enter the day'))
    m=int(input('Enter the month'))
    y=int(input('Enter the year'))

    if m==2:
        if y%4==0:
            if d>29:
                print('invalid')
                break
        else:
            if d>28:
                print('invalid')
                break
    elif m in (1,3,5,7,8,10,12):
        if d>31:
            print('invalid')
            break
    else:
        if d>30:
            print('invalid')
            break
    print('valid')
    ans=input('want to enter more values?y/n')
'''   
#6)Function Program
'''
x=int(input('Enter the number x'))
n=int(input('Enter the number n'))
if n==0:
    print(x)
elif n==1:
    print(x+1)
elif n==2:
    print(x**2+n)
else:
    print(x**n)
'''
#7)Eb Bill
'''
a = int(input("enter past month reading : "))
b = int(input("enter current month reading : "))
if b-a < 0:
    c=None    
if b-a <= 200 and b-a >= 0:
    c = (b-a)*0.50
elif b-a <= 400 and b-a >= 0:
    c = 100 + (b-a-200)*0.65
elif b-a <= 600 and b-a >= 0:
    c = 100 + 200*0.65+(b-a-400)*0.80
elif b-a > 600 and b-a >= 0:
    c = 100 + 200*0.65 + 200*0.80+(b-a-600)*1.25
print("your current bill in rupees is = ", c)
'''
    
