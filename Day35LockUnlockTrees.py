from collections import deque

class LockingTree:
    class TreeNode:
        def __init__(self, num):
            self.locked = False
            self.user = -1
            self.val = num
            self.children = []
        def islocked(self):
            return self.locked
        
        def canUnlock(self,usr):
            return self.locked and self.user == usr
        
        def lock(self,usr):
            self.locked = True
            self.user = usr
        
        def unlock(self):
            self.locked = False
            self.user = -1
        

    def __init__(self, parent):
        self.valToNode = {}
        self.parent = parent
        self.initialize(parent)
        
    def initialize(self,parent):
        self.valToNode[0] = self.TreeNode(0)
        for i in range(1, len(parent)):
            self.valToNode[i] = self.TreeNode(i)
            self.valToNode[parent[i]].children.append(self.valToNode[i])
        

    def lock(self, num, user):
        node = self.valToNode[num]
        if not node.islocked():
            node.lock(user)
            return True
        return False
    

    def unlock(self, num, user):
        node = self.valToNode[num]
        if node.canUnlock(user):
            node.unlock()
            return True
        return False
        

    def upgrade(self, num, user):
        node = self.valToNode[num]
        if node.islocked():
            return False
        if self.hasLockedAncestors(num):
            return False
        if not self.hasLockedDescendent(num):
            return False
        node.lock(user)
        self.upgradeDescendents(num)
        return True

        
    def hasLockedAncestors(self, i):
        while i > 0:
            parentNode = self.valToNode[self.parent[i]]
            if parentNode.islocked():
                return True
            i = self.parent[i]
        return False
    
    def hasLockedDescendent(self, num):
        node = self.valToNode[num]
        queue = deque()
        for i in range(0, len(node.children)):
            queue.append(node.children[i])
            
        while len(queue) > 0:
            curr = queue.popleft()
            if curr.islocked():
                return True
            for i in range(0, len(curr.children)):
                queue.append(curr.children[i])
                
        return False
    
    def upgradeDescendents(self, num):
        node = self.valToNode[num]
        queue = deque()
        for i in range(0, len(node.children)):
            queue.append(node.children[i])
            
        while len(queue) > 0:
            curr = queue.popleft()
            curr.unlock()
            for i in range(0, len(curr.children)):
                queue.append(curr.children[i])
                
if __name__ == "__main__":
 obj = LockingTree([-1,0,0,1,1,2,2])
 param_1 = obj.lock(2,2)
 param_2 = obj.unlock(2,3)
 param_3 = obj.upgrade(2,2)
 param_4 = obj.lock(4,5)
 param_5 = obj.upgrade(0,1)
 param_6 = obj.lock(0,1)
