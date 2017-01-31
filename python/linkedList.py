class Node:
    def __init__(self,data):
        self.next = None
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None

    def addAtBeginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def addAtEnd(self,data):
        temp = self.head
        if(temp == None):
            self.head = Node(data)
            return
        while(temp.next):
            temp = temp.next
        temp.next =  Node(data)

    def addAfter(self,prev,data):
        temp = self.head
        while(temp.data != prev and temp.next):
            temp = temp.next
        if(temp.next == None and temp.data != prev):
            print("Given value doesnt exist in the list")
            return
        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node

    def addBefore(self,next,data):
        temp = self.head
        new_node = Node(data)
        if(temp.data == next):
            self.addAtBeginning(data)
            return
        while(temp.next and temp.next.data != next):
            temp = temp.next
        if(temp.next == None):
            print("Given value doesn't exist in the list")
            return        
        new_node.next = temp.next
        temp.next = new_node

    def deleteNode(self,data):
        temp = self.head
        if(temp == None):
            print("list is empty")
            return
        if(temp.data == data):
            self.head = temp.next.next
            return
        while(temp.next.data != data and temp.next):
            temp = temp.next

        if(temp == None):
            print("Given value not found.")
            return
        temp.next = temp.next.next
            
    
    def printList(self):
        temp = self.head
        list = ""
        while temp:
            if(len(list) != 0):
                list = list + "->"
            list = list + str(temp.data)
            temp = temp.next
        print(list)
    
    def length(self):
        temp = self.head
        count = 0
        while(temp!=None):
            count = count+1
            temp = temp.next
        return count

    def lengthRecursive(self,node):     
        if(node == None):
            return 0
        return 1 + self.lengthRecursive(node.next)

    def getLengthRecusrsive(self):
        return self.lengthRecursive(self.head) 

    def swapTwoKeysLink(self,key1,key2):
        temp = self.head
        foundKey1 = False
        foundKey2 = False
        while(temp.next != None):
            if(temp.next.data == key1 and not foundKey1):
                node1parent = temp
                node1 = temp.next
                foundKey1 = True
            elif(temp.next.data == key2 and not foundKey2):
                node2 = temp.next
                node2parent = temp
                foundKey2 = True
            temp = temp.next

        if(foundKey1 and foundKey2):
            node1parent.next = node2
            tempnode = node2.next
            node2.next = node1.next
            node2parent.next = node1
            node1.next = tempnode          


        elif foundKey1:
            print(str(key2) + "not found")
        elif foundKey2:
            print(str(key1)+" not found")
        

if __name__=="__main__":
    list = LinkedList()
    list.addAtEnd(78)
    list.addAtBeginning(1)
    list.addAtBeginning(2)
    list.addAtBeginning(2)
    list.addAtBeginning(34)
    list.addAtBeginning(3)
    list.addAtEnd(45)
    list.addAtBeginning(4)
    list.addAfter(45,65)
    list.addAtBeginning(5)
    list.addBefore(34,456)
    list.addAtBeginning(6)
    list.deleteNode(456)
    list.addAtBeginning(7)
    list.printList()
    list.swapTwoKeysLink(34,78)
    list.printList()
    print("Length of list : " + str(list.getLengthRecusrsive()))