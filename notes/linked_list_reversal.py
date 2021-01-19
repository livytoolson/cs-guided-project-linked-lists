# Linked List Reversal in place

# Nodes do not change, just their next pointers change
    # instead of pointers starting on left of list and point to the right,
    # they start on the right and point to the left 
# This will be an O(n) operation
# We want each node to point to the previous one rather than to the next one
# Need 3 pointers chasing each other

prev = cur
cur = next
next = cur.next