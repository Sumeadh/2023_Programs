#CREATION OF LINKED LIST
'''
class Node: #(node class is just for avoiding an extra variable head for each node)
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList: 
    def __init__(self): # initially head=none
        self.head = None

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head 
        self.head = new_node

    def add_last(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref = new_node

    def add_afternode(self,data,x):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.data is not x:
                if n.ref is not None:
                    n=n.ref
                else:
                    print('element not found')
                    break
            new_node.ref = n.ref
            n.ref=new_node
    
    def add_beforenode(self,data,x):
        new_node = Node(data)
        if self.head.data==x:
            new_node.ref=self.head
            self.head=new_node
        else:
            n = self.head
            while n.ref.data is not x:
                if n.ref is not None:
                    n = n.ref
                else:
                    print('element not found')
                    break
            new_node.ref = n.ref
            n.ref = new_node
    
    def delete_first(self):
        if self.head is None:
            print("Linked list is empty!")
        else:
            self.head=self.head.ref

    def delete_last(self):
        if self.head is None:
            print("Linked list is empty!")
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None

    def delete_mid(self,x):
        if self.head is None:
            print("Linked list is empty!")
        if self.head.data==x:
            self.head=self.head.ref
        else:
            n=self.head
            while n.ref is not None:
                if x == n.ref.data:
                    n.ref = n.ref.ref
                    break
                else:
                    n=n.ref
            if n.ref == None:
                print('\n','element not found')


    def print_LL(self): #2 condns, one for empty and one for non empty
        if self.head is None:
            print("Linked list is empty!")
        else:
            n = self.head # self. head contains the whole Class object which has data, ref as its attributes
            while n is not None: # at end n= None
                print(n.data,end='-->')
                n = n.ref
    
   
ll1=LinkedList()
ll1.add_begin(10)

ll1.add_last(20)
ll1.add_last(30)

ll1.add_begin(0)

ll1.add_afternode(15,10)
ll1.add_afternode(40,110)

ll1.add_beforenode(25, 0)
#ll1.add_beforenode(25,50)


ll1.print_LL()

ll1.delete_last()
ll1.delete_mid(22)
ll1.delete_first()
print()
ll1.print_LL()
#without Node class( node class is just for avoiding an extra variable head for each node)
# wrong code
#idea: using linked list as the object, i tried to connect nodes
#problem:but afer each creation i lost the connection with my prev node and i only got my last node as a result
'''
'''

class LinkedList:
    def __init__(self,data=None):
        self.head = None
        self.data = data
        self.ref = None
    
    def print_LL(self):
        if self.ref is None:
            print("Linked list is empty!")
        else:
            n = self.ref
            while n is not None:
                print(n.data, end='-->')
                n = n.ref

    def add_begin(self, data):
        new_node = LinkedList(data)
        new_node.ref = ll1.head
        self.ref = new_node
        #print(.data)

    def add_last(self, data):
        new_node = LinkedList(data)
        print(ll1.data)
        ll1.ref = new_node


ll1 = LinkedList(None)
ll1.print_LL()
ll1.add_begin(10)
ll1.add_last(20)
ll1.add_last(30)
ll1.add_begin(0)
ll1.print_LL()
'''
'''
class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(LinkedList):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is not None and list2 is not None:
            if list1.val > list2.val:
                n = list1
            else:
                n = list2

            while list1 is not None and list2 is not None:
                if list2.val > list1.val:
                    n.next = list2
                    list2 = list2.next

                else:
                    n.next = list1
                    list1 = list1.next
            else:
                if list1 is None:
                    while list2:
                        n.next = list2
                        list2 = list2.next

                if list2 is None:
                    while list1:
                        n.next = list1
                        list1 = list1.next

        else:
            if list1 is None:
                return list2
            else:
                return list1

        return n
ll=Solution()
ll1=Node()
'''
lists=[1,2,3]
def Listsolver(start,end):
    mid = (start+end)//2
    if mid > start:
        left = Listsolver(start, mid)
        right = Listsolver(mid, end)
        return merge_list(left, right)
    else:
        if lists[start] == [] or start==len(lists)-1:
                return []
        elif start+1 == end:
                 return lists[start]
        else:
                return merge_list(lists[start], lists[end])
Listsolver(0,len(lists))