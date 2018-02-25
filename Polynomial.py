import collections


class Polynomial():
    def __init__(self, poly, eps):
        self.monomials = poly
        self.eps = eps
        self.simplify()

    def __str__(self):
        return str(self.monomials)

    def __repr__(self):
        return str(self.monomials)

    def __add__(self, poly2):
        for key in poly2.monomials:
            self.monomials[key] += poly2.monomials[key]
        return self.simplify()

    def __mul__(self, poly2):
        result_poly = collections.defaultdict(lambda: 0)
        for e1 in self.monomials:
            for e2 in poly2.monomials:
                e3 = tuple(x + y for (x, y) in zip(e1, e2))
                result_poly[e3] += self.monomials[e1] * poly2.monomials[e2]
        self.monomials = result_poly
        return self.simplify()

    def __div__(self, poly2, variables):
        for e2 in poly2.monomials:
            for e in self.monomials:
                devider = poly2.monomials[e2]
                self.monomials[e] = float(self.monomials[e] / devider)
        return self.simplify()

    def __pow__(self, second, variables):
        for e2 in second.monomials:
            for e in self.monomials:
                self.monomials[e] = self.monomials[e] ** second.monomials[e2]


    def simplify(self):
        list_for_delete = []
        for e in self.monomials:
            if abs(self.monomials[e]) < self.eps:
                list_for_delete.append(e)
        for e in list_for_delete:
            self.monomials.pop(e)
        return self
