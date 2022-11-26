# stack implementation 

# Creating a stack
def createStack():
    stack = []
    return stack

# creating an empty stack 
def isEmpty(stack):
    return len(stack) == 0

# adding items to the stack
def push(item, stack):
    stack.append(item)
    print("pushed item: " + item)

# removing an item from the stack
def pop(stack):
    if(isEmpty(stack)):
        return "stack is empty"
    return stack.pop()

stack = createStack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
print("popped item: " + pop(stack))
print("stack after popping an element: " + str(stack))