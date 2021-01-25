class ListNode:
	def __init__(self, val):
		self.value = val
		self.next = None
​
a = ListNode(1)
b = ListNode(2)
c = ListNode(4)
​
a.next = b
b.next = c
c.next = None
​
new_node = ListNode(3)  # What we're going to insert
​
cur = a
prev = None
​
while cur is not None:
	if cur.value > new_node.value:
		print(f"insert between nodes {prev.value} and {cur.value}")
		pre.next = new_node
        new_node.next = cur   # prev.next.next = cur -- either line works, they are identical
        break
​
	prev = cur          # "Chasing pointers", prev chases cur
	cur = cur.next

cur = a

while cur is not None:
    print(cur.value)
    cur = cur.next