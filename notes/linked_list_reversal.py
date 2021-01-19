# Linked List Reversal in place

# Nodes do not change, just their next pointers change
    # instead of pointers starting on left of list and point to the right,
    # they start on the right and point to the left 
# This will be an O(n) operation
# We want each node to point to the previous one rather than to the next one
# Need 3 pointers chasing each other

def reverse(head_of_list):
    current_node = head_of_list
    previous_node = None
    next_node = None
​
    # Until we have 'fallen off' the end of the list
    while current_node:
        # Copy a pointer to the next element
        # before we overwrite current_node.next
        next_node = current_node.next
​
        # Reverse the 'next' pointer
        current_node.next = previous_node
​
        # Step forward in the list
        previous_node = current_node
        current_node = next_node
​
    return previous_node