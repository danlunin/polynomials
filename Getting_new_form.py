import Polynomial
import functools
import operator
import collections
from Prepare_of_polynomial import split_polynomial
import logging

OPERATORS = ["+", "-", "*", "/", "^"]


def get_new_form(polynomial, variables, EPS):
    '''
    Translates polynomial in correct form. Creates objects of class
    'Polynomial'.Returns list of such objects.
    '''
    dic = collections.defaultdict(lambda: 0)
    splitted = split_polynomial(polynomial)
    for mono in splitted:
        coefficients = []
        coefficients.append(1.0)
        powers = [0]*len(variables)
        power_zero = [0]*len(variables)
        i = 0
        while i < len(mono):
            if mono[i] == '-':
                coefficients.append(-1.0)
            elif mono[i] in variables:
                variable = mono[i]
                if i < len(mono)-1 and mono[i+1] == '^':
                    i += 2
                    power = float(mono[i])
                else:
                    power = 1.0
                powers[variables.index(variable)] += power
            elif is_number(mono[i]):
                coefficients.append(float(mono[i]))
            i += 1
        final_coef = functools.reduce(operator.mul, coefficients, 1.0)
        a = tuple(powers)
        if len(coefficients) == 1 and power_zero == powers:
            dic[a] = 0
        else:
            dic[a] += final_coef
        final_poly = Polynomial.Polynomial(dic, EPS)
    return final_poly


def calculate_polynomial(polynomial, variables, EPS):
    '''
    Partition of polynomial on polynomials.
    Inside brackets - single polynomial.
    '''
    polynomial_good_form = ['(']
    open_bracket = False
    close_bracket = False
    i = 0
    polynomial.insert(0, '(')
    polynomial.insert(1, '0')
    polynomial.insert(2, '+')
    polynomial.append(')')
    i += 1
    while i < len(polynomial):
        if polynomial[i] == '(' or polynomial[i] == ')':
            list1 = []
            next_pointer = i
            open_bracket = False
            close_bracket = False
            if polynomial[i] == '(':
                open_bracket = True
                if polynomial[i-1] in OPERATORS:
                    operand = polynomial[i-1]
                else:
                    polynomial_good_form.append('(')
                    i += 1
                    continue
                i -= 1
            elif polynomial[i] == ')':
                if polynomial[i-1] == ')':
                    polynomial_good_form.append(')')
                    i += 1
                    continue
                elif (i < len(polynomial)-2):
                        if polynomial[i+2] != '(' and polynomial[i+1] != '('\
                                and polynomial[i+1] != ')':
                            close_bracket = True
                            operand = polynomial[i+1]
                            if operand == '-':
                                operand = '+'
            i -= 1
            while i >= 0 and polynomial[i] != '(' and polynomial[i] != ')':
                list1.append(polynomial[i])
                i -= 1
            list1.reverse()
            if list1:
                polynomial_good_form.append(get_new_form(list1, variables,
                                            EPS))
            else:
                pass
            if open_bracket:
                polynomial_good_form.append(operand)
                open_bracket = False
                polynomial_good_form.append(polynomial[next_pointer])
            elif close_bracket:
                polynomial_good_form.append(polynomial[next_pointer])
                polynomial_good_form.append(operand)
                close_bracket = False
            else:
                polynomial_good_form.append(polynomial[next_pointer])
            i = next_pointer + 1
        else:
            i += 1
    string_polynomal_good_form = []
    for e in polynomial_good_form:
        if isinstance(e, Polynomial.Polynomial):
            string_polynomal_good_form.append(str(dict(e.monomials)))
        else:
            string_polynomal_good_form.append(str(e))
    string_polynomal_good_form = ''.join(string_polynomal_good_form)
    logging.debug(string_polynomal_good_form)
    return polynomial_good_form


def is_number(s):
    '''
    Checks is s float number or not.
    '''
    try:
        float(s)
        return True
    except ValueError:
        return False
