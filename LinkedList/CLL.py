class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class CLL:
    def __init__(self, last=None):
        self.last = last

    def is_empty(self):
        return self.last is None

    def insert_at_first(self, data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n

    def insert_at_last(self, data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n
            self.last = n

    def search(self, data):
        if self.is_empty():
            return None
        temp = self.last.next
        while True:
            if temp.item == data:
                return temp
            temp = temp.next
            if temp == self.last.next:
                break
        return None

    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(data, temp.next)
            temp.next = n
            if temp == self.last:
                self.last = n

    def print_list(self):
        if self.is_empty():
            return
        temp = self.last.next
        while True:
            print(temp.item, end=' ')
            temp = temp.next
            if temp == self.last.next:
                break
        print()

    def delete_first(self):
        if not self.is_empty():
            if self.last.next == self.last:
                self.last = None
            else:
                self.last.next = self.last.next.next

    def delete_last(self):
        if not self.is_empty():
            if self.last.next == self.last:
                self.last = None
            else:
                temp = self.last.next
                while temp.next != self.last:
                    temp = temp.next
                temp.next = self.last.next
                self.last = temp

    def delete_item(self, data):
        if self.is_empty():
            return

        # Deleting the first item
        if self.last.next.item == data:
            self.delete_first()
            return

        # Deleting a specific item
        temp = self.last.next
        while temp.next != self.last:
            if temp.next.item == data:
                temp.next = temp.next.next
                return
            temp = temp.next

        # Deleting the last item
        if self.last.item == data:
            self.delete_last()
