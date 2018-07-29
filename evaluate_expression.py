#!/usr/bin/python

from ds import Stack

def get_next_token(eq, indx):
    token = ''
    if eq[indx].isdigit():
        while indx < len(eq) and eq[indx].isdigit():
            token += eq[indx]
            indx += 1
    else:
        token = eq[indx]
        indx += 1

    return token, indx

def is_operand(token):
    return token.isdigit()

def convert_to_postfix(eq):
    paMap = {'^': {'p': 4, 'a': 'right'}, '*': {'p': 3, 'a': 'left'}, '/': {'p': 3, 'a': 'left'}, '+': {'p': 2, 'a': 'left'}, '-': {'p': 2, 'a': 'left'}, '(': {'p': 1, 'a': 'left'}}
    postfix = ''
    i = 0
    op_stack = Stack.Stack()

    while i < len(eq):
        token, i = get_next_token(eq, i)

        if token == ' ':
            continue
        elif is_operand(token):
            postfix += token + ' '
            continue
        else:
            if token == '(':
                op_stack.push(token)
            elif token == ')':
                while op_stack.peek() != '(':
                    postfix += op_stack.pop() + ' '
                op_stack.pop()
            else:
                #print "Stack Empty:", op_stack.isEmpty
                #print "Stack Top:", op_stack.peek()
                while not op_stack.isEmpty and (paMap[op_stack.peek()]['p'] > paMap[token]['p'] or (paMap[op_stack.peek()]['p'] == paMap[token]['p'] and paMap[token]['a'] == 'left') and op_stack.peek() != '('):
                    postfix += op_stack.pop() + ' '
                op_stack.push(token)

    # Expression parsing is complete, dump whatever is left in the stack into the postfix expression
    while not op_stack.isEmpty:
        postfix += op_stack.pop() + ' '

    return postfix

def calculate(a, b, operator):
    if operator == '+':
        return str(int(a) + int(b))
    elif operator == '-':
        return str(int(a) - int(b))
    elif operator == '*':
        return str(int(a) * int(b))
    elif operator == '/':
        return str(int(a) / int(b))
    elif operator == '^':
        return str(pow(int(a), int(b)))
    else:
        return None

def evaluate(eq):
    # Step 1: Convert to Postfix notation
    postfix_eq = convert_to_postfix(eq)

    #print "Postfix Notation:", postfix_eq

    # Evaluate the postfix expression
    operator = ''

    equation_list = postfix_eq.split()
    operand_stack = Stack.Stack()
    for token in equation_list:
        if is_operand(token):
            operand_stack.push(token)
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()

            result = calculate(operand1, operand2, token)
            if result == None:
                sys.exit(1)
            else:
                operand_stack.push(result)

    return postfix_eq, operand_stack.pop()

if __name__ == "__main__":
    expr = ["3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3"]#, "(3+1) * (16-7)", "3 + (6 - 1)"]
    for eq in expr:
        post_eq, res = evaluate(eq)
        print "Postfix expr: " + post_eq, " Result = ", res
