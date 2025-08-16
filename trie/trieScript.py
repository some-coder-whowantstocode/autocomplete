'''
trie structure 
[trie node]

trie node structure
{ch, is_end}

'''

class Node:
    def __init__(self, ch, nextNode):
        self.ch = ch
        self.next = (TrieNode() if nextNode else None) 
        self.is_end = (False if nextNode else True)

class TrieNode:
    def __init__(self):
        self.nodes = []
    
    def _insert(self,ch, end):
        node
        if end:
            node = Node(ch,False)
        else :
            node = Node(ch, True)
        self.nodes.append(node)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        elem = None
        # check if it exists in the trie
        for ch in word:
            elem = next((obj for obj in node.nodes if obj.ch == ch) , None)
            if elem is None or elem.is_end is True :
                # store it in trie
                newnode = Node(ch, True)
                node.nodes.append(newnode)
                elem = newnode
            node = elem.next
        newnode = Node("", False)
        elem.next.nodes.append(newnode)
        return node
    
    def autocomplete(self, prefix):
        node = self._traverse(prefix) 
        results = []
        self._dfs(node,prefix, results)
        return results
        
    def _traverse(self, word):
        node = self.root
        for ch in word:
            nextnode = next((obj.next for obj in node.nodes if obj.ch == ch) , None)
            if nextnode == None:
                return None
            node = nextnode
        return node
    
    def _dfs(self, node,prefix, results):
        if node is None:
            return
        for elem in node.nodes:
            newprefix = prefix + elem.ch
            if elem.is_end == True:
                results.append(newprefix)
                continue
            self._dfs(elem.next, newprefix, results)

    def showStructure(self,root):
        nodes = root.nodes
        for node in nodes:
            print(node.ch, end=" ")
            if node.is_end:
                print()
                continue
            self.showStructure(node.next)
