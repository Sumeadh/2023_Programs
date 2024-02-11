import random as r
#1)Average of Marks
'''

d={'102122070':0,'102122071':0,'102122072':0,'102122073':0}
no_lst=[]
for i in range(0,101):
    no_lst.append(i)
for i in d:
    temp=[]
    for j in range(5):
        a=r.choice(no_lst)
        temp.append(a)
    d[i]=temp
print(d)

for i in d :
    print('The given student',i,'has the')
    print(' max mark',max(d[i]))
    print('min mark',max(d[i]))
    print('avg mark',sum(d[i])/5)
'''
#2)Latitude and Longitude
'''
import math as Math
city_dict={}
city_dict['trichy']=[78.8132,10.7589,] # [latitude,longitude]
city_dict['dindigul']=[77.9695,10.3624]
city_dict['palani']=[77.5161,10.4500]
city_dict['pollachi']=[10.6609,77.0048]

def dist(l1,l2):
    R = 6371 #Radius of the earth in km
    dLat = deg2rad(l2[0]-l1[0])
    dLon = deg2rad(l2[1]-l1[1])
    a = Math.sin(dLat/2) * Math.sin(dLat/2) +Math.cos(deg2rad(l1[0])) * Math.cos(deg2rad(l2[0])) * Math.sin(dLon/2) * Math.sin(dLon/2)
    c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a)); 
    d = R * c # Distance in km
    return d
    
def deg2rad(deg): 
  return deg * (Math.pi/180)
for i in city_dict:
    print(i)
    
c1=input('enter initial city')
c2=input('enter final city')
print('the distance between them is',dist(city_dict[c1],city_dict[c2]))
'''
#3)Denomination
'''
den=[500,200,100,50,20,10,5,2,1]
inp=int(input('enter the amount'))
d={}
op=d.copy()
sum=0
for i in den:
    d[i]=r.randint(0,10) #number of denomination available in i den
    n=inp//i # 2300//500
    print('denomination',i,'number of denominations',d[i])
    if n<=d[i]:
        op[i]=n
        d[i]=d[i]-n
        inp=inp%i
    elif d[i]!=0:
        op[i]=d[i]
        d[i]=0
        inp=inp%op[i]
    elif d[i]==0:
        op[i]=d[i]
        d[i]=0
print(d)
print(op)
'''
    

        
