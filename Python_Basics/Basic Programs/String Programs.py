
#1)2 Word Merger
'''
w1=input('Enter the word')
w2=input('Enter the word')
w=''
l=min(len(w1),len(w2))    
for i in range(l):
    w+=w1[i]+w2[i]
if len(w1)-len(w2)>0:
    w+=w1[i+1:]
else:
    w+=w2[i+1:]
print(w)
'''

#2)Password generator
#' welcome to nitt'
'''
a=input('enter a given string')
pw1=''
pw2=''
l=a.split()
print(l)
for i in l:
    pw1+=i[0].upper()
    pw2+=str(len(i))
print(pw1+'@'+pw2)
'''

#3)Roll Number Decoder
'''
rno=input('enter a given string')
l=[]
decoded=[]
for i in range(0,len(rno),2):
    l.append(rno[i:i+2])
#print(l)
l[-2]=l[-2]+l[-1]
if l[0]=='10':
    decoded.append('btech')
if l[0]=='20':
    decoded.append('mtech')

if l[1]=='21':
    decoded.append('chemical')
if l[1]=='22':
    decoded.append('civil')
if l[1]=='23':
    decoded.append('cs')

decoded.append('year:20'+l[2])

decoded.append('roll no:'+l[3])

print(decoded)
'''

#4)Word Splitter
'''
word=input('Enter the word')
l=len(word)
print(word[l//2-1::-1]+'&'+word[:l//2-1:-1])
'''

#5)Train
'''
train = {
    "bullet train": "01",
    "commuter rail": "02",
    "express train": "03",
    "monorail": "04",
    "metro": "05",
    "shatabdi express": "06",
    "jan shatabdi express": "07",
    "duronto express": "08",
}

source = input("Enter the source point: ")
destination = input("Enter the destination point: ")
Type = input("Enter the type of train: ")
runDay = [item for item in input("Enter the list items (Enter like M T W Th F Sa S): ").split()]
s=source[:2]+destination[:2]+train.get(Type)+ str(len(runDay))
d=""
for i in runDay:
    d= d + str(i)
s= s+ d 
print("code:", s)
'''
#6)Word Searcher

