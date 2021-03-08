def infix(expression):
    numStack = []
    opStack = []
    result = 0
    for i in expression:
        if i.isdigit():
            if len(opStack) != 0:
                value = numStack.pop() * int(i) if i == '*' else numStack.pop() / int(i)
            numStack.append(int(i))
        else:
            pass