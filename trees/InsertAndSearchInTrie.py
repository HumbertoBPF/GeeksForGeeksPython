class TrieNode:

    def __init__(self):
        self.children = [None]*26

        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False


class Solution:
    # Function to insert string into TRIE.
    def insert(self, root, key):
        current_node = root

        for letter in key:
            insertion_index = ord(letter) - ord('a')
            next_node = current_node.children[insertion_index]

            if next_node is None:
                current_node.children[insertion_index] = TrieNode()
                next_node = current_node.children[insertion_index]

            current_node = next_node

        current_node.isEndOfWord = True


    # Function to use TRIE data structure and search the given string.
    def search(self, root, key):
        current_node = root

        for letter in key:
            searched_index = ord(letter) - ord('a')
            next_node = current_node.children[searched_index]

            if next_node is None:
                return False

            current_node = next_node

        return current_node.isEndOfWord
# code here