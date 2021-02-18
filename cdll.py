# Course: CS261 - Data Structures
# Student Name: Katrina Jang
# Assignment: 3
# Description: Implement methods for a circular doubly linked list


class CDLLException(Exception):
    """
    Custom exception class to be used by Circular Doubly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DLNode:
    """
    Doubly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        self.next = None
        self.prev = None
        self.value = value


class CircularList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with sentinel
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.sentinel = DLNode(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

        # populate CDLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'CDLL ['
        if self.sentinel.next != self.sentinel:
            cur = self.sentinel.next.next
            out = out + str(self.sentinel.next.value)
            while cur != self.sentinel:
                out = out + ' <-> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list

        This can also be used as troubleshooting method. This method works
        by independently measuring length during forward and backward
        traverse of the list and return the length if results agree or error
        code of -1 or -2 if thr measurements are different.

        Return values:
        >= 0 - length of the list
        -1 - list likely has an infinite loop (forward or backward)
        -2 - list has some other kind of problem

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """

        # length of the list measured traversing forward
        count_forward = 0
        cur = self.sentinel.next
        while cur != self.sentinel and count_forward < 101_000:
            count_forward += 1
            cur = cur.next

        # length of the list measured traversing backwards
        count_backward = 0
        cur = self.sentinel.prev
        while cur != self.sentinel and count_backward < 101_000:
            count_backward += 1
            cur = cur.prev

        # if any of the result is > 100,000 -> list has a loop
        if count_forward > 100_000 or count_backward > 100_000:
            return -1

        # if counters have different values -> there is some other problem
        return count_forward if count_forward == count_backward else -2

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.sentinel.next == self.sentinel

    # ------------------------------------------------------------------ #

    def add_front(self, value: object) -> None:
        """
        Add node to front of CDLL.
        """
        new_node = DLNode(value)
        new_node.prev = self.sentinel           # set prev pointer of new node to sentinel
        new_node.next = self.sentinel.next      # set next pointer of new node to sentinel.next

        self.sentinel.next = new_node           # set next pointer of sentinel to new node
        new_node.next.prev = new_node           # set prev pointer of original first node to point to new node

    def add_back(self, value: object) -> None:
        """
        Add node to back of CDLL.
        """
        new_node = DLNode(value)
        new_node.prev = self.sentinel.prev      # set prev pointer of new node to last node
        new_node.next = self.sentinel           # set next pointer of new node to sentinel

        self.sentinel.prev = new_node           # set prev pointer of sentinel to point to new node
        new_node.prev.next = new_node           # set next pointer of original last node to point to new node

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Insert node at index in CDLL.
        """
        if index < 0 or index > self.length():      # if index is invalid, raise exception
            print(index)
            raise CDLLException

        count = 0
        current = self.sentinel

        while count != index:                       # traverse linked list up to index
            current = current.next
            count += 1

        new_node = DLNode(value)                    # update prev and next pointer of inserted node
        new_node.prev = current
        new_node.next = current.next

        current.next = new_node
        new_node.next.prev = new_node

    def remove_front(self) -> None:
        """
        Remove node at front of CDLL.
        """
        if self.is_empty():
            raise CDLLException

        self.sentinel.next = self.sentinel.next.next
        self.sentinel.next.prev = self.sentinel

    def remove_back(self) -> None:
        """
        Remove node at back of CDLL.
        """
        if self.is_empty():
            raise CDLLException

        self.sentinel.prev.prev.next = self.sentinel
        self.sentinel.prev = self.sentinel.prev.prev

    def remove_at_index(self, index: int) -> None:
        """
        Remove node at index in CDLL..
        """
        if index < 0 or index >= self.length():         # if index is invalid
            raise CDLLException

        count = 0
        current = self.sentinel

        while count != index:                           # traverse linked list to index
            current = current.next
            count += 1

        if current.next == self.sentinel:
            raise CDLLException

        current.next.next.prev = current                # update pointers after removing node
        current.next = current.next.next

    def get_front(self) -> object:
        """
        Return value of first node in CDLL.
        """
        if self.is_empty():
            raise CDLLException

        node = self.sentinel.next
        front_val = node.value

        return front_val

    def get_back(self) -> object:
        """
        Return value of last node in CDLL.
        """
        if self.is_empty():
            raise CDLLException

        return self.sentinel.prev.value

    def remove(self, value: object) -> bool:
        """
        Remove node with value in CDLL.
        """

        if self.is_empty():
            return False

        current = self.sentinel.next                # set current to first node

        # if value of node is equal to value, remove node, update pointers, and return True
        while current != self.sentinel:
            if current.value == value:
                prev = current.prev
                prev.next = current.next
                current.next.prev = prev
                current.prev = None
                current.next = None
                return True

            current = current.next                  # if not equal to value, check next node

        return False                                # if value is not found in linked list, return False

    def count(self, value: object) -> int:
        """
        Return count of number of nodes with that value.
        """
        count = 0
        current = self.sentinel

        for index in range(self.length() + 1):
            if current.value == value:              # increment count if node contains that value
                count += 1
            current = current.next

        return count


    def swap_pairs(self, index1: int, index2: int) -> None:
        """
        Swap two nodes at two given indices.
        """
        length = self.length()

        # if index is invalid
        if (index1 < 0) or (index2 < 0) or (index1 >= length) or (index2 >= length):
            raise CDLLException

        # if index is the same, no change
        if index1 == index2:
            return

        # if index1 is greater than index2, swap them so that index2 > index 1
        elif index1 > index2:
            index1, index2 = index2, index1

        node1 = self.get_node_at_index(index1)          # get nodes at index 1 and 2
        node2 = self.get_node_at_index(index2)

        prev_of_node1 = node1.prev
        next_of_node1 = node1.next

        prev_of_node2 = node2.prev
        next_of_node2 = node2.next

        # If node1 and node2 are next to each other
        if index2 - index1 == 1:

            prev_of_node1.next = node2      # set next pointer of the prev of node1 to now point to node2
            node2.prev = prev_of_node1      # set prev pointer of node2 to now point to prev of node1

            node1.next = next_of_node2      # set next pointer of node1 to point to what was next of node2
            next_of_node2.prev = node1      # set prev pointer of what was next of node2 to now point to node1

            node2.next = node1              # make that node2 next pointer points to node1
            node1.prev = node2              # set prev of node1 point to node2

        else:
            prev_of_node1.next = node2      # establish prev and next pointers b/t previous of node1 and node2
            node2.prev = prev_of_node1

            node2.next = next_of_node1      # establish prev and next pointers b/t node2 and next of node1
            next_of_node1.prev = node2

            prev_of_node2.next = node1      # establish prev and next pointers b/t node1 and prev of node2
            node1.prev = prev_of_node2

            node1.next = next_of_node2      # establish prev and next pointers b/t node1 and next of node2
            next_of_node2.prev = node1


    def get_node_at_index(self, index):
        """
        Helper method to get node at index.
        """
        curr_index = 0
        current = self.sentinel.next

        while curr_index < index:           # keep traversing until you reach index, then get node
            current = current.next
            curr_index += 1

        return current



    def reverse(self) -> None:
        """
        Reverse a doubly linked list.
        """
        curr = self.sentinel

        for i in range(self.length() + 1):    # traverse linked list
            next_node = curr.next
            prev_node = curr.prev

            curr.next = prev_node             # set next pointer to point to prev node
            curr.prev = next_node             # set prev pointer to point to next node

            curr = next_node                  # go to next node

    def sort(self) -> None:
        """
        Implement a bubble sort to sort list in non-descending order.
        """
        length = self.length()
        curr = self.sentinel.next

        for i in range(length):                 # traverse the length of the linked list
            node1 = self.sentinel.next          # establish node1 and node2 (the node after node1)
            node2 = self.sentinel.next.next

            for j in range(length - i - 1):     # compare and swap from (length-index-1)

                # value on left is greater on the right, swap
                if node1.value > node2.value:

                    temp1 = node1
                    temp2 = node2

                    # swap node1 and node2
                    node1.next = node2.next     # update pointers so that node1's next node is what was node2's next node
                    node2.prev = node1.prev     # and that node2's previous node is what was node1's previous node

                    node1.prev.next = node2     # update node1's previous node to point to node2 now
                    node2.next.prev = node1     # update nodes'2 next node to have it's previous pointer point to node1 now

                    node1.prev = node2
                    node2.next = node1

                    node1 = temp2               # swap node1 and node2
                    node2 = temp1

                # else, update pointers to proceed to next nodes
                node1 = node1.next
                node2 = node2.next



    def rotate(self, steps: int) -> None:
        """
        Rotate a linked list by given steps.
        """

        length = self.length()

        # list is empty or only has one value, no change
        if length == 0 or length == 1:
            return

        # calculate relative position of k steps
        steps %= length

        # if k steps == 0, return
        if steps == 0:
            return

        # make tail point to last node, head point to first node
        tail = self.sentinel.prev
        head = self.sentinel.next

        # get tail node, get new_head and disconnect with previous node
        # connect tail node to original head node
        # change pointers

        # new head will start from (length - k steps)
        # attach tail -> next to head and find new head relative to tail position
        steps_to_new_head = length - steps
        tail.next = head                    # connect tail node with original head node with both pointers
        head.prev = tail

        while steps_to_new_head > 0:
            tail = tail.next                # get new tail
            steps_to_new_head -= 1

        new_head = tail.next                # new head is the next node after the new tail

        new_head.prev = self.sentinel       # establish new head as first node
        self.sentinel.next = new_head

        tail.next = self.sentinel           # establish new tail to point to sentinel
        self.sentinel.prev = tail



    def remove_duplicates(self) -> None:
        """
        Remove all numbers with duplicates in linked list so only unique numbers remain.
        """
        curr = self.sentinel.next

        while curr.next != self.sentinel:

            # if current value is equal to next value, but value after that is not equal to current value, remove
            #       both current and next value (if you only have 2 copies of that number)
            if curr.value == curr.next.value and curr.next.next.value != curr.value:
                self.remove_node(curr.next)
                self.remove_node(curr)

            # if current value equals next value, remove next value
            elif curr.value == curr.next.value:
                self.remove_node(curr.next)

            # traverse to next node
            else:
                curr = curr.next

    def remove_node(self, node):
        """Helper method to remove node."""
        node.next.prev = node.prev
        node.prev.next = node.next

    def odd_even(self) -> None:
        """
        Arrange linked list to have all nodes at odd indices, then all nodes at even indices.
        """

        odd = self.sentinel.next  # set odd as the head
        even = self.sentinel.next.next  # set even as head.next
        even_head = even  # set pointer to even for head of even linked list

        # get odd nodes, get even nodes, link the odd nodes with the even nodes
        while (even != self.sentinel and even.next != self.sentinel):
            odd.next = even.next        # get odd nodes
            odd = odd.next
            odd.next.prev = odd

            even.next = odd.next        # get even nodes
            even = even.next
            even.next.prev = even

        odd.next = even_head            # link odd nodes with even nodes

    def add_integer(self, num: int) -> None:
        """
        Add integer to linked list.
        """

        # given a linked list and integer

        # 1) Get last digit of integer (from right) to use later
        #       Get digit = number % 10
        #       Get next_num = number // 10

        # 2) Get last number of linked list (curr.prev.value)

        # 3) Add linked list number + digit to get a number to change linked list value
        #       next_num + next_linked_list_node_value = some number

        #       digit = some number % 10
        #       next_num = some number // 10

        # 4) If curr.prev == self.sentinel:
        #       check if number > 9:
        #           Allocate node and take number % 10 to get digit
        #           Get next_num == number // 10
        #           Proceed until number >= 9

        # Example:
        # [2, 0, 9, 0, 7] and 108   ->  [2, 1, 0, 1, 5]
        # 1) 108 + 7 (last node in linked list ) = 115
        #       115 % 10 = 5 (goes in linked list, change value)   [2, 0, 9, 0, 5]
        #       115 // 10 = 11 (used for next addition)
        #
        # 2) 11 + 0 (4th node in linked list) = 11
        #       11 % 10 = 1 (goes in linked list, change value)    [2, 0, 9, 1, 5]
        #       11 // 10 = 1 (used for next addition)
        #
        # 3) 1 + 9 (3rd node in linked list) = 10
        #       10 % 10 = 0 (goes in linked list)                   [2, 0, 0, 1, 5]
        #       10 // 10 = 1 (used for next addition)
        #
        # 4) 1 + 0 (2nd node in linked list) = 1
        #       1 % 10 = 1 (goes in linked list)                    [2, 1, 0, 1, 5]
        #       1 // 10 = 0 (used for next addition)
        #
        # 5) 0 + 2 (1st node in linked list) = 2
        #       2 % 10 = 2 (goes in linked list)                     [2, 1, 0, 1, 5]
        #       2 // 10 = 0 (used for last check)
        #
        # Check if number remaining is > 9 and check if node is self.sentinel:
        #     If greater than 9, then n % 10 to get digit.  Add new node to front for new digit.
        #     Get next number // 10 to get next number.
        #     Repeat until number is 9 or less, because you won't need any more nodes then.

        curr = self.sentinel.prev       # start at last node

        while curr != self.sentinel:
            sum = curr.value + num      # add node value and number
            digit = sum % 10            # get digit
            curr.value = digit          # place value into node

            num = sum // 10             # get next number

            curr = curr.prev            # traverse backwards in linked list

            # When you have reached self.sentinel, but num still has a number, create a node
            while curr == self.sentinel:
                if num == 0:
                    break

                if num <= 9:                # if number is 9 or last, add that node
                    self.add_front(num)
                    break

                else:                       # if greater than 9, add the digit, then repeat until less than 9
                    digit = num % 10
                    num = num // 10
                    self.add_front(digit)

        if self.is_empty():             # if linked list is empty, but you have an integer, add into linked list
            while num > 9:
                digit = num % 10
                self.add_front(digit)
                num = num // 10

            else:
                self.add_front(num)




if __name__ == '__main__':
    pass
    """
    
    print('\n# add_front example 1')
    lst = CircularList()
    print(lst)
    lst.add_front('A')
    lst.add_front('B')
    lst.add_front('C')
    print(lst)

    print('\n# add_back example 1')
    lst = CircularList()
    print(lst)
    lst.add_back('C')
    lst.add_back('B')
    lst.add_back('A')
    print(lst)
    
    
    print('\n# insert_at_index example 1')
    lst = CircularList()
    test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    for index, value in test_cases:
        print('Insert of', value, 'at', index, ': ', end='')
        try:
            lst.insert_at_index(index, value)
            print(lst)
        except Exception as e:
            print(type(e))

    
    print('\n# remove_front example 1')
    lst = CircularList([1, 2])
    print(lst)
    for i in range(3):
        try:
            lst.remove_front()
            print('Successful removal', lst)
        except Exception as e:
            print(type(e))
    

    print('\n# remove_back example 1')
    lst = CircularList()
    try:
        lst.remove_back()
    except Exception as e:
        print(type(e))
    lst.add_front('Z')
    lst.remove_back()
    print(lst)
    lst.add_front('Y')
    lst.add_back('Z')
    lst.add_front('X')
    print(lst)
    lst.remove_back()
    print(lst)

    print('\n# remove_at_index example 1')
    lst = CircularList([1, 2, 3, 4, 5, 6])
    print(lst)
    for index in [0, 0, 0, 2, 2, -2]:
        print('Removed at index:', index, ': ', end='')
        try:
            lst.remove_at_index(index)
            print(lst)
        except Exception as e:
            print(type(e))
    print(lst)
    

    print('\n# get_front example 1')
    lst = CircularList(['A', 'B'])
    print(lst.get_front())
    print(lst.get_front())
    lst.remove_front()
    print(lst.get_front())
    lst.remove_back()
    try:
        print(lst.get_front())
    except Exception as e:
        print(type(e))

    
    print('\n# get_back example 1')
    lst = CircularList([1, 2, 3])
    lst.add_back(4)
    print(lst.get_back())
    lst.remove_back()
    print(lst)
    print(lst.get_back())

    print('\n# remove example 1')
    lst = CircularList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(lst)
    for value in [7, 3, 3, 3, 3]:
        print(lst.remove(value), lst.length(), lst)




    print('\n# count example 1')
    lst = CircularList([1, 2, 3, 1, 2, 2])
    print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))

    print('\n# count example 2')
    lst = CircularList([1, 2, 2, 3, 1, 4, 3, 3, 1, 4, 2, 1, 2])
    print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))
    



    print('\n# swap_pairs example 1')
    lst = CircularList([0, 1, 2, 3, 4, 5, 6])
    test_cases = ((0, 6), (0, 7), (-1, 6), (1, 5),
                  (4, 2), (3, 3), (1, 2), (2, 1))

    for i, j in test_cases:
        print('Swap nodes ', i, j, ' ', end='')
        try:
            lst.swap_pairs(i, j)
            print(lst)
        except Exception as e:
            print(type(e))



    
    print('\n# reverse example 1')
    test_cases = (
        [1, 2, 3, 3, 4, 5],
        [1, 2, 3, 4, 5],
        ['A', 'B', 'C', 'D'],
    )
    for case in test_cases:
        lst = CircularList(case)
        lst.reverse()
        print(lst)

    print('\n# reverse example 2')
    lst = CircularList()
    print(lst)
    lst.reverse()
    print(lst)
    lst.add_back(2)
    lst.add_back(3)
    lst.add_front(1)
    lst.reverse()
    print(lst)

    print('\n# reverse example 3')


    class Student:
        def __init__(self, name, age):
            self.name, self.age = name, age

        def __eq__(self, other):
            return self.age == other.age

        def __str__(self):
            return str(self.name) + ' ' + str(self.age)


    s1, s2 = Student('John', 20), Student('Andy', 20)
    lst = CircularList([s1, s2])
    print(lst)
    lst.reverse()
    print(lst)
    print(s1 == s2)

    print('\n# reverse example 4')
    lst = CircularList([1, 'A'])
    lst.reverse()
    print(lst)



    print('\n# sort example 1')
    test_cases = (
        [1, 10, 2, 20, 3, 30, 4, 40, 5],
        ['zebra2', 'apple', 'tomato', 'apple', 'zebra1'],
        [(1, 1), (20, 1), (1, 20), (2, 20)]
    )
    for case in test_cases:
        lst = CircularList(case)
        print(lst)
        lst.sort()
        print(lst)


    """
    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    for steps in [1, 2, 0, -1, -2, 28, -100]:
        lst = CircularList(source)
        lst.rotate(steps)
        print(lst, steps)

    print('\n# rotate example 2')
    lst = CircularList([10, 20, 30, 40])
    for j in range(-1, 2, 2):
        for _ in range(3):
            lst.rotate(j)
            print(lst)

    print('\n# rotate example 3')
    lst = CircularList()
    lst.rotate(10)
    print(lst)

    """
    print('\n# remove_duplicates example 1')
    test_cases = (
        [1, 2, 3, 4, 5], [1, 1, 1, 1, 1],
        [], [1], [1, 1], [1, 1, 1, 2, 2, 2],
        [0, 1, 1, 2, 3, 3, 4, 5, 5, 6],
        list("abccd"),
        list("005BCDDEEFI")
    )

    for case in test_cases:
        lst = CircularList(case)
        print('INPUT :', lst)
        lst.remove_duplicates()
        print('OUTPUT:', lst)


    print('\n# odd_even example 1')
    test_cases = (
        [1, 2, 3, 4, 5], list('ABCDE'),
        [], [100], [100, 200], [100, 200, 300],
        [100, 200, 300, 400],
        [10, 'A', 20, 'B', 30, 'C', 40, 'D', 50, 'E']
    )


    for case in test_cases:
        lst = CircularList(case)
        print('INPUT :', lst)
        lst.odd_even()
        print('OUTPUT:', lst)


    
    print('\n# add_integer example 1')
    test_cases = (
        ([1, 2, 3], 10456),
        ([], 25),
        ([], 1276),
        ([2, 0, 9, 0, 7], 108),
        ([9, 9, 9], 9_999_999),
        ([3, 7, 2, 1, 9, 8], 19957)
    )
    for list_content, integer in test_cases:
        lst = CircularList(list_content)
        print('INPUT :', lst, 'INTEGER', integer)
        lst.add_integer(integer)
        print('OUTPUT:', lst)
    """