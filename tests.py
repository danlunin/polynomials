import collections
import unittest
from Prepare_of_polynomial import split_polynomial, get_list_of_variables,\
    delete_spaces, add_multiple_symbol, adding_extra_brackets, involution,\
    count_powers
from Calculator_of_polynomials import final_move, convert_to_postfix_notation
from Getting_new_form import calculate_polynomial, get_new_form
from final_calculation import compare, check


class MyTestCase(unittest.TestCase):

    def test_final_move2(self):
        poly1 = ['(', 'x',  '-',  '(', '1', ')', ')']
        dict1 = {(1, ): 1, (0, ): -1}
        self.assertEqual(dict1, (final_move(convert_to_postfix_notation(
            calculate_polynomial(poly1,
                                 ['x'])), ['x'], 1e-6)).monomials)

    def test_final_move3(self):
        poly1 = ['-', '(', '1', ')']
        poly2 = ['(', '-1', ')']
        variables = get_list_of_variables(poly1)
        dict1 = {(): -1}
        self.assertEqual(final_move(convert_to_postfix_notation(
                         calculate_polynomial(poly1, variables, 1e-6)),
                                    variables, 1e-6).monomials, dict1)

    def test_get_new_form6(self):
        polynomial = ['2', '*', '3', 'y', '^', '2', 'x', 'y', '^', '12', '-',
                      '3', '*', 'x']
        new_form = {(1.0, 14.0, 0): 6.0, (1.0, 0, 0): -3.0}
        self.assertEqual(new_form, get_new_form(polynomial, ['x', 'y', 'z'],
                         1e-6).monomials)

    def test_get_list_of_variables(self):
        poly = 'x*8 +9x -5z +y'
        variables = ['y', 'z', 'x']
        self.assertEqual(set(variables), set(get_list_of_variables(poly)))

    def test_get_new_form(self):
        poly1 = ['x', '^', '2', 'y', '^', '2', 'z', '+', '5', '*', 'x', '*',
                 'z']
        poly2 = ['y', '+', '5', 'z']
        new_form = {(2.0, 3.0, 1.0): 1.0, (2.0, 2.0, 2.0): 5.0,
                    (1.0, 1.0, 1.0): 5.0, (1.0, 0, 2.0): 25}
        self.assertEqual(new_form, (get_new_form(poly1, ['x', 'y', 'z'],
                                    1e-6)*(get_new_form(poly2,
                                                        ['x', 'y', 'z'],
                                                        1e-6))).monomials)

    def test_get_new_form2(self):
        poly12 = ['x', '+', 'y']
        poly21 = ['x', '-', 'y']
        new_form = {(2.0, 0, 0): 1, (0, 2.0, 0): -1}
        self.assertEqual(new_form, (get_new_form(poly12, ['x', 'y', 'z'],
                                    1e-6)*(get_new_form(poly21,
                                                        ['x', 'y', 'z'],
                                                        1e-6))).monomials)

    def test_get_new_form3(self):
        poly = ['x', '-', 'y']
        new_form = {(1.0, 0, 0): -1, (0, 1.0, 0): 1}
        self.assertEqual(new_form,
                         (get_new_form(poly, ['x', 'y', 'z'],
                                       1e-6)*get_new_form(['-', '1'],
                                                          ['x', 'y', 'z'],
                                                          1e-6)).monomials)

    def test_get_new_form4(self):
        poly1 = ['x', 'y', '^', '2',  '-', 'x', '*', '2', '*', 'y']
        poly2 = ['+', '5', 'y', '^', '2', '*', 'x', '-', '10']
        new_form = {(1.0, 2.0, 0): 6.0, (1.0, 1.0, 0): -2.0, (0, 0, 0): -10.0}
        self.assertEqual(new_form, (get_new_form(poly1, ['x', 'y', 'z'],
                                    1e-6) + (get_new_form(poly2,
                                                          ['x', 'y', 'z'],
                                                          1e-6))).monomials)

    def test_final_move(self):
        poly = ['(', '(', 'x', '+', 'z', ')', '*', '(', 'x', '-', 'y', ')',
                '+', '6', '*', 'x', 'y', ')', '*', '1']
        final_form = {(2.0, 0, 0): 1.0, (0, 1.0, 1.0): -1.0,
                      (1.0, 1.0, 0): 5.0, (1.0, 0, 1.0): 1.0}
        self.assertEqual(final_form,
                         (final_move(
                             convert_to_postfix_notation(calculate_polynomial(
                                 poly,
                                 ['x', 'y', 'z'], 1e-6)),
                          ['x', 'y', 'z'], 1e-6)).monomials)

    def test_final_move2(self):
        poly = ['(', 'x', '+', 'y', ')', '*', '(', 'x', '-', 'y', ')']
        final_form = {(2.0, 0, 0): 1.0, (0, 2.0, 0): -1.0}
        self.assertEqual(final_form,
                         (final_move(convert_to_postfix_notation(
                            calculate_polynomial(poly,  ['x', 'y', 'z'],
                                                 1e-6)),
                                     ['x', 'y', 'z'], 1e-6)).monomials)

    def test_get_new_form5(self):
        polynomial = ['1', '*', 'x', '+', '3', '*', 'y', '-', '5', '*', 'z']
        new_form = {(1.0, 0, 0): 1.0, (0, 1.0, 0): 3.0, (0, 0, 1): -5.0}
        self.assertEqual(new_form, get_new_form(polynomial, ['x', 'y', 'z'],
                                                1e-6).monomials)

    def test_split_polynomial(self):
        polynomial = ['1', '*', 'x', '+', '3', '*', 'y', '-', '5', '*', 'z']
        splitted = [['+', '1', '*', 'x'], ['+', '3', '*', 'y'],
                    ['-', '5', '*', 'z']]
        self.assertEqual(splitted, split_polynomial(polynomial))

    def test_split_polynomial(self):
        polynomial = ['-', '1']
        splitted = [['-', '1']]
        self.assertEqual(splitted, split_polynomial(polynomial))

    def test_delete_spaces(self):
        polynomial = '7 b    + 4      k *3/(5-4) '
        list_without_spaces = ['7', 'b', '+', '4', 'k', '*', '3', '/',
                               '(', '5', '-', '4', ')']
        self.assertEqual(list_without_spaces, delete_spaces(polynomial))

    def test_add_multiple_symbol1(self):
        polynomial = '3(742ab+6)a+b*a(8a+4)(a+2)'
        list_with_all_symbols = ['3', '*', '(', '742', '*', 'a', '*', 'b',
                                 '+', '6', ')', '*', 'a', '+', 'b', '*', 'a',
                                 '*', '(',
                                 '8', '*', 'a', '+', '4', ')', '*',
                                 '(', 'a', '+', '2', ')']
        self.assertEqual(list_with_all_symbols,
                         add_multiple_symbol(polynomial))

    def test_add_multiple_symbol2(self):
        polynomial = '72.5ab'
        list_with_all_symbols = ['72.5', '*', 'a', '*', 'b']
        self.assertEqual(list_with_all_symbols,
                         add_multiple_symbol(polynomial))

    def test_add_multiple_symbol3(self):
        polynomial = '3.5(72.4+6.4)'
        list_with_all_symbols = ['3.5', '*', '(', '72.4', '+', '6.4', ')']
        self.assertEqual(list_with_all_symbols,
                         add_multiple_symbol(polynomial))

    def test_add_multiple_symbol4(self):
        polynomial = '(6)a'
        list_with_all_symbols = ['(', '6', ')', '*', 'a']
        self.assertEqual(list_with_all_symbols,
                         add_multiple_symbol(polynomial))

    def test_add_multiple_symbol5(self):
        polynomial = '(6.56)(a^2)'
        list_with_all_symbols = ['(', '6.56', ')', '*', '(', 'a', '^', '2',
                                 ')']
        self.assertEqual(list_with_all_symbols,
                         add_multiple_symbol(polynomial))

    def test_adding_extra_brackets(self):
        poly2 = ['x', '+', '(', 'y', '-', 'x', '^', '2', ')', '*', 'y', '-',
                 'x']
        poly1 = ['x', '+', '(', '(', 'y', '-', 'x', '^', '2', ')', '*', 'y',
                 ')', '-', 'x']
        self.assertEqual(poly1, adding_extra_brackets(poly2))

    def test_adding_extra_brackets3(self):
        poly1 = ['(', 'x', '+', 'y', '*', '(', 'y', '-', 'x', '^', '2', ')',
                 '-', 'x', ')']
        poly2 = ['(', 'x', '+', '(', 'y', '*', '(', 'y', '-', 'x', '^', '2',
                 ')', ')', '-', 'x', ')']
        self.assertEqual(poly2, adding_extra_brackets(poly1))

    def test_adding_extra_brackets2(self):
        poly2 = ['(', 'x', '+', 'y', '*', '(', 'y', '-', 'x', '^', '2', ')',
                 '*', 'y', '-', 'x', ')']
        poly1 = ['(', 'x', '+', '(', '(', 'y', '*', '(', 'y', '-', 'x', '^',
                 '2', ')', ')', '*', 'y', ')', '-', 'x', ')']
        self.assertEqual(poly1, adding_extra_brackets(poly2))

    def test_adding_extra_brackets4(self):
        poly2 = ['(', 'x', '+', 'y', '*', '(', '(', 'y', '+', 'x', ')', '+',
                 '2', ')',  '-', 'x', ')']
        poly1 = ['(', 'x', '+', '(', 'y', '*', '(', '(', 'y', '+', 'x', ')',
                 '+', '2', ')', ')',  '-', 'x', ')']
        self.assertEqual(poly1, adding_extra_brackets(poly2))

    def test_compare(self):
        dict1 = {'a': 1.0000006, 'b': 1.0000008}
        dict2 = {'b': 1.0000008, 'a': 1.0000006}
        self.assertEqual(True, compare(dict1, dict2, 1e-6))

    def test_compare2(self):
        dict1 = {'a': 1.00005, 'b': 1.0000008}
        dict2 = {'b': 1.00008, 'a': 1.0000006}
        self.assertEqual(False, compare(dict1, dict2, 1e-6))

    def test_comapare3(self):
        dict1 = {'a': 1.00005, 'b': 1.0000008}
        dict2 = {'c': 1.00008, 'a': 1.0000006}
        self.assertEqual(False, compare(dict1, dict2, 1e-6))

    def test_comapare4(self):
        dict1 = {'a': 1.0000005, 'b': 1.0000008, 'k': 2}
        dict2 = {'b': 1.0000008, 'a': 1.0000006, 'd': 1}
        self.assertEqual(False, compare(dict1, dict2, 1e-6))

    def test_comapare5(self):
        dict1 = {'a': 1.0000005, 'b': 1.0000008, 'k': 2, 'l': 4}
        dict2 = {'b': 1.0000008, 'a': 1.0000006, 'd': 1}
        self.assertEqual(False, compare(dict1, dict2, 1e-6))

    def test_compare6(self):
        dict1 = {'a': 1.0000006, 'b': 1.0000008}
        dict2 = {'b': 1.0000008, 'a': 1.0000007}
        self.assertEqual(False, compare(dict1, dict2, 1e-7))

    def test_compare7(self):
        dict1 = {'a': 1.0000006, 'b': 1.0000008}
        dict2 = {'b': 1.0000008, 'a': 1.0000007}
        self.assertEqual(True, compare(dict1, dict2, 1e-6))

    def test_check(self):
        poly1 = 'x-y+z'
        dict1 = collections.defaultdict()
        dict1 = {(1.0, 0, 0): 1.0, (0, 1.0, 0): -1.0, (0, 0, 1.0): 1.0}
        self.assertEqual(dict1,  dict(check(poly1, ['x', 'y', 'z'], 1e-6)))

    def test_involution(self):
        list = [3, 2, 2, 1]
        result = 81
        self.assertEqual(result, involution(list))

    def test_count_powers(self):
        poly = ['x', '+', 'y', '+', '5', '^', '2']
        result_poly = ['x', '+', 'y', '+', '25']
        self.assertEqual(result_poly, count_powers(poly))

    def test_count_powers2(self):
        poly = ['-', '2', '^', '2', '^', '2', 'x', '+', 'y', '+', '5', '^',
                '2']
        result_poly = ['-', '16', 'x', '+', 'y', '+', '25']
        self.assertEqual(result_poly, count_powers(poly))

if __name__ == '__main__':
    unittest.main()
