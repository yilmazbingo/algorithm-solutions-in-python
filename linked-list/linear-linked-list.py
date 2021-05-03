# elements are not stored in contiguous order in memory
# searching takes O(n) in linked list
# insertions and deletions are cheaper in linked list.
class _Node:
    # if we defined slots, we dont have __dict__
    __slots__='_element','_next' #__slots__ has to be iterable, usually tuple
    def __init__(self,element,next):
        self._element=element
        self._next=next

class LinkedList:
    def __init__(self):
        self._head=None
        self._tail=None
        self._size=0
    def __len__(self):
        return self._size
    def isempty(self):
        return self._size==0
    def addlast(self,e):
        newest=_Node(e,None)
        if self.isempty():
            self._head=newest #not self._head=self._tail=newest check after else
        else:
            self._tail._next=newest
        self._tail=newest
        self._size+=1
    def display(self):
        p=self._head
        while p:
            print(p._element,end='-->')
            p=p._next
        print() # This will produce an invisible newline character, which in turn will cause a blank line to appear on your screen.
    def search(self,key): #O(n)
        p=self._head
        index=0
        while p:
            if p._element==key:
                return index
            p=p._next
            index+=1
        return -1
    def addfirst(self,key):
        newest=_Node(key,None)
        if self.isempty():
            self._head=newest
            self._tail=newest
        else:
            newest._next=self._head
            self._head=newest
        self._size+=1
    def addany(self,position,key): # watch 76th in leetcode for better visualization
        newest=_Node(key,None)
        p=self._head
        i=1 # because it is position not index
        while i<position-1:
            p=p._next
            i+=1
        newest._next=p._next  #if we linked to the newest first, we would lose the ref to the next
        p._next=newest
        self._size+=1
    def deletefirst(self):
        p=self._head._element # because we are returning the value not the node
        self._head=self._head._next #now all other class member recognizes this as
        self._size-=1
        if self.isempty():
            self._tail=None
        print(p._next._element)
        return p
    def deletelast(self):
        p=self._head
#         i=1
#         while i<len(self)-1:
#             p=p._next
#             i+=1
#         self._tail=p
#         p=p._next
#         e=p._element
#         self._tail._next=None
#         self._size-=1
#         return e
        while p._next:
            p=p._next
        e=self._tail._element
        p._next=None
        self._tail=p
        self._size-=1
        print("e",e)
        print("testing new tail",self._tail._element)
        return e
    def deleteany(self,position):
        p=self._head
        i=1
        while i<position-1:#this takes us to where we want
            i+=1
            p=p._next
        e=p._next._element
        p._next=p._next._next
        self._size-=1
        return e