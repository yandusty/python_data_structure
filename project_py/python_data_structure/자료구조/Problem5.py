from re import L
from typing import List
from ListStack import *

class TwoStack_Queue:
    def __init__(self):
        self.__st = ListStack()
        self.__tst = ListStack()

    def __move_elements(self,st,tst ):
        while not st.isEmpty():
            tst.push(st.pop())

    def enqueue(self,x):
        self.__move_elements(self.__st,self.__tst)
        self.__st.push(x)
        self.__move_elements(self.__tst,self.__st)

    def dequeue(self):
        return self.__st.pop()

if __name__ == "__main__":
    st = TwoStack_Queue()
    st.enqueue(1)
    st.enqueue(2)
    st.enqueue(3)
    print(st.dequeue())
    print(st.dequeue())
    print(st.dequeue())