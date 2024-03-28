class Minstack:
    def __init__(self) -> None:
        self.stack=[]
        self.minstack=[]
    def push(self, val) : 
        self.stack.append(val)
        minimum=min(val,self.minstack[-1] if self.minstack else val)
        self.minstack.append(minimum)
    def pop(self):
        self.stack.pop()
        self.minstack.pop()
    def top(self) -> int:
        return self.stack[-1]
    def getmin(self) -> int:
        return self.minstack[-1]
    

o = Minstack()
o.push(1)
o.push(2)
o.push(-3)
print(o.getmin())
o.pop()
print(o.getmin())

