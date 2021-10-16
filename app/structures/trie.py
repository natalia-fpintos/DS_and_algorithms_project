import logging
from string import ascii_lowercase


LOG = logging.getLogger(__name__)


class Node:
    def __init__(self, value, size, is_item_name=False):
        self.value = value
        self.children = [None for _ in range(size)]
        self.is_item_name = is_item_name


class Trie:
    SIZE = 26

    def __init__(self):
        self.root = Node('', self.SIZE)
        
    def insert(self, item_name):
        current_node = self.root
        last_letter = len(item_name) - 1
        for position, letter in enumerate(item_name):
            index = ascii_lowercase.index(letter)
            if current_node.children[index] is None:
                current_node.children[index] = Node(letter, self.SIZE, position == last_letter)
            current_node = current_node.children[index]

    def find_node(self, prefix):
        current_node = self.root
        for letter in prefix:
            index = ascii_lowercase.index(letter)
            if current_node.children[index] is not None:
                current_node = current_node.children[index]
            else:
                LOG.info('No words found for prefix')
                return None
        return current_node

    def find_next_matching_item_name(self, prefix):
        current_node = self.find_node(prefix)
        if not current_node:
            return None

        word = prefix
        while not current_node.is_item_name:
            for i in range(self.SIZE):
                if current_node.children[i] is not None:
                    current_node = current_node.children[i]
                    word += current_node.value
                    break

        return word
