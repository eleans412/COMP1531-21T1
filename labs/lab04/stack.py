class Stack:
    def __init__(self):
        '''
        Generates the stack
        
        Parameters:
            self (object): The stack itself
        
        '''
        self.items = []

    def push(self, item):
        '''
        Pushes items onto the stack
        
        Parameters:
            item (str): the item to be pushed onto the stack
        
        Returns: 
            N/A
        '''
        self.items.append(item)

    def size(self):
        '''
        Calculates the size of the stack
        
        Parameters:
            self (object): the stack
        
        Returns: 
            size (int): The size of the stack
        '''
        return len(self.items)

    def pop(self):
        '''
        Pops item off the stack
        
        Parameters:
            None
        
        Returns: 
            N/A
        '''
        if len(self.items) == 0:
            raise Exception('Cannot pop, stack is empty')
        return self.items.pop()

	