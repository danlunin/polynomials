from Getting_new_form import get_new_form, OPERATORS

OPERATORS_BRACKETS = ('(', ')', '+', '-', '*', '/', '^')
PRIORITY_DICT = {'(': 0, ')': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
OPS = {'+': lambda w1, w2, variables, EPS: w1 + w2,
       '*': lambda w1, w2, variables, EPS: w1 * w2,
       '/': lambda w1, w2, variables, EPS: w2.__div__(w1, variables),
       '^': lambda w1, w2, variables, EPS: w2.__pow__(w1, variables),
       '-': lambda w1, w2, variables, EPS:
           w1 * get_new_form(['-', '1'], variables, EPS) + w2}


def convert_to_postfix_notation(polynomial):
    '''
    Converts polynomial to postfix notatin.
    '''
    outputSeparated = []
    stack = []
    for c in polynomial:
        if c in OPERATORS_BRACKETS:
            if stack and c != '(':
                if c == ')':
                    s = stack.pop()
                    while s != '(':
                        outputSeparated.append(s)
                        s = stack.pop()
                elif get_priority(c) > get_priority(stack[len(stack)-1]):
                    stack.append(c)
                else:
                    while stack and get_priority(c)\
                                    <= get_priority(stack[-1]):
                        outputSeparated.append(stack.pop())
                    stack.append(c)
            else:
                stack.append(c)
        else:
            outputSeparated.append(c)
    outputSeparated.extend(stack[::-1])
    return outputSeparated


def get_priority(s):
    return PRIORITY_DICT.get(s, 4)


def final_move(notation, variables, EPS):
    '''
    Returns calculated polynomial as an instance of class 'Polynomial'.
    '''
    stack = []
    for e in notation:
        if e in OPERATORS:
            w1 = stack.pop()
            w2 = stack.pop()
            result = make_operation(e, w1, w2, variables, EPS)
            stack.append(result)
        else:
            stack.append(e)
    return stack[0]


def make_operation(e, w1, w2, variables, EPS):
    return OPS[e](w1, w2, variables, EPS)
