from src.constants import Stack, tokenizations, isint

def calculator(expression: str, operations: dict):
    stack = Stack()
    tokens = tokenizations(expression)
    for token in tokens:
        if token in operations:
            try:
                if token == '//' or token == '%':
                    if isint(a) and isint(b):
                        finish = operations[token](b, a)
                        stack.push(finish)
                    else:
                        finish = operations[token](b, a)
                        stack.push(finish)
            except ZeroDivisionError:
                raise ZeroDivisionError("Division by zero")
            except IndexError:
                raise IndexError("Index out of range")
        else:



