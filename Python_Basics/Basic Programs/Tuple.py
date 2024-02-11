# Tuple

# 1)Time in 24 hrs--> 12 hrs format(Tuple)
'''
hrs=int(input('enter the hours'))
mint=int(input('enter the minutes'))
sec=int(input('enter the seconds'))
t=tuple()
m=''
if hrs>12:
    hrs_n=hrs-12
    m='PM'
else:
    hrs_n=hrs
    m='AM'
t=hrs_n,mint,sec,m
print(t)
'''
