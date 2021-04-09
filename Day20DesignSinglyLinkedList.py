class MyLinkedList:
    class LinkedListNode:
        def __init__(self, val):
            self.value = val;
            self.next = None;
        

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None;
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        reqNode = self.getNodeAtIndex(index);
        if reqNode == None:
            return -1;
        return reqNode.value;
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        newHead = self.LinkedListNode(val);
        newHead.next = self.head;
        self.head = newHead;

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        """
        curr = self.head;
        if curr == None:
            self.addAtHead(val);
            return;
        while(curr!= None and curr.next != None):
            curr = curr.next;
        curr.next = self.LinkedListNode(val);

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of   linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            self.addAtHead(val);
            return;
        reqNode = self.getNodeAtIndex(index-1);       
        if reqNode != None:
            newNode = self.LinkedListNode(val);
            save = reqNode.next 
            reqNode.next = newNode;
            newNode.next = save
            

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index == 0:
            self.head = self.head.next;
            return;
        prevNode = self.getNodeAtIndex(index-1);
        nodeToDelete = prevNode.next;
        if prevNode != None and nodeToDelete != None:
            prevNode.next = nodeToDelete.next;
        
        
    def getNodeAtIndex(self, index):
        if index == 0:
            return self.head;          
        curr = self.head;
        i = 0;
        while (i < index and curr!= None):
            curr = curr.next;
            i+=1;
        if i == index:
            return curr;
        return None;
        


