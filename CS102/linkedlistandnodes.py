from LinkedList import LinkedList


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node


class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + "\n"
                current_node = current_node.get_next_node()
        return string_list

    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
            if next_node.get_value() == value_to_remove:
                current_node.set_next_node(next_node.get_next_node())
                current_node = None
            else:
                current_node = next_node


# In Python, we can implement the nth-last-node-finder function as such:


def nth_last_node(linked_list, n):
    current = None
    tail_seeker = linked_list.head_node
    count = 1
    while tail_seeker:
        tail_seeker = tail_seeker.get_next_node()
        count += 1
        if count >= n + 1:
            if current is None:
                current = linked_list.head_node
            else:
                current = current.get_next_node()
    return current


def generate_test_linked_list():
    linked_list = LinkedList()
    for i in range(50, 0, -1):
        linked_list.insert_beginning(i)
    return linked_list

# The exact variable names aren’t important, and the internal implementation could be written in a number of ways, but the important part is that we are able to complete this problem efficiently, in O(n) time (we must iterate through the entire list once), and O(1) space complexity (we always use only three variables no matter what size the linked list is: two pointers and a counter).


# Use this to test your code:
test_list = generate_test_linked_list()
print(test_list.stringify_list())
nth_last = nth_last_node(test_list, 4)
print(nth_last.value)


# Complete this function:

def find_middle(linked_list):
    fast = linked_list.head_node
    slow = linked_list.head_node
    while fast:
        fast = fast.get_next_node()
        if fast:
            fast = fast.get_next_node()
            slow = slow.get_next_node()
    return slow
# As with the nth-to-last solution, this solution has O(n) time complexity, and O(1) space complexity (we always use two variables no matter what size the linked list is: two pointers).


# Half-Speed

# Another equally valid solution is to move the fast pointer once with each loop iteration but only move the slow pointer every-other iteration:


def find_middle_alt(linked_list):
    count = 0
    fast = linked_list.head_node
    slow = linked_list.head_node
    while fast:
        fast = fast.get_next_node()
        if count % 2 != 0:
            slow = slow.get_next_node()
        count += 1
    return slow


def generate_test_linked_list(length):
    linked_list = LinkedList()
    for i in range(length, 0, -1):
        linked_list.insert_beginning(i)
    return linked_list


# Use this to test your code:
test_list = generate_test_linked_list(7)
print(test_list.stringify_list())
middle_node = find_middle(test_list)
print(middle_node.value)
