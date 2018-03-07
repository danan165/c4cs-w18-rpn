#!/usr/bin/env python3

import operator
from termcolor import colored, cprint

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}

def calculate(myarg):
    if myarg == "":
        exit(0)
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    cprint("Nice", 'red', 'on_white')
    cprint("Cool, dude", 'blue', 'on_yellow')
    while True:
        result = calculate(input("rpn calc> "))
        if result < 0:
            print("Result: ")
            cprint(resut, 'red', 'on_white')
        else:       
            print("Result: ")
            cprint(result, 'green', 'on_white')

if __name__ == '__main__':
    main()
