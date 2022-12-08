# Code Challenge: Recursion
# 1. Move items to the end of the list.
# define move_to_end() here
from node import LinkedList


def move_to_end(lst, val):
    result = []
    if len(lst) == 0:
        return lst
    if lst[0] == val:
        result += move_to_end(lst[1:], val)
        result.append(lst[0])
    else:
        result.append(lst[0])
        result += move_to_end(lst[1:], val)
    return result

# We first create an empty list variable called result - we will use this variable to store the output list.

# The base case checks if lst is empty by if len(lst) == 0. If it is empty, we return an empty list [].

# Next, we proceed to the recursive step. If the first item matches val, we need to extract the first item from lst and append it to the end of result. This is achieved by recursively calling result += move_to_end(lst[1:], val) first, and then appending the item using result.append(lst[0]). We use lst[1:] as the argument here in order to bring the input closer to the base case.

# In the else section, where the first item does NOT match val, we need to extract the first item from lst and append it to the beginning of result. This is achieved by appending the item using result.append(lst[0]), and then recursively calling result += move_to_end(lst[1:], val) second.


# Finally, the function returns result. After recursive calls have been returned from the call stack, result will be a copy of lst with every instance of val moved to the end of the list.
# Test code - do not edit
gemstones = ["Amber", "Sapphire", "Amber", "Jade"]
print(move_to_end(gemstones, "Amber"))

# 2. Delete i-th node from a linked list.

# Definition for singly-linked list node.
# class ListNode:
#     def __init__(self, value, next_node=None):
#         self.value = value
#         self.next_node = next_node

# define remove_node() here


def remove_node(head, i):
    if i < 0:
        return head
    if head == None:
        return None
    if i == 0:
        return head.next_node
    head.next_node = remove_node(head.next_node, i - 1)
    return head

# We take care of the edge case where i <= 0 because it’s impossible to remove a node of negative index. It’s good practice to address edge cases like this in your program to ensure it always functions as intended.

# We then define the two base cases:

# The first base case involves checking if head is None. If this is True, we know that we have reached the end of the linked list so we simply return a None object.
# The second base case involves checking if i == 0 and removing head from the linked list. The simplest way to remove head is by skipping over it and returning head.next_node instead.
# In order to iterate the linked list, we assign head.next_node to the recursive call. remove_node() is recursively called with arguments head.next_node and i - 1, which moves the input closer to the first and second base cases simultaneously.


# The last step is to return head. After all recursive calls on the call stack resolve, head will be the first node of the linked list with the ith node removed.
# Test code - do not edit
gemstones = LinkedList.LinkedList(["Amber", "Sapphire", "Jade", "Pearl"])
head = remove_node(gemstones.head, 1)
print(head.flatten())

# 3. Prepend and append to a string.
# define wrap_string() here


def wrap_string(str, n):
    result = ""
    if n <= 0:
        return str
    result += "<"
    result += wrap_string(str, n - 1)
    result += ">"
    return result

# Like the first challenge, we will use a variable called result to store the output string.

# In the base case, we check if n <= 0, in which case we simply return the unwrapped str.

# The recursive step happens between two iterative statements. < is prepended to result before the recursive call, and > is appended to result after the recursive call. In the middle, wrap_string() is called with n-1 to bring the input one step closer to the base case. The return value of this recursive call is concatenated to result as well.


# Using this approach, result will be wrapped layer by layer due to the order of the call stack returns. For example, when we call wrap_string("Pearl", 3), the call stack will return in this order: Pearl -> <Pearl> -> <<Pearl>> -> <<<Pearl>>>.
# Test code - do not edit
wrapped = wrap_string("Pearl", 3)
print(wrapped)
