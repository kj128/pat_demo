# Course: CS261 - Data Structures
# Student Name: Katrina Jang
# Assignment: 3
# Description: Implement methods for a stack using a singly linked list


from sll import SLNode, LinkedList


class StackException(Exception):
    """
    Custom exception to be used by MaxStack Class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MaxStack:
    def __init__(self):
        """
        Init new MaxStack based on Singly Linked Lists
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.sll_val = LinkedList()
        self.sll_max = LinkedList()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "MAX STACK: " + str(self.sll_val.length()) + " elements. "
        out += str(self.sll_val)
        return out

    def is_empty(self) -> bool:
        """
        Return True is Maxstack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.sll_val.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the MaxStack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.sll_val.length()

    # ------------------------------------------------------------------ #

    def push(self, value: object) -> None:
        """
        Add new element to top of stack with O(1) runtime complexity.
        """
        self.sll_val.add_front(value)       # add value to top of val stack

        # if max stack is empty or if current value in stack is greater than or equal to max stack,
        #   add to top of max stack
        if self.sll_max.is_empty() or self.sll_max.get_front() <= value:
            self.sll_max.add_front(value)

    def pop(self) -> object:
        """
        Remove top element of stack and returns it with O(1) runtime complexity.
        """

        # stack is empty, raise exception
        if self.is_empty():
            raise StackException

        removed_obj = self.sll_val.get_front()      # get object at top of val stack to return later
        self.sll_val.remove_front()                 # remove top element of val stack

        # if max stack is not empty, remove same object you popped off the val stack
        if self.sll_max.is_empty() is False and self.sll_max.get_front() == removed_obj:
            self.sll_max.remove_front()

        return removed_obj

    def top(self) -> object:
        """
        Return value of top element of stack without removing it with O(1) runtime complexity.
        """
        if self.is_empty():
            raise StackException

        # get and return top element of stack
        top_obj = self.sll_val.get_front()
        return top_obj


    def get_max(self) -> object:
        """
        Return max value in stack with O(1) runtime complexity.
        """
        if self.is_empty():
            raise StackException

        # return top element of max stack which is max value
        return self.sll_max.get_front()


# BASIC TESTING
if __name__ == "__main__":
    pass


    print('\n# push example 1')
    s = MaxStack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)

    print('\n# pop example 1')
    s = MaxStack()
    try:
        print(s.pop())
    except Exception as e:
        print("Exception:", type(e))
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    for i in range(6):
        try:
            print(s.pop())
        except Exception as e:
            print("Exception:", type(e))

    print('\n# top example 1')
    s = MaxStack()
    try:
        s.top()
    except Exception as e:
        print("No elements in stack", type(e))
    s.push(10)
    s.push(20)
    print(s)
    print(s.top())
    print(s.top())
    print(s)


    print('\n# get_max example 1')
    s = MaxStack()
    for value in [1, -20, 15, 21, 21, 40, 50]:
        print(s, ' ', end='')
        try:
            print(s.get_max())
        except Exception as e:
            print(type(e))
        s.push(value)
    while not s.is_empty():
        print(s.size(), end='')
        print(' Pop value:', s.pop(), ' get_max after: ', end='')
        try:
            print(s.get_max())
        except Exception as e:
            print(type(e))


