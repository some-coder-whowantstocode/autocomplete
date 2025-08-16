from trie.trieScript import Trie
    
TRIE = Trie()

def addWord(data):
    TRIE.insert(data["word"])

def completeWord(data):
    return TRIE.autocomplete(data["word"])