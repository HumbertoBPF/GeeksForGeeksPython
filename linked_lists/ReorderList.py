import math

def traverse_linked_list(head):
    current_node = head

    while current_node is not None:
        print(current_node.data)
        current_node = current_node.next

# Node Class
class node:
    def __init__(self, val):
        self.data = val
        self.next = None


# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None


class RecursiveSolution:

    def reorderList(self, head):
        n = self.get_length_list(head)

        if n < 3:
            return head

        return self.reorder(head, None, 0, n)

    def reorder(self, current_node, previous_node, i, n):
        if (n % 2 == 1) and (i == n // 2):
            node_1 = current_node.next
            previous_node.next = node_1
            current_node.next = None
            return current_node

        if (n % 2 == 0) and (i == n // 2 - 1):
            # Separating current_node -> node_1 from the input linked list and returning current_node as the head
            # of the output linked list
            node_1 = current_node.next
            node_2 = node_1.next
            previous_node.next = node_2
            node_1.next = None
            return current_node

        head_output_linked_list = self.reorder(current_node.next, current_node, i + 1, n)

        node_1 = current_node.next
        if previous_node is not None:
            # Separating current_node -> node_1 from the input linked list
            node_2 = node_1.next
            previous_node.next = node_2
        # Chaining current_node -> node_1 to head_output_linked_list (current_node -> node_1 -> head_output_linked_list)
        node_1.next = head_output_linked_list

        return current_node

    def get_length_list(self, head):
        current_node = head
        n = 0

        while current_node is not None:
            n += 1
            current_node = current_node.next

        return n


class Solution:

    def reorderList(self, head):
        n = self.get_length_list(head)

        if n < 3:
            return head

        current_node_1, current_node_2 = self.split_linked_list(head, n)
        current_node_2 = self.reverse_linked_list(current_node_2)
        # Popping the head of the first linked list
        next_node = current_node_1.next
        current_node_1.next = None
        tail_output = current_node_1
        current_node_1 = next_node
        # Pop a node from the linked lists, switching between them for each iteration
        for i in range(n - 1):
            if i % 2 == 0:
                next_node = current_node_2.next
                current_node_2.next = None
                tail_output.next = current_node_2
                current_node_2 = next_node
            else:
                next_node = current_node_1.next
                current_node_1.next = None
                tail_output.next = current_node_1
                current_node_1 = next_node

            tail_output = tail_output.next

        return head

    def split_linked_list(self, head, n):
        """
        Splits the linked list into two halves. For an odd number of items, the first half has an additional item.
        :param head: head of the linked list to be split
        :param n: number of items of the linked list
        :return: the resulting halves of the linked list
        """
        middle = math.ceil(n / 2)

        previous_node = None
        current_node = head

        for i in range(middle):
            previous_node = current_node
            current_node = current_node.next

        previous_node.next = None
        return head, current_node

    def reverse_linked_list(self, head):
        previous_node = None
        current_node = head

        while current_node is not None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        return previous_node

    def get_length_list(self, head):
        current_node = head
        n = 0

        while current_node is not None:
            n += 1
            current_node = current_node.next

        return n


node_0 = node(1)
node_1 = node(2)
node_2 = node(3)
node_3 = node(4)
node_4 = node(5)

node_0.next = node_1
node_1.next = node_2
node_2.next = node_3
node_3.next = node_4

solution = Solution()
new_head = solution.reorderList(node_0)

traverse_linked_list(new_head)
