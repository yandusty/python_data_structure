from hashlib import new
from tkinter.messagebox import NO
from typing import List


class ListNode:
    def  __init__(self,newItem,nextNode:"ListNode"):
        self.item =newItem
        self.next =nextNode

class CircularLinkedListIterator:
    def __init__(self, alist):
        self.__head = alist.getNode(-1) #더미헤드 가져오기
        self.iterPosition = self.__head.next #0번노드
    def __next__(self):
        if self.iterPosition == self.__head: #순환 끝 0번노드부터 -> 더미헤드까지
            raise StopIteration
        else: # 현재 원소를 리턴하면서 다음원소로 이동
            item = self.iterPosition.item
            self.iterPosition = self.iterPosition.next
            return item

class CircularLinkedList:
    def __init__(self):
        self.__tail = ListNode("dummy",None)
        self.__tail.next = self.__tail
        self.__numItems = 0

    def __iter__(self):
        return CircularLinkedListIterator(self)


    def __findNode(self, x):
        __head = prev = self.__tail.next
        curr = prev.next
        while curr != __head:
            if curr.item == x:
                return(prev,curr)
            else:
                prev = curr;curr = curr.next
        return(None,None)

    def getNode(self, i:int):
        curr = self.__tail.next
        for index in range(i+1):
            curr = curr.next
        return curr
        

    def insert(self, i:int, newItem):
        if(i >=0 and i <=self.__numItems):
            prev = self.getNode(i-1)
            newNode = ListNode(newItem,prev.next)
            prev.next = newNode
            if i ==self.__numItems:
                self.__tail = newNode
            self.__numItems +=1
        else:
            print("index",i,": out of bound in insert()") #에러처리

    def append(self, newItem) ->None:
        newNode = ListNode(newItem,self.__tail.next)
        self.__tail.next = newNode
        self.__tail = newNode
        self.__numItems += 1

    def pop(self,*args):
        if self.isEmpty():
            return None

        if  len(args) != 0:
            i = args[0]

        if (i>=0 and i<= self.__numItems-1):
            prev = self.getNode(i-1)
            retItem =prev.next.item
            prev.next = prev.next.next
            if i ==self.__numItems -1:
                self.__tail = prev
            self.__numItems -= 1
            return retItem
        else:
            return None

    def remove(self,x):
        (prev,curr) = self.__findNode(x)
        if curr != None:
            prev.next = curr.next

            if curr == self.__tail:
                self.__tail = prev
            self.__numItems -=1
            return x
        else:
            return None

    def get(self,*args):
        if self.isEmpty():
            return None

        if len(args) != 0:
            i = args[0]
        if len(args) ==0 or i ==-1:
            i = self.__numItems -1
        if (i>=0 and i<=self.__numItems-1):
            return self.getNode(i).item
        else:
            return None

    def index(self,x):
        cnt = 0 
        for element in self:
            if element ==x:
                return cnt
            cnt += 1
        return None

    def isEmpty(self) ->bool:
        return self.__numItems == 0

    def size(self):
        return self.__numItems

    def clear(self):
        self.__tail = ListNode("dummy",None)
        self.__tail.next = self.__tail
        self.__numItems =0

    def count(self,x)->int:
        cnt = 0
        for element in self:
            if element ==x:
                cnt +=1
        return cnt

    def extend(self,a):
        for x in a:
            self.append(x)

    def copy(self):
        a = CircularLinkedList()
        for element in self:
            a.append(element)
        return a
    
    def reverse(self)->None:
        __head = self.__tail.next
        prev = __head; curr =prev.next; next = curr.next
        curr.next = __head; __head.next = self.__tail; self.__tail = curr
        for i in range(self.__numItems -1):
            prev = curr; curr = next; next = next.next
            curr.next = prev

    def sort(self):
        a =[]
        for element in self:
            a.append(element)

        a.sort()
        self.clear()
        for element in a:
            self.append(element)

    def printList(self):
        for element in self:
            print (element, end =' ')
        print()

