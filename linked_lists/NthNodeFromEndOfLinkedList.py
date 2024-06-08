"""
	Your task is to return the data stored in
	the nth node from end of linked list.

	Function Arguments: head (reference to head of the list), n (pos of node from end)
	Return Type: Integer or -1 if no such node exits.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
"""

def getNthFromLast(head, n):
    i = 0
    pointer = head
    current_node = head

    while current_node is not None:
        # Only start moving the pointer when you are n positions from the head node
        if i >= n:
            pointer = pointer.next
        i += 1
        current_node = current_node.next
    # If there are not n items, return -1
    return - 1 if i < n else pointer.data
