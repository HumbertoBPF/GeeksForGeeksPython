class TrieNode:

    def __init__(self):
        self.children = [None]*26

        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False

class Solution:
    def deleteKey(self, root, key):
        n = len(key)

        current_node = root
        # Prefix inside key
        inner_prefix = None

        for i in range(n):
            letter = key[i]

            letter_index = ord(letter) - ord('a')
            next_node = current_node.children[letter_index]
            # FIRST POSSIBILITY: the key does not exist in the trie
            if next_node is None:
                return

            if (i < n - 1) and next_node.isEndOfWord:
                inner_prefix = (next_node, i)

            current_node = next_node
        # FIRST POSSIBILITY: the key does not exist in the trie
        if not current_node.isEndOfWord:
            return
        # SECOND POSSIBILITY: the key is part of a prefix
        if len(current_node.children) > 0:
            current_node.isEndOfWord = False
            return
        # THIRD POSSIBILITY: the key contains a prefix
        if inner_prefix is not None:
            inner_prefix_node, inner_prefix_index = inner_prefix
            inner_prefix_node.children[inner_prefix_index] = None
            return
        # FOURTH POSSIBILITY: the key is not part of a prefix nor contains a prefix
        first_letter = key[0]
        first_index = ord(first_letter) - ord('a')
        root.children[first_index] = None
