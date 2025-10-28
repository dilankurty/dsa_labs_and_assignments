class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedLists:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.tail = new_node
            self.head = new_node
    
    def insert_end(self, data):
        new_node = Node(data)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.tail = new_node
            self.head = new_node

    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            else:
                current_node = current_node.next
        return False
    
    def remove_beginning(self):
        if self.head:
            remove_data = self.head.data
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return remove_data
        else:
            return None
        
    def remove_end(self):
        if self.tail:
            remove_data = self.tail.data
            current_node = self.head
            if self.head == self.tail:
                self.head = None
                self.tail = None
                return remove_data
            while current_node:
                if current_node.next == self.tail:
                    self.tail = current_node
                    current_node.next = None
                    break
                else:
                    current_node = current_node.next
            return remove_data
        else: 
            return None
        
    def remove_at(self,data):
        current_node = self.head
        prev_node = None
        while current_node:
            if current_node.data == data:
                remove_data = current_node.data
                if current_node == self.head:
                    self.head = current_node.next
                    if not self.head:
                        self.tail = None
                elif current_node == self.tail:
                    self.tail = prev_node
                    prev_node.next = None
                else:
                    prev_node.next = current_node.next
                return remove_data
            else:
                prev_node = current_node
                current_node = current_node.next
        return None