import unittest

from app.structures.trie import Trie


class TrieTest(unittest.TestCase):
    def setUp(self) -> None:
        self.trie = Trie()
        self.trie.insert('courgette')
        self.trie.insert('cookie')
        self.trie.insert('cranberries')
        self.trie.insert('cantaloupe')
        self.trie.insert('cherries')

    def test_trie_insert(self):
        self.trie.insert('hi')
        self.assertEqual('h', self.trie.root.children[7].value)
        self.assertIsNone(self.trie.root.children[8])
        self.assertFalse(self.trie.root.children[7].is_item_name)
        self.assertEqual('i', self.trie.root.children[7].children[8].value)
        self.assertIsNone(self.trie.root.children[7].children[7])
        self.assertTrue(self.trie.root.children[7].children[8].is_item_name)

    def test_trie_find_match(self):
        result = self.trie.find_node('ca')
        self.assertEqual(self.trie.root.children[2].children[0], result)

    def test_trie_find_returns_next_possible_word(self):
        result = self.trie.find_next_matching_item_name('c')
        self.assertEqual('cantaloupe', result)


if __name__ == '__main__':
    unittest.main()
