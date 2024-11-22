class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        d = self.trie

        for c in word:
            d = d.setdefault(c, {})
        
        d['.'] = '.'

    def search(self, word: str) -> bool:
        d = self.trie

        for c in word:
            d = d.get(c)
            if d is None:
                return False
        
        return '.' in d

    def startsWith(self, prefix: str) -> bool:
        d = self.trie

        for c in prefix:
            d = d.get(c)
            if d is None:
                return False

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)