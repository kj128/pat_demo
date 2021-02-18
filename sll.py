# Course: CS261 - Data Structures
# Student Name: Katrina Jang
# Assignment: 3
# Description: Implement methods for a singly linked list


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class SLNode:
    """
    Singly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with front and back sentinels
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.head = SLNode(None)
        self.tail = SLNode(None)
        self.head.next = self.tail

        # populate SLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        if self.head.next != self.tail:
            cur = self.head.next.next
            out = out + str(self.head.next.value)
            while cur != self.tail:
                out = out + ' -> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        cur = self.head
        while cur.next != self.tail:
            cur = cur.next
            length += 1
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.head.next == self.tail

    # ------------------------------------------------------------------ #

    def add_front(self, value: object) -> None:
        """
        Add new node to front of the linked list.
        """
        new_node = SLNode(value)
        new_node.next = self.head.next
        self.head.next = new_node

    def add_back(self, value: object) -> None:
        """
        Add node to back of the linked list.
        """
        # traverse the list to find last node
        self.add_back_help(value, self.head)

    def add_back_help(self, value, curr):
        """
        Helper method to add node to back of linked list.
        """
        # If we have transversed to the last node of the linked list, create new node and add to back
        if curr.next == self.tail:
            new_node = SLNode(value)
            curr.next = new_node
            new_node.next = self.tail
        else:
            self.add_back_help(value, curr.next)

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Insert node at index in linked list.
        """
        # If index is less than 0 or greater than the length of the list, raise exception
        if index < 0 or index > self.length():
            raise SLLException

        self.insert_at_index_help(index, value, self.head)

    def insert_at_index_help(self, index, value, curr):
        """
        Helper method to insert node at index in linked list.
        """
        # when we have finally reached the index, insert node
        if index == 0:
            new_node = SLNode(value)
            new_node.next = curr.next
            curr.next = new_node

        # otherwise, decrement index and transverse to next node
        else:
            self.insert_at_index_help(index - 1, value, curr.next)

    def remove_front(self) -> None:
        """
        Remove node at front of linked list.
        """
        # if linked list is empty, raise exception
        if self.is_empty():
            raise SLLException

        # otherwise, remove first node
        node = self.head.next
        self.head.next = node.next
        node.next = None

    def remove_back(self) -> None:
        """
        Remove node at back of linked list.
        """
        if self.is_empty():
            raise SLLException

        self.remove_back_help(self.head)

    def remove_back_help(self, curr):
        """
        Helper method to remove node at back of linked list.
        """
        # when you have reached the second to last node, change next pointer to tail and remove last node
        if curr.next.next == self.tail:
            last_node = curr.next
            curr.next = self.tail
            last_node.next = None
        else:
            self.remove_back_help(curr.next)

    def remove_at_index(self, index: int) -> None:
        """
        Remove node at index.
        """
        if index < 0 or index > (self.length() - 1):
            raise SLLException
        self.remove_at_index_help(index, self.head)

    def remove_at_index_help(self, index, curr):
        """
        Helper method to remove node at index.
        """
        # once you have reached the index, remove it
        if index == 0:
            node = curr.next
            curr.next = node.next
            node.next = None

        # otherwise, decrement the index and go to next node
        else:
            self.remove_at_index_help(index - 1, curr.next)

    def get_front(self) -> object:
        """
        Return value of first node.
        """
        if self.is_empty():
            raise SLLException

        return self.head.next.value

    def get_back(self) -> object:
        """
        Return value of last node.
        """
        if self.is_empty():
            raise SLLException

        return self.get_back_help(self.head)

    def get_back_help(self, curr):
        """
        Helper method to return value of last node.
        """
        # when you reach last node, return that value
        if curr.next == self.tail:
            return curr.value

        # otherwise, traverse to next node of linked list
        else:
            return self.get_back_help(curr.next)

    def remove(self, value: object) -> bool:
        """
        Remove node with value.
        """
        return self.remove_help(value, self.head)

    def remove_help(self, value, curr):
        """Helper method to remove node with value."""

        # if no nodes contain value return False
        if curr.next == self.tail:
            return False

        # if node has that value, remove node and return true
        elif curr.next.value == value:
            node = curr.next
            curr.next = node.next
            node.next = None
            return True
        else:
            return self.remove_help(value, curr.next)

    def count(self, value: object) -> int:
        """
        Return count of nodes with that value.
        """
        return self.count_help(value, self.head)

    def count_help(self, value, curr):
        """
        Helper method to return count of methods with that value.
        """

        # if no nodes in linked list contain that value, return count of 0
        if curr.next == self.tail:
            return 0

        # if node contains that value, add 1 to the count and go to next node
        elif curr.next.value == value:
            return 1 + self.count_help(value, curr.next)

        # if node does not contain value, move to next node
        else:
            return self.count_help(value, curr.next)


    def slice(self, start_index: int, size: int) -> object:
        """
        Return a new linked list of given size that starts at start index.
        """
        # if start index is not in range [0, n-1], or if size is less than 0 or greater than length of list,
        #   raise exception
        if start_index < 0 or start_index > self.length() - 1 or \
                size < 0 or start_index + size > self.length():
            raise SLLException

        # if linked list has no nodes, return empty linked list
        if size == 0:
            return LinkedList()

        # otherwise, get node at start index
        node = self.get_node_at_index(start_index)
        new_ll = LinkedList()                   # create new linked list
        self.slice_help(node, size, new_ll)     # create slice starting at start index of correct size
        return new_ll

    def slice_help(self, node, size, new_ll):
        """
        Helper method for slice method.
        """

        # while you have not finished making slice of appropriate size,
        #   add node to new Linkedlist object, decrease size, and go to next node
        if size != 0:
            new_ll.add_back(node.value)
            self.slice_help(node.next, size - 1, new_ll)

    def get_node_at_index(self, index: int):
        """
        Helper method to get node at index for slice method.
        """
        # if index is invalid, raise exception
        if index < 0 or index > (self.length() - 1):
            raise SLLException

        # get node at index
        return self.get_node_at_index_help(index, self.head)

    def get_node_at_index_help(self, index, curr):
        """
        Helper method for get node at index.
        """
        if index < 0:
            return curr

        # traverse list to get next node until you have reached index
        else:
            return self.get_node_at_index_help(index - 1, curr.next)


if __name__ == '__main__':
    pass
    """
    print('\n# add_front example 1')
    list = LinkedList()
    print(list)
    list.add_front('A')
    list.add_front('B')
    list.add_front('C')
    print(list)

    print('\n# add_back example 1')
    list = LinkedList()
    print(list)
    list.add_back('C')
    list.add_back('B')
    list.add_back('A')
    print(list)

    print('\n# insert_at_index example 1')
    list = LinkedList()
    test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    for index, value in test_cases:
        print('Insert of', value, 'at', index, ': ', end='')
        try:
            list.insert_at_index(index, value)
            print(list)

        except Exception as e:
            print(type(e))

    print('\n# remove_front example 1')
    list = LinkedList([1, 2])
    print(list)
    for i in range(3):
        try:
            list.remove_front()
            print('Successful removal', list)
        except Exception as e:
            print(type(e))

    print('\n# remove_back example 1')
    list = LinkedList()
    try:
        list.remove_back()
    except Exception as e:
        print(type(e))
    list.add_front('Z')
    list.remove_back()
    print(list)
    list.add_front('Y')
    list.add_back('Z')
    list.add_front('X')
    print(list)
    list.remove_back()
    print(list)

    print('\n# remove_at_index example 1')
    list = LinkedList([1, 2, 3, 4, 5, 6])
    print(list)
    for index in [0, 0, 0, 2, 2, -2]:
        print('Removed at index:', index, ': ', end='')
        try:
            list.remove_at_index(index)
            print(list)
        except Exception as e:
            print(type(e))
    print(list)

    print('\n# get_front example 1')
    list = LinkedList(['A', 'B'])
    print(list.get_front())
    print(list.get_front())

    list.remove_front()
    print(list.get_front())
    list.remove_back()

    try:
        print(list.get_front())
    except Exception as e:
        print(type(e))

    print('\n# get_back example 1')
    list = LinkedList([1, 2, 3])
    list.add_back(4)
    print(list.get_back())
    list.remove_back()
    print(list)
    print(list.get_back())

    print('\n# remove example 1')
    list = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(list)
    for value in [7, 3, 3, 3, 3]:
        print(list.remove(value), list.length(), list)

    print('\n# count example 1')
    list = LinkedList([1, 2, 3, 1, 2, 2])
    print(list, list.count(1), list.count(2), list.count(3), list.count(4))
    """

    print('\n# slice example 1')
    list = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = list.slice(1, 3)
    print(list, ll_slice, sep="\n")
    ll_slice.remove_at_index(0)
    print(list, ll_slice, sep="\n")

    print('\n# slice example 2')
    list = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", list)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Slice", index, "/", size, end="")
        try:
            print(" --- OK: ", list.slice(index, size))
        except:
            print(" --- exception occurred.")


