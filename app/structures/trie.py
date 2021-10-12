from string import ascii_lowercase


class Node:
    def __init__(self, value, size):
        self.value = value
        self.children = [None for _ in range(size)]


class Trie:
    SIZE = 26

    def __init__(self):
        self.root = Node('', self.SIZE)
        
    def insert(self, item_name):
        current_node = self.root
        for letter in item_name:
            index = ascii_lowercase.index(letter)
            if current_node.children[index] is None:
                current_node.children[index] = Node(letter, self.SIZE)
            current_node = current_node.children[index]
        
    def find(self, item):
        pass

