class ExprNode: #Tree node
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        self.next=None

class StackNode: #Stack Node
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack:
    def __init__(self):
        self.head=None

    def push(self, value):
        new_node = StackNode(value)
        new_node.next = self.head
        self.head = new_node
            
    def pop(self):
        if self.head:
            popped = self.head.value
            self.head = self.head.next
            return popped
        else:
            print("Stack underflow")

    def is_empty(self):
        return self.head is None

    def peek(self):
        if not self.head:
            return None
        return self.head.value

def precedence(op): #Defines the importance of operators
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0
    
        

def build_tree_from_infix(expr): #Use 2 stacks to build a tree
    operators = Stack()
    operands = Stack()

    for ch in expr:
        if ch == ' ':
            continue
        elif ch.isdigit():
            operands.push(ExprNode(ch))
        elif ch == '(':
            operators.push(ch)
        elif ch == ')':
            while not operators.is_empty() and operators.peek() != '(':
                op = operators.pop()
                right = operands.pop()
                left = operands.pop()
                node = ExprNode(op)
                node.left = left
                node.right = right
                operands.push(node)
            operators.pop()  #remove '('
        elif ch in '+-*/':
            while (not operators.is_empty() and
                   operators.peek() != '(' and
                   precedence(operators.peek()) >= precedence(ch)):
                op = operators.pop()
                right = operands.pop()
                left = operands.pop()
                node = ExprNode(op)
                node.left = left
                node.right = right
                operands.push(node)
            operators.push(ch)

    while not operators.is_empty():
        op = operators.pop()
        right = operands.pop()
        left = operands.pop()
        node = ExprNode(op)
        node.left = left
        node.right = right
        operands.push(node)

    return operands.pop()

def postorder_nonrecursive(root): #Reverse the Tree
    if not root:
        return []

    stack1 = Stack()
    stack2 = Stack()
    stack1.push(root)

    while not stack1.is_empty():
        node = stack1.pop()
        stack2.push(node)
        if node.left:
            stack1.push(node.left)
        if node.right:
            stack1.push(node.right)

    result = []
    while not stack2.is_empty():
        result.append(stack2.pop().value)

    return result
    

def evaluate_postfix(postfix_tokens): #Count the values
    stack = Stack()

    for token in postfix_tokens:
        if token not in '+-*/':
            stack.push(float(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.push(a+b)
            elif token == '-':
                stack.push(a-b)
            elif token == '*':
                stack.push(a*b)
            elif token == '/':
                stack.push(a/b)
    return stack.pop()

if __name__ == "__main__":
    expr = "3 + 2*(1+ 4* 5-6/3) - 2"
    print("Infix Expression:", expr)
    
    root = build_tree_from_infix(expr)
    postfix = postorder_nonrecursive(root)
    
    print("Postfix Expression:", ' '.join(postfix))
    print("Result =", evaluate_postfix(postfix))
