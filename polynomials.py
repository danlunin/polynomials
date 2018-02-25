#!/usr/bin/env python3
import argparse
import sys
import logging
from final_calculation import check, compare
from Prepare_of_polynomial import get_list_of_variables


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('polynomial1', type=str,
                        help='first polynomial in string format')
    parser.add_argument('polynomial2', type=str,
                        help='second polynomial in string format')
    parser.add_argument('-e', metavar='eps',
                        action='store', type=float,
                        help='EPS given', default=1e-6)
    parser.add_argument('-d', help='debugging mode on', action='store_true')
    args = parser.parse_args()
    polynomial1 = args.polynomial1
    polynomial2 = args.polynomial2
    EPS = float(args.e)
    print('polynomial1: ', polynomial1)
    print('polynomial2: ', polynomial2)
    if args.d:
        a = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  ' \
            u'%(message)s'
        logging.basicConfig(format=a, level=logging.DEBUG)
    variables = get_list_of_variables(polynomial1 + polynomial2)
    poly1 = check(polynomial1, variables, EPS)
    poly2 = check(polynomial2, variables, EPS)
    if compare(poly1, poly2, EPS):
        print ('Yes')
        sys.exit(0)
    print ('No')
    sys.exit(1)


if __name__ == '__main__':
    main()
