import pickle as p
'''
fo=open('Sample.txt')
fr=fo.read()
print(fr)
fo2=open('Sample2.txt','w')
fo2.write(fr)
fo.close()
fo2.close()
'''
list=['sumeadhmass@gmail.com','6/09/2069']
d=dict()
d[9384403833]=list
fo=open('Binaryfile.bin','wb')
p.dump(d,fo)
fo2=open('Binaryfile.bin','rb')
fo2.seek(0)
while True:
    if fo2.tell():
        break
    else:
        fr2=p.load(fo2)
fo2.close()
