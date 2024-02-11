#Dec to Bin
'''
dnum=float(input("Enter the decimal number: "))

dec=dnum%1
who=int(dnum//1)

raf=''
for i in range (0,6):
    val=dec*2
    if val<1:
        ans=0
    else: ans=1
    raf=raf+str(ans)
    dec=val%1
decipart= f".{raf}"
ref=""
while who!=0:
    rem=who%2
    who=who//2
    ref=ref+str(rem)
whole=ref[::-1]
print(whole+decipart)

'''
#Dec to Oct
'''
dnum=int(input("Enter the decimal number: "))

ref=""
while dnum!=0:
    rem=dnum%8
    dnum=dnum//8
    ref=ref+str(rem)

    
print(ref[::-1])
'''
#Dec to Hexa
'''
dnum=int(input("Enter the decimal number: "))

ref=""
while dnum!=0:
    rem=dnum%16
    dnum=dnum//16
    if len(str(rem))>1:
        vals= {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
        rem=vals[rem]
    ref=ref+str(rem)

    
print(ref[::-1])
'''
#Bin to Dec
'''
bnum = input("Enter Binary Number: ")
val = 0


size = len(bnum) - 1

for num in bnum:
	val = val + int(num)*2**size
	size = size - 1
'''
#Oct to Dec
'''
onum = input("Enter Octal Number: ")
val = 0
size = len(onum) - 1
for num in onum:
	val = val + int(num)*2**size
	size = size - 1
print(val)

'''
#Hexa to Dec
'''
table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
hnum = input("Enter Hexadecimal Number: ").strip().upper()
val = 0
size = len(hnum) - 1
for num in hnum:
	val = val + table[num]*16**size
	size = size - 
print(val)

'''


