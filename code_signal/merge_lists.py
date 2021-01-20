"""
Note: Your solution should have O(l1.length + l2.length) time complexity, since this is what you will be asked to accomplish in an interview.

Given two singly linked lists sorted in non-decreasing order, your task is to merge them. In other words, return a singly linked list, also sorted in non-decreasing order, that contains the elements from both original lists.

Example

For l1 = [1, 2, 3] and l2 = [4, 5, 6], the output should be
mergeTwoLinkedLists(l1, l2) = [1, 2, 3, 4, 5, 6];
For l1 = [1, 1, 2, 4] and l2 = [0, 3, 5], the output should be
mergeTwoLinkedLists(l1, l2) = [0, 1, 1, 2, 3, 4, 5].
Input/Output

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer l1

A singly linked list of integers.

Guaranteed constraints:
0 ≤ list size ≤ 104,
-109 ≤ element value ≤ 109.

[input] linkedlist.integer l2

A singly linked list of integers.

Guaranteed constraints:
0 ≤ list size ≤ 104,
-109 ≤ element value ≤ 109.

[output] linkedlist.integer

A list that contains elements from both l1 and l2, sorted in non-decreasing order.
"""

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def mergeTwoLinkedLists(l1, l2):
    head = ListNode(0)
    pointer = head
    
    while True:
        if l1 is None and l2 is None:
            break
        elif l1 is None:
            pointer.next = l2
            break
        elif l2 is None:
            pointer.next = l1
            break
        else:
            smaller_value = 0
            if l1.value < l2.value:
                smaller_value = l1.value
                l1 = l1.next
            else:
                smaller_value = l2.value
                l2 = l2.next
            
            new_node = ListNode(smaller_value)
            pointer.next = new_node
            pointer = pointer.next
        
    return head.next

def mergeTwoLinkedLists(l1, l2):
    dummyNode = ListNode(0)
    tail = dummyNode
    while True:
        if l1 is None:
            tail.next = l2
            break
        if l2 is None:
            tail.next = l1
            break
        if l1.value <= l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    return dummyNode.next