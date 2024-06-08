"""
	Function to merge two sorted lists in one
	using constant space.

	Function Arguments: head_a and head_b (head reference of both the sorted lists)
	Return Type: head of the obtained list after merger.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
"""

def sortedMerge(head1, head2):
    current_node_1 = head1
    current_node_2 = head2

    head_merged_list = None
    last_node_merged_list = None

    while (current_node_1 is not None) and (current_node_2 is not None):
        # If current_node_1 is the smallest element, set it as the next item of the linked list
        if current_node_1.data < current_node_2.data:
            # If the head has not been set yet, set it
            if last_node_merged_list is None:
                head_merged_list = current_node_1

            if last_node_merged_list is not None:
                last_node_merged_list.next = current_node_1

            last_node_merged_list = current_node_1
            current_node_1 = current_node_1.next
            continue
        # If the head has not been set yet, set it
        if last_node_merged_list is None:
            head_merged_list = current_node_2
        # If current_node_2 is the smallest element, set it as the next item of the linked list
        if last_node_merged_list is not None:
            last_node_merged_list.next = current_node_2

        last_node_merged_list = current_node_2
        current_node_2 = current_node_2.next
    # Add the remaining items to the linked list
    if current_node_1 is not None:
        last_node_merged_list.next = current_node_1

    if current_node_2 is not None:
        last_node_merged_list.next = current_node_2

    return head_merged_list
