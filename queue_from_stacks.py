# Course: CS261 - Data Structures
# Student Name: Katrina Jang
# Assignment: 3
# Description: Implement methods for a queue from a stack


from max_stack_sll import MaxStack


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class Queue:
    def __init__(self):
        """
        Init new Queue based on two stacks
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.s1 = MaxStack()  # use as main storage
        self.s2 = MaxStack()  # use as temp storage

    def __str__(self) -> str:
        """
        Return content of queue in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "QUEUE: " + str(self.s1.size()) + " elements. "
        out += str(self.s1)
        return out

    def is_empty(self) -> bool:
        """
        Return True if queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.s1.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.s1.size()

    # ------------------------------------------------------------------ #

    def enqueue(self, value: object) -> None:
        """
        Adds new value to end of queue with O(1) runtime complexity.
        """
        self.s1.push(value)

    def dequeue(self) -> object:
        """
        Removes and returns value at beginning of queue with runtime complexity of not worse than O(n).
        """

        if self.s1.is_empty():
            raise QueueException

        # while s1 is not empty, pop top of stack and push to s2
        while self.s1.is_empty() is not True:
            self.s2.push(self.s1.pop())

        # pop top of s2 stack off to remove value at beginning of queue
        s2_elem = self.s2.pop()

        # while s2 is not empty, pop and push values back into s1
        while self.s2.is_empty() is not True:
            self.s1.push(self.s2.pop())

        return s2_elem


        # last_obj = self.s1.sll_val.get_back()
        #
        # #self.s1.pop()
        # return last_obj


"""
# BASIC TESTING
if __name__ == "__main__":
    pass

    print('\n# enqueue example 1')
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)

    print('\n# dequeue example 1')
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for i in range(6):
        try:
            print(q.dequeue(), q)
        except Exception as e:
            print("No elements in queue", type(e))
"""

