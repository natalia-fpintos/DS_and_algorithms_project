import unittest

from app.structures.trie import Trie


class TrieTest(unittest.TestCase):
    def setUp(self) -> None:
        self.trie = Trie()

    def test_trie_insert(self):
        self.trie.insert('hi')
        self.assertEqual('h', self.trie.root.children[7].value)
        self.assertIsNone(self.trie.root.children[8])
        self.assertEqual('i', self.trie.root.children[7].children[8].value)
        self.assertIsNone(self.trie.root.children[7].children[7])


if __name__ == '__main__':
    unittest.main()
