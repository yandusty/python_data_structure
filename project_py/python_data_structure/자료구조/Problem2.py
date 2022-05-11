from LinkedQueue import *

class Checker:
    def __init__(self):
        self.__queue = LinkedQueue()

    def is_included(self,s):
        idx = s.find('$')

        for i in range(idx):
            self.__queue.enqueue(s[i])

        for i in range(idx +1, len(s)):
            prev = self.__queue.dequeue()
            curr = s[i]

            if prev != curr:
                return False
        return self.__queue.isEmpty()


if __name__ == "__main__":
    s = "abc$abc"
    check = Checker()
    rv = check.is_included(s)

    print(rv)