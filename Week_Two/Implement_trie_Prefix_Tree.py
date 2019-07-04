class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.isEnd = False
        self.link = dict()
        
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        p = self
        for w in word:
            if not w in p.link:
                p.link[w] = Trie()
            p = p.link[w]
    
        p.isEnd = True
                        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        p = self
        for w in word:
            if w in p.link:
                p = p.link[w]
            else:
                return False
        
        return p.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        p = self
        for w in prefix:
            if w in p.link:
                p = p.link[w]
            else:
                return False

        if any(list(p.link.values())) or p.isEnd:
            return True
        
        return False
    
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
