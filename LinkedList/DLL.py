class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next
class DLL:
    def __init__(self, start=None):
        self.start = start
    
    def is_empty(self):
        return self.start is None
    
    def insert_at_first(self, data):
        n = Node(None, data, self.start)
        if not self.is_empty():
            self.start.prev = n
        self.start = n
    
    def insert_at_last(self, data):
        n = Node(None, data)
        if self.start is None:
            self.start = n
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
            n.prev = temp
    
    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None
    
    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(temp, data, temp.next)
            if temp.next is not None:
                temp.next.prev = n
            temp.next = n
    
    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=' ')
            temp = temp.next
        print()  # Print newline after the list
    
    def delete_first(self):
        if self.start is None:
            return
        if self.start.next is None:
            self.start = None
        else:
            self.start = self.start.next
            self.start.prev = None
    
    def delete_last(self):
        if self.start is None:
            return
        if self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            if temp.prev is not None:
                temp.prev.next = None
    
    def delete_item(self, data):
        if self.start is None:
            return
        if self.start.item == data:
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None
            return
        temp = self.start
        while temp is not None:
            if temp.item == data:
                if temp.next is not None:
                    temp.next.prev = temp.prev
                if temp.prev is not None:
                    temp.prev.next = temp.next
                return
            temp = temp.next
