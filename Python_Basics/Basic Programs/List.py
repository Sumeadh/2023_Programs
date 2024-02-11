#1)Generate prime numbers
#List
'''
n=[]
while True:
    a=int(input('enter the number to be appended'))
    n.append(a)
    answ=input('DO you want to add more?')
    if answ!='y':
        break
for i in n:
    for j in range(2,i//2):
        if i%j!=0:
            continue
        else:
            print('the number',i,'is a composite number')
            break
    else:
        print('the number',i,'is a prime number')
'''
#2) Marks calculator
'''
N = [int(input("enter physics marks")), int(
    input("enter chemistry marks")), int(input("enter maths marks"))]

print(max(N))
print(min(N))
print(sum(N)/len(N))
'''


            
