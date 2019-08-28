class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        # ваш код
        if self.size() < 1:
            return None # если стек пустой
        return self.stack.pop(0)
            
    def push(self, value):
        self.stack.insert(0,value)
        # ваш код

    def FILO(self):
        # ваш код
        if stack.size() > 0:
            self.stack.pop(stack.size()-1)
            return stack
        else:
            return None # если стек пустой

    def peek(self):
        # ваш код
        if self.size() < 1:
            return None # если стек пустой
        return self.stack[0]

    def balanced(self, old_stack):
        new_stack = Stack()
        for i in range(len(old_stack)):
            if old_stack[i] == '(':
                new_stack.push('(')
            elif old_stack[i] == ')' and new_stack.peek() == '(':
                new_stack.pop()
        if new_stack.size() == 0:
            return 'balanced'
        else:
            return 'no balanced'

    def calculating(self, s0):
        s = s0.split()
        s2 = Stack()
        s1 = Stack()
        for i in range(len(s)):
            s1.push(s[i])
            if s[i] == "+":
                while s2.size() > 1:
                    s2.push(s2.pop() + s2.pop())
                s1.pop()
            elif s[i] == "*":
                while s2.size() > 1:
                    s2.push(s2.pop() * s2.pop())
                s1.pop()
            elif s[i] == "=":
                return s2.pop()
            else:
                s2.push(int(s1.pop()))
