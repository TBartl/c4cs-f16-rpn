#!/usr/bin/env python3

import operator

operators = {
    '+': add.add,
    '-': subtract.sub,
    '*': multiply.mul,
    '/': divide.truediv,
}

def calculate (arg):
    stack = list()
    for token in arg.split():
        try:
            stack.append(int(token))
        except ValueError:
            arg2 = stack.pop()
            arg1 = stack.pop()
            function = operators[token]
            result = function(arg1, arg2)
            stack.append(result)            

    if (len(stack) != 1):
        raise TypeError
    return stack.pop()

def main():
    while True:
        calculate(input("rpn calc> "))

if __name__ == '__main__':
    main()
