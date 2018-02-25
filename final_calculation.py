from Calculator_of_polynomials import final_move, convert_to_postfix_notation
from Getting_new_form import calculate_polynomial
from Prepare_of_polynomial import adding_extra_brackets, add_multiple_symbol,\
                                  delete_spaces, count_powers
import sys
from Calculator_of_polynomials import OPERATORS


def check(poly, variables, EPS):
    try:
        checkOnExceptions(poly)
    except Exception as exc:
        print(exc)
        sys.exit(1)
    return final_move(convert_to_postfix_notation(
        calculate_polynomial(count_powers(adding_extra_brackets(
            add_multiple_symbol(
                             delete_spaces(poly)))),
                             variables, EPS)),
                      variables, EPS).monomials


class PolException(Exception):
    def __init__(self, message, pointer, polynomial):
        self.message = message
        self.pointer = pointer
        self.polynomial = polynomial

    def __str__(self):
        return self.message + ' in position: ' + \
               str(self.pointer) + ' in polynomial: ' + self.polynomial


def checkOnExceptions(poly):
        brackets = 0
        last_open_bracket = 0
        for i in range(len(poly)):
            if poly[i] == '(':
                brackets += 1
                last_open_bracket = i
            elif poly[i] == ')':
                brackets -= 1
                if brackets < 0:
                    raise PolException('Incorrect amount of brackets', i, poly)
            if i != len(poly) - 1:
                if poly[i] == '(' and poly[i+1] in OPERATORS\
                   and poly[i+1] != '-':
                    i += 1
                    raise PolException('Operator after open bracket', i+1,
                                       poly)
                if poly[i] in OPERATORS and poly[i+1] in OPERATORS:
                    raise PolException('Two operators', i+1, poly)
            if i == len(poly) - 1 and poly[i] in OPERATORS:
                raise PolException('Noting after operator', i, poly)
            if i > 0:
                if poly[i] == ')' and poly[i-1] in OPERATORS:
                    raise PolException('Operator before close bracket', i,
                                       poly)
        if brackets != 0:
            raise PolException('Incorrect amount of brackets',
                               last_open_bracket, poly)


def compare(dict1, dict2, EPS):
    if len(dict1) != len(dict2):
        return False
    for e1 in dict1:
        try:
            if abs(dict1[e1] - dict2[e1]) > EPS:
                return False
        except KeyError:
            return False
    return True
