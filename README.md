# polynomials
2 polynomials from severl variables in mathematical form (some signs of opertions may be absent). 
Output: If there is a mistake in expression than the program will show the place of first mistake. 
If there is no mistakes - it will tell user if polynomials are the same or not after adduction ("Polynomials are the same" or "Polynomials are different").

Программа принимает на вход два многочлена, записанные в математической форме. Если после приведения, многочлены совпадают,
то сообщается - "Polynomials are the same", в обратном случае - "Polynomials are different".
# Parameters
Key -d for debugging
Key -e for configuring of epsilon (used for comparison of numbers e.g. 0.004 and 0.003 are the same if epsilon is 1e-2)
# Example of launch:
polynomials.py (x+z)(y+x)-z(x+y) x(y+x) -e 1e-4 -d
