class Node:
    def __init__(self, val, k):
        self.right = None
        self.data = val
        self.left = None

# Function to delete a node from BST.
def deleteNode(root, X):
    node_to_delete, parent_node = search_node(root, X)

    if node_to_delete is None:
        return root
    # FIRST SCENARIO: the node to delete is a leaf
    if (node_to_delete.left is None) and (node_to_delete.right is None):
        # The root is a leaf, so it is the unique node of the tree
        if node_to_delete.data == root.data:
            return None

        # Delete the pointer referring to the node_to_delete from the PARENT NODE
        update_node_pointer(parent_node, node_to_delete, None)
        return root

    # SECOND SCENARIO: the node to delete has one child (left child)
    if (node_to_delete.left is not None) and (node_to_delete.right is None):
        # The root only has the left child, so I just need to return it!
        if node_to_delete.data == root.data:
            return node_to_delete.left

        # Make the PARENT NODE's pointer to refer to the unique child
        update_node_pointer(parent_node, node_to_delete, node_to_delete.left)
        return root

    # SECOND SCENARIO: the node to delete has one child (right child)
    if (node_to_delete.left is None) and (node_to_delete.right is not None):
        # The root only has the right child, so I just need to return it!
        if node_to_delete.data == root.data:
            return node_to_delete.right

        # Make the PARENT NODE's pointer to refer to the unique child
        update_node_pointer(parent_node, node_to_delete, node_to_delete.right)
        return root

    # Find the in-order successor
    current_node = node_to_delete.right

    while current_node.left is not None:
        current_node = current_node.left

    # current_node here is the in-order successor
    in_order_successor_value = current_node.data
    # Delete the in-order successor
    deleteNode(root, in_order_successor_value)
    # Replace the node_to_delete with in-order successor
    node_to_delete.data = in_order_successor_value
    return root

def update_node_pointer(parent_node, node_to_delete, replacer_node):
    parent_node_left = parent_node.left

    if (parent_node_left is not None) and (parent_node_left.data == node_to_delete.data):
        parent_node.left = replacer_node
        return

    parent_node_right = parent_node.right

    if (parent_node_right is not None) and (parent_node_right.data == node_to_delete.data):
        parent_node.right = replacer_node

    return

def search_node(root, X):
    current_node = root
    parent_node = None

    while current_node is not None:
        current_val = current_node.data

        if current_val == X:
            return current_node, parent_node

        parent_node = current_node

        if current_val > X:
            current_node = current_node.left
            continue

        current_node = current_node.right

    return None, None