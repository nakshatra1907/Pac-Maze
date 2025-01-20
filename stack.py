class Stack:
    def __init__(self):
        #YOU CAN (AND SHOULD!) MODIFY THIS FUNCTION
        self.st=[]
        
        pass
    # You can implement this class however you like
    def push(self,x):
        self.st.append(x)
    def popit(self):
        self.st.pop()

    def top(self):
        return self.st[-1]
    def givepath(self):
        return self.st