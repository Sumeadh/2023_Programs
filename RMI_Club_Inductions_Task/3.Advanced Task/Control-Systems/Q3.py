def search(list,element):# gives the list of the connections with the given node
    n_lst=[]
    for n,i in enumerate(list,0):
        if element in i :
            indx=abs(1-i.index(element))
            n_lst.append([i[indx],n])
    return n_lst

def connection(element):
    for j in search(connections, element):
        if j[0] not in close and j[0] is not Node:
            connections[j[1]] = [Node, j[0]]
            open.remove(j[0])
            close.append(j[0])
            connection(j[0])
    return True

    
n=6#int(input('enter the n value'))
connections = [[0, 1], [0, 2], [2, 3], [1, 2],[1,3],[4,3]]#eval(input('enter the list'))
# [[0,1],[0,2],[0,3],[1,2],[1,3]]

Node=connections[0][0]

close=[]
open=[]
for i in range(n):
    if i is not Node:
        open.append(i)

#Checking for direct connection in node
temp=open.copy()
for i in temp:
    if [Node, i] in connections or [i, Node] in connections:
        open.remove(i)
        close.append(i)
# Checking for intermediate connections
for i in close:
    connection(i)
print(connections)

# Checking number of available connections that can be cut
cnt=0
for i in connections:
    if Node not in i:
        cnt+=1

#Final result

if cnt>=len(open):
    print(len(open))
else:
    print(-1)
