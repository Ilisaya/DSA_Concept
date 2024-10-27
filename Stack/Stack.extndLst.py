class Stack(list):
    def is_empty(self):
        return len(self)==0
    
    def push(self,data):
        self.append(data)
        
    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("Stack is empty")
            
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Stack is Empty")
        
    def size(self):
        return len(self)
    
    def insert(self,index,data):
        raise AttributeError("No Attribute 'insert' in the stack")
    
    def prnt(self):
        if self.is_empty():
            print("Stack is Empty")
        else:
            print("items is the stack (from top to bottom):")
            for item in reversed(self):
                print(item)
        