class TrieNode:
    def __init__(self):
        self.children = {} #key = letter itself, values = trienodes it is pointing to
        self.endOfWord = False #marks end of word

class Trie:

    def __init__(self):
        self.root = TrieNode() #root itself contains no value, but will still point to letters

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode() #create new node when needed
            curr = curr.children[char] #move down trie as needed
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.endOfWord #return this instead of True, because the prefix might exist, but not as a word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
