from queue import PriorityQueue
b_stack = [[551, 431, 451, 981, 984, 401, 5109, 4210],
           [923, 491, 490], [4192, 491, 451, 987, 781, 901], 
           [9014, 10234, 1941],
           [111, 9982, 231, 921], [912, 4129, 9412, 412, 9012, 412, 519], 
           [9815, 9923], [414, 4912, 7891, 6893, 5891], [914, 52, 29, 905],
            [152, 123, 512, 598, 319]]

checkpoint=['A','B','C','D','E','F','G','H','I','J']

maze={'A':{'D':691,'B':43,'F':89},
      'B':{'A':43,'F':72,'G':39},
      'C':{'B':103,'E':201},
      'D':{'J':89},
      'E':{'J':70,'H':67},
      'F':{'A':89,'I':22,'H':56},
      'G':{'D':151,'J':95},
      'H':{'F':89,'C':19,'E':67},
      'I':{'F':22,'G':59,},
      'J':{'D':89}}

geog={'x0':{'x1':[44,'F']},
      'x1':{'x0':44,'x2':79,'A':53},
      'x2':{'x1':79,'x7':170,'x3':97.8},
      'x3':{'x4':62,'D':57,'x2':97.8},
      'x4':{'E':120,'x3':62,'x5':172},
      'x5':{'x4': 172,'x6':66,'x11':177},
      'x6':{'x5':66,'D':117,'C':97,'x7':81},
      'x7':{'x8':90,'B':98,'x2':170,'x6':81},
      'x8':{'A':109,'x9':246.248,'x7':90},
      'x9':{'B':80,'x10':86,'x8':246},
      'x10':{'C':76,'x11':66,'x9':86},
      'x11':{'x5':177,'E':330,'x10':66},
      'A':{'x1':53,'x8':109},
      'B':{'x7':98,'x9':80},
      'C':{'x10':76,'x6':97},
      'D':{'x3':57,'x6':117},
      'E':{'x4':120,'x11':330}}

battery_cnt=dict()
#mapping battery stack with each node
for i in range(len(b_stack)):
    battery_cnt[checkpoint[i]]=[b_stack[i],len(b_stack[i])]

def dijkstra(maze,start,end,count):
    open=PriorityQueue()# To Find the shortest node
    came_from={}#To trace out the shortest path
    h_score = {i: float("inf") for i in maze}# Initially h_score of all nodes are 
    print('h_score initially', h_score)
    open.put((0, start))
    open_hash=set()
    open_hash.add(start)
    current=None
    path=[]
    h_score[start]=0
    while current!=end:
        current=open.get()[1]
        neighbour_dict = maze[current]
        for neighbours in neighbour_dict:
            h_score_temp=h_score[current]+ neighbour_dict[neighbours]+2*count[current][1]
            if  h_score_temp< h_score[neighbours]:
                came_from[neighbours]=current #ex: C:B,B:A
                h_score[neighbours]=h_score_temp
                if neighbours not in open_hash:
                    open.put((h_score_temp,neighbours))
                    open_hash.add(neighbours)
    while current in came_from:
        path.append(current)
        current=came_from[current]
    path = [start]+path[::-1]
    battery_final_stack=[]
    print('h_score finally',h_score)
    print('The path needed to be followed is',path)
    print('The shortest distance to the point',end,'is',h_score[end])

    for i in path:
        battery_final_stack+=count[i][0]
    return battery_final_stack

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

    i = j = k = 0 # i for list1 , j for list2, k for merged list

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

final_stack=dijkstra(maze,'A','J',battery_cnt)
merge_sort(final_stack)
print('The final sorted array of batteries according to its mah',final_stack)