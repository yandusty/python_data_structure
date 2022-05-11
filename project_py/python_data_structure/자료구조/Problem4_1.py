from LinkedQueue import *

class TwoQueueStack:
    def  __init__(self):
        self.__q = LinkedQueue()
        self.__tq = LinkedQueue()
        self.cnt = 0

    def __move_elements(self,q,tq):
        for i in range(self.cnt-1):
            tq.enqueue(q.dequeue())

    def push(self,x):
        self.__q.enqueue(x)
        self.cnt +=1

    def pop(self):
        self.__move_elements(self.__q,self.__tq)
        retItem = self.__q.dequeue()
        self.__move_elements(self.__tq,self.__q)
        self.cnt -= 1
        return retItem

if __name__ == "__main__":
    st = TwoQueueStack()
    st.push(1)
    st.push(2)
    st.push(3)
    print(st.pop())
    print(st.pop())
    print(st.pop())