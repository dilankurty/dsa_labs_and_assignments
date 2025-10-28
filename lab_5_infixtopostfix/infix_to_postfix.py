def precedence(op):
    if op == '^':
        return 3
    elif op in ('*', '/'):
        return 2
    elif op in ('+', '-'):
        return 1
    return -1

def infix_to_postfix(expression):
    stack = []
    result = []
    
    for char in expression:
        # Operand
        if char.isalnum():
            result.append(char)
        
        # Opening parenthesis
        elif char == '(':
            stack.append(char)
        
        # Closing parenthesis
        elif char == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            if stack:
                stack.pop()  # Remove '('
            else:
                print("Error: Mismatched parentheses.")
                return None
        
        # Operator
        else:
            while (stack and stack[-1] != '(' and
                   (precedence(char) < precedence(stack[-1]) or
                    (precedence(char) == precedence(stack[-1]) and char != '^'))):
                result.append(stack.pop())
            stack.append(char)
    
    # Pop all remaining operators
    while stack:
        if stack[-1] == '(':
            print("Error: Mismatched parentheses.")
            return None
        result.append(stack.pop())
    
    return ' '.join(result)

# input and output
if __name__ == "__main__":
    expression = input("Enter infix expression: ").replace(' ', '')
    postfix = infix_to_postfix(expression)

    if postfix:
        print("Postfix Expression:", postfix)
