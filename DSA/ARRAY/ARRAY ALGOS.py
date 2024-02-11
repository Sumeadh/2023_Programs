# kadane's algo
'''
l=[4,-3,-2,2,3,1,-2,-3,6,-6,-4,2,1]
curr_sum=max_sum=l[0]
strt=end=pivot=0
for i in range (1,len(l)):
    curr_sum += l[i]
    if curr_sum>max_sum:
        max_sum=curr_sum
        start=pivot
        end=i
    if curr_sum<0:
        curr_sum=0
        pivot=i+1
print('The sub-array is :',l[start:end+1],'With a MAX SUM of',max_sum,sep='\n')
'''



'''
def maxSubSumKConcat(arr, n, k):
	# Write your code here.
	max_sum = arr[0]
	curr_sum = 0
	start = end = pivot = 0
	for i in range(0, n):
		curr_sum += arr[i]
		if curr_sum >= max_sum:
			max_sum = curr_sum
			start = pivot
			end = i
		if curr_sum < 0:
			curr_sum = 0
			pivot = i+1
	if start != 0 and end == n-1:
		cnt = 0
		while curr_sum > 0 and curr_sum >= max_sum:
			curr_sum += arr[cnt]
			max_sum = max(max_sum, curr_sum)
			cnt += 1
	if sum(arr)*k > max_sum:
		max_sum = sum(arr)*k
	return max_sum
	
	return max_sum


# 1 28 -10 25 33 -7
print(maxSubSumKConcat([-13, 44], 2, 10))
#print(maxSubSumKConcat([1 ,- 73, 11, 89, 93 ,17 ,- 71 ,35 ,69 ,- 23], 10, 8))
'''

def kadane_algo(l):
	max_sum = l[0]
	curr_sum=0
	trt = end = pivot = 0
	for i in range(0, len(l)):
		curr_sum += l[i]
		if curr_sum > max_sum:
			max_sum = curr_sum
			start = pivot
			end = i
		if curr_sum < 0:
			curr_sum = 0
			pivot = i+1

	return (start,end,max_sum)

def add_sum(l1, l2):
	if l1!=[]:
		return [l1[i] + l2[i] for i in range(len(l1))]
	else:
		return l2
	
def maxSumRectangle(arr, n, m):
	top=bottom=0
	max_sum=0
	for i in range(n):
		sum_array = []
		for j in range(i,n):
			sum_array= add_sum(sum_array,arr[j])
			(temp_left,temp_right,temp)= kadane_algo(sum_array)
			if temp>max_sum:
				max_sum=temp
				top=i
				bottom=j
				left=temp_left
				right=temp_right
	return [i[left:right+1] for i in arr[top:bottom+1]]
arr1 = [[1, 2, -1, -4, -20],
        [-8, -3, 4, 2, 1],
        [3, 8, 10, 1, 3],
        [-4, -1, 1, 7, -6]
        ]
a=maxSumRectangle(arr1,4 , 5)
print(a)