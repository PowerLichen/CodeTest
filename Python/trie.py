# 연관 검색어 구조 구현

class Node:
    def __init__(self, key):
        self.count = 0
        self.key = key
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node("")

    def insert(self, word):
        word = word.lower()
        cur_node = self.head
        for ch in word:
            if ch not in cur_node.children:
                cur_node.children[ch] = Node(ch)
            cur_node.count += 1
            cur_node = cur_node.children[ch]
        cur_node.count += 1

    def search_count(self, word):
        word = word.lower()
        cur_node = self.head
        for ch in word:
            if ch not in cur_node.children:
                return 0
            cur_node = cur_node.children[ch]
        return cur_node.count


search_tree = Trie()

search_tree.insert("Hello")
search_tree.insert("Hell")
search_tree.insert("Hey")

print(search_tree.search_count("Hey"))
