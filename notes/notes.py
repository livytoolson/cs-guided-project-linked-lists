# Linked Lists have good performance characteristics

class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
    
    def repr(self):
        # This comes into play when using print statements
        # Makes the print statement more readable / nicer
        return f'Node({repr(self.value)})'

head = None

def insert_at_front(val):
    global head

    # Make a new node
    new_node = Node(val)

    # Point new node next at head
    new_node.next = head

    # Point head to new node
    head = new_node

# insert_at_front(45)
# insert_at_front(88)

# print(head.value) # should print 88
# print(head.next) # should print 45
# print(head.next.next) # should print None
# print(head.next.next.next) # should print an error because we have walked off the end of our list

def print_list():
    global head

    # Set cur to head
    cur = head

    # Loop while cur is not None
    while cur is not None:
        # Print value at cur
        print(cur.value, end=" ")

        # Set cur to cur.next
        cur = cur.next

def delete_head():
    global head

    old_next = head.next
    head.next = None

    head = old_next

def delete_node(value):
    global head

    # Special Case: empty list
    if head is None:
        return

    # Special Case: delete the head
    if head.value == value:             # assumes head is not None because we took care of it in the case above
        delete_head()
        return

    # General case of deleting something in the middle
    # Need this to keep track of head and the value previous to the head
    prev = head
    cur = head.next                     # could also do cur = prev.next

    # Loop while cur is not None
    while cur is not None:              # Time Complexity: O(n)
        if cur.value == value:
            # print(f"Found it! {prev.value}, {cur.value}")
            prev.next = cur.next        # reassigning pointer
            cur.next = None             # get rid of pointer pointing to next node
            return                      # cur falls out of scope and node has nothing pointing to it - garbage collected

        # this moves both pointers down the list - chasing pointers
        cur = cur.next
        prev = prev.next
    # print("Didn't find it.")

insert_at_front(45)
insert_at_front(88)
insert_at_front(24)
insert_at_front(12)

print_list()

# delete_node(88)
delete_node(12)

# delete_head()

print_list()