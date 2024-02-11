#Getting inputs
maze=eval(input('Enter the maze in nested list format'))
row=len(maze)
column=len(maze[0])
   
count=0
start=[0,0]# first row first column--> start+(1,1)=Row,column
end=[row-1,column-1] # last row last column

#Breadth first search algorithm
que=[start]
while len(que)>0:
    current=que.pop(0)
    if current==end:
        count+=1
        continue
    right_neighbour=[current[0],current[1]+1]
    down_neighbour=[current[0]+1,current[1]]

    if current[1]+1<row:
        right_element=maze[right_neighbour[0]][right_neighbour[1]]
        if right_element!=1:
            que.append(right_neighbour)
    
    if current[0]+1<column:
        down_element=maze[down_neighbour[0]][down_neighbour[1]]
        if down_element!=1:
            que.append(down_neighbour)
print(count)
'''
[[0,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,0]]
[[0,1],[0,0]]
'''