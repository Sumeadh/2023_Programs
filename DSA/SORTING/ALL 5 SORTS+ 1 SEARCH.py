#insertion sort
'''
L=[15.5,12,14.25,16.3,11,13.4]
print(L)
for i in range(1, len(L)):
    key=L[i]
    j=i-1
    while j>=0 and key< L[j]:
        L[j+1]=L[j]
        #print(i,'INTERMEDIATE L',L)
        j=j-1
    L[j+1]=key
print(L)
'''

#MERGE SORT COMBINING ALGORITHM
'''
a=[5,8,12,56]
b=[7,9,45,51]
len_a = len(a)
len_b = len(b)
sl=[]
i = j = 0

while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sl.append(a[i])
            i+=1
        else:
            sl.append(b[j])
            j+=1
print(sl)
'''     
#MERGE SORT MAIN ALGO
'''
def merge_sort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_lists(left, right, arr)


def merge_two_sorted_lists(a, b, arr):
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1

    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1

    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1


if __name__ == '__main__':
    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9, 8, 7, 2],
        [1, 2, 3, 4, 5]
    ]

    for arr in test_cases:
        merge_sort(arr)
        print(arr)
'''
#BINARY SEARCH(MY VERSION)
'''
def binary_search(l):
    global start, end
    mid = (start+end)//2
    if start>=end:
        print('element not found ')
    else:
        if l[mid]>searching_elmnt:
            end=mid
            binary_search(l)
        elif l[mid]<searching_elmnt:
            start=mid+1
            binary_search(l)
        else:
            print('element found at index', mid)
            return True 


lst=[5,10,2,17,22,6]
lst.sort()
print(lst)
start = 0
end = len(lst)
 searching_elmnt = int(input('enter the number to search'))
binary_search(lst)
'''  
# MERGE SORT QE
# SORT A DICTIONARY NESTED INSIDE A LIST BASED ON THE KEY OF THE DICTIONARY

# MY APPROACH
'''
def merge_sort(l,o):
    if  len(l)>1:
        mid=len(l)//2
        l_lst=l[:mid]
        r_lst=l[mid:]

        merge_sort(l_lst,o)
        merge_sort(r_lst,o)
        compare(l_lst, r_lst,o,l)
    return None
def compare(lft,rt,ord,lst):
    i=j=k=0
    if ord==True:
        while i < len(lft) and j < len(rt):
            if lft[i]<=rt[j]:
                lst[k]=lft[i]
                i+=1
                k+=1
            elif lft[i] >=rt[j]:
                lst[k] = rt[j]
                j += 1
                k += 1
            
        while i < len(lft):
            lst[k] = lft[i]
            i += 1
            k += 1
        while j < len(rt):
            lst[k] = rt[j]
            j += 1
            k += 1
    else:
        while i < len(lft) and j < len(rt):
            if lft[i] <= rt[j]:
                lst[k] = rt[j]
                j += 1
                k += 1
            elif lft[i] >= rt[j]:
                lst[k] = lft[i]
                i += 1
                k += 1
        while i < len(lft):
            lst[k] = rt[j]
            j += 1
            k += 1
        while j < len(rt):
           lst[k] = lft[i]
           i += 1
           k += 1
    return True

def sorter(ele, key='time_hours', ascending=True):
    for i in ele:
        main_lst.append(i[key])
    merge_sort(main_lst,ascending)

    for i in range(len(main_lst)):
        for j in range(len(main_lst)):
            if main_lst[i]==elements[j][key]:
                final_lst.append(elements[j])
    print(final_lst)

main_lst = []
final_lst=[]
elements = [
    {'name': 'vedanth',   'age': 17, 'time_hours': 1},
    {'name': 'rajab', 'age': 12,  'time_hours': 3},
    {'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
    {'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
]

sorter(elements)
'''

# you can use this to sort strings too

'''
def merge_sort(elements, key, descending=False):
    size = len(elements)

    if size == 1:
        return elements

    left_list = merge_sort(elements[0:size//2], key, descending)
    right_list = merge_sort(elements[size//2:], key, descending)
    sorted_list = merge(left_list, right_list, key, descending)

    return sorted_list


def merge(left_list, right_list, key, descending=False):
    merged = []
    if descending:
        while len(left_list) > 0 and len(right_list) > 0:
            if left_list[0][key] >= right_list[0][key]:
                merged.append(left_list.pop(0))
            else:
                merged.append(right_list.pop(0))

    else:
        while len(left_list) > 0 and len(right_list) > 0:
            if left_list[0][key] <= right_list[0][key]:
                merged.append(left_list.pop(0))
            else:
                merged.append(right_list.pop(0))

    merged.extend(left_list)
    merged.extend(right_list)
    return merged


if __name__ == '__main__':
    elements = [
        {'name': 'vedanth',   'age': 17, 'time_hours': 1},
        {'name': 'rajab', 'age': 12,  'time_hours': 3},
        {'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        {'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]

    sorted_list = merge_sort(elements, key='time_hours', descending=True)
    print(sorted_list)
'''
#SELECTION SORT
'''
def selection_sort(arr):
    size = len(arr)
    for i in range(size-1):
        min_index = i
        for j in range(min_index+1,size):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == '__main__':
    tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1,5,8,9],
        [234,3,1,56,34,12,9,12,1300],
        [78, 12, 15, 8, 61, 53, 23, 27],
        [5]
    ]
    for elements in tests:
        selection_sort(elements)
        print(elements)
 '''       
#quick sort  using hoare partition scheme
'''
def swap(a, b, arr):
    if a!=b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi-1)
        quick_sort(elements, pi+1, end)

def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start+=1

        while elements[end] > pivot:
            end-=1

        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)

    return end
elements = [11,9,29,7,2,15,28]
# elements = ["mona", "dhaval", "aamir", "tina", "chang"]
quick_sort(elements, 0, len(elements)-1)
print(elements)
'''
#QES
#BUBBLE AND INSERTION SORT QE
'''
inpt = input('on what basis do u wanna sort. 1) name,2) age, 3) time_hours')
elements = [
    {'name': 'vedanth',   'age': 17, 'time_hours': 1},
    {'name': 'rajab', 'age': 12,  'time_hours': 3},
    {'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
    {'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
]

for j in range(len(elements),0,-1):
    for i in range(j-1):
        if elements[i][inpt]>elements[i+1][inpt]:
            elements[i], elements[i+1] = elements[i+1], elements[i]

print(elements)
'''
# 1) recursion qe
'''
def happy_number(n):
    if n==1:
        print('the number is a happy number')
        return True
    elif n<10:
        print(n,'the number is NOT a happy number')
        return True
    else:
        happy_number(sum_sq_digits(n))
def sum_sq_digits(x):
    string=str(x)
    sumation=0
    for  i in string:
        sumation+=int(i)**2
    
    return sumation
    
number=int(input("enter the number"))
happy_number(number)

'''

'''
def convertString(str):

    # Write your code here
    l=str.split()
    str=''
    for i in range(len(l)):
        l[i]=l[i].capitalize()
        print(l,l[i])
        str+=l[i]
    return str
'''

def convertString(str):
    # Write your code here
    str=str[0].capitalize()+str[1:]
    cnt1=cnt2=0
    while cnt1<len(str):
        if str[cnt1]==' ':
            cnt2+=1
        elif cnt2>0:
            str=str[0:cnt1]+str[cnt1].capitalize()+str[cnt1+1:]
            cnt2=0
        cnt1+=1
    return str
print(convertString('ho my name is     sHanthi'))

