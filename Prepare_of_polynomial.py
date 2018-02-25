import logging
symbols = {"(", ")", "+", "-", "*", "/", "^"}


def get_list_of_variables(s):
    variables = list(set(filter(str.isalpha, s)))
    variables_text = 'Variables: ' + str(variables)
    logging.debug(variables_text)
    return variables


def delete_spaces(poly_str):
    '''
    Deletes spaces from the polynomial. Returns list.
    '''
    return [e for e in poly_str if e != ' ']


def add_multiple_symbol(poly_str):
    '''
    Adds multiple operand in initial expression.
    '''
    list1 = []
    for i in range(len(poly_str)):
        if i > 0 and (poly_str[i].isdigit() or poly_str[i] == '.')\
                and (poly_str[i-1].isdigit() or poly_str[i-1] == '.'):
            list1[-1] = list1[-1] + poly_str[i]
        elif i > 0 and ((poly_str[i-1] not in symbols and
                         poly_str[i] not in symbols) or
                        (poly_str[i] == '(' and
                         poly_str[i-1] not in symbols) or
                        (poly_str[i-1] == ')' and
                         poly_str[i] not in symbols) or
                        (poly_str[i-1] == ')' and poly_str[i] == '(')):
            list1.extend(('*', poly_str[i]))
        else:
            list1.append(poly_str[i])
    return list1


def count_powers(polynomial):
    i = 1
    powers_to_count = []
    while i < len(polynomial):
        if is_number(polynomial[i]) and polynomial[i-1] == '^':
            index1 = i - 2
            print(i)
            powers_to_count.append(int(polynomial[i-2]))
            powers_to_count.append(int(polynomial[i]))
            i += 1
            while i < len(polynomial)\
                    and (is_number(polynomial[i]) or polynomial[i] == '^'):
                if is_number(polynomial[i]):
                    powers_to_count.append(int(polynomial[i]))
                i += 1
            index2 = i
            final_number = involution(powers_to_count)
            x = polynomial
            polynomial = x[:index1]
            polynomial.append(str(final_number))
            polynomial.extend(x[index2:])
        i += 1
    return polynomial


def involution(powers_to_count):
    a = powers_to_count.pop()
    while len(powers_to_count) > 0:
        b = powers_to_count.pop()
        a = b ** a
    return a


def split_polynomial(polynomial):
    '''
    Gets polynomial in the form of the list, splits it on monomials.
    '''
    monomials = []
    monomial = []
    sign_in_the_begin = False
    if polynomial[0] in '-+':
        monomial.append(polynomial[0])
        sign_in_the_begin = True
    else:
        monomial.append('+')
    poly_iter = iter(polynomial)
    if sign_in_the_begin:
        next(poly_iter)
    for ch in poly_iter:
        if ch not in '-+':
            monomial.append(ch)
        else:
            monomials.append(monomial)
            monomial = [ch]
    monomials.append(monomial)
    return monomials


def adding_extra_brackets(polynomial):
    i = 0
    while i < len(polynomial):
        if i < len(polynomial) - 3\
           and (polynomial[i].isalpha() or is_number(polynomial[i]))\
           and polynomial[i+1] == '*' and polynomial[i+2] == '(':
            next = i+3
            polynomial.insert(i, '(')
            count = -1
            i += 3
            while count != 0:
                i += 1
                if polynomial[i] == ')':
                    count += 1
                elif polynomial[i] == '(':
                    count -= 1
            polynomial.insert(i, ')')
            i = next
        if i < len(polynomial) - 3 \
           and (polynomial[i + 2].isalpha() or is_number(polynomial[i]))\
           and polynomial[i + 1] == '*' and polynomial[i] == ')':
            next = i + 3
            polynomial.insert(i + 3, ')')
            count = -1
            while count != 0:
                i -= 1
                if polynomial[i] == '(':
                    count += 1
                elif polynomial[i] == ')':
                    count -= 1
            polynomial.insert(i, '(')
            i = next
        i += 1
    return polynomial


def is_number(s):
    '''
    Checks is s float number or not.
    '''
    try:
        float(s)
        return True
    except ValueError:
        return False
