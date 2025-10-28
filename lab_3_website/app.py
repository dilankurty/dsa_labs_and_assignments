from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

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


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/touppercase', methods=['GET', 'POST'])
def uppercase():
    text = ""
    result = ""
    if request.method == "POST":
        text = request.form["text"]
        result = text.upper()
    return render_template("touppercase.html", text=text, result=result)

@app.route('/area_circle', methods=['GET', 'POST'])
def area_circle():
    area = None
    if request.method == 'POST':
        radius = float(request.form["radius"])
        area = np.pi * radius**2
    return render_template('area_circle.html', area="{:.2f}".format(area) if area is not None else None)

@app.route('/area_triangle', methods=['GET', 'POST'])
def area_triangle():
    area = None
    if request.method == 'POST':
        input_base = float(request.form["base"])
        input_height = float(request.form["height"])
        if input_base and input_height:
            area = 0.5 * input_base * input_height
    return render_template('area_triangle.html', area="{:.2f}".format(area) if area is not None else None)

@app.route('/infix-to-postfix_converter', methods=['GET', 'POST'])
def infix_to_postfix_converter():
    expression = ""
    postfix = ""
    if request.method == "POST":
        expression = request.form["expression"].replace(' ', '')
        postfix = infix_to_postfix(expression)
    return render_template("infix-to-postfix_converter.html", expression=expression, postfix=postfix)

if __name__ == "__main__":
    app.run(debug=True)
