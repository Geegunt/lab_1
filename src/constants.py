import re

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []


OPERATIONS: dict = {
'+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '**': lambda x, y: x ** y,
    '//': lambda x, y: x // y,
    '%': lambda x, y: x % y
}

def tokenizations(expression: str) -> dict:
    current_expression = expression.replace(('(', '').replace(')', ''))
    pattern = r'\d+(?:\.\d+)?|//|\*\*|[%+\-*/]'
    tokens = re.findall(pattern, current_expression)
    joined_tokens = ''.join(tokens)
    expression_no_spaces = current_expression.replace(' ', '')
    return tokens

def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False