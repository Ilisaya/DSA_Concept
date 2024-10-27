class Node:
    def __init__(self, item=None, prev=None, next=None):
        self.item = item
        self.prev = prev
        self.next = next

class CDLL:
    def __init__(self,start=None):
        self.start =start

    def is_empty(self):
        return self.start is None

    def insert_at_first(self, data):
        n= Node(data)
        if self.is_empty():
            n.next =n.prev = n
            self.start = n
        else:
            last = self.start.prev
            n.next = self.start
            n.prev = last
            last.next = self.start.prev =n
            self.start = n

    def insert_last(self, data):
        if self.is_empty():
            self.insert_at_first(data)
        else:
            n= Node(data)
            last = self.start.prev
            n.next = self.start
            n.prev = last
            last.next = self.start.prev =n

    def search(self, data):
        if self.is_empty():
            return None
        temp = self.start
        while True:
            if temp.item == data:
                return temp
            temp = temp.next
            if temp == self.start:
                return None

    def insert_after(self,temp, data):
        if temp is None:
            return
        n= Node(data)
        n.next = temp.next
        n.prev = temp
        temp.next.prev =n
        temp.next =n

    def print_list(self):
        if self.is_empty():
            print("List is empty.")
            return
        temp = self.start
        while True:
            print(temp.item, end=' ')
            temp = temp.next
            if temp == self.start:
                break
        print()

    def delete_first(self):
        if self.is_empty():
            return
        if self.start.next == self.start:  # Only one node
            self.start = None
        else:
            last = self.start.prev
            self.start = self.start.next
            self.start.prev = last
            last.next = self.start

    def delete_last(self):
        if self.is_empty():
            return
        if self.start.next == self.start:  # Only one node
            self.start = None
        else:
            last = self.start.prev
            second_last = last.prev
            second_last.next = self.start
            self.start.prev = second_last

    def delete_item(self, data):
        if self.is_empty():
            return
        temp = self.start
        while True:
            if temp.item == data:
                if temp == self.start:
                    self.delete_first()
                elif temp == self.start.prev:
                    self.delete_last()
                else:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                return
            temp = temp.next
            if temp == self.start:
                break
