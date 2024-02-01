"""
sum = sum(range(0, 101, 10))
print("0-100自然数中能被10整除的所有数的和为：" + str(sum))

print("0-100自然数中能被10整除的所有数分别为：")
for i in range(0, 101, 10):
    print(str(i))

a = 10 + 20 + 30 + 40 + 50 + 60 + 70 + 80 + 90 + 100
print("0-100自然数中能被10整除的所有数的和为：" + str(a))
"""

"""
from sympy import symbols, Eq, solve

x, y = symbols('x y')
eq1 = Eq(x + y, 88)
eq2 = Eq(x - y, 2)
solution = solve((eq1, eq2), (x, y,))
print(solution)
"""

"""
from sympy import symbols, Eq, solve
# 定义变量
x = symbols('x')
# 创建方程
equation = Eq(x**2 + 3*x + 2, 0)
# 使用sympy求解方程
solutions = solve(equation, x)
print(solutions)
"""
a1 = 1
b1 = 2
c1 = 1
a2 = 2
b2 = 4
c2 = 2

import cmath

d = a1*b2 - a2*b1
dx = c1*b2 - c2*b1
dy = a1*c2 - a2*c1

if d != 0:
    x = dx/d
    y = dy/d
    print("x is :", x)
    print("y is :", y)
else:
    if dx == 0 and dy == 0:
        print("There are infinitely many solutions")
    else:
        print("There is no solution")
