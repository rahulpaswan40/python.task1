#1. Integer
i3 = 5000
print('i3 value is =', i3, 'and i3 type is', type(i3))

i4 = -123456
print('i4 value is =', i4, 'and i4 type is', type(i4))

#2. String
s3 = "Python Programming"
print('s3 value is =', s3, 'and s3 type is', type(s3))

s4 = 'Data Science'
print('s4 value is =', s4, 'and s4 type is', type(s4))

#3. Float
f3 = 9.806
print('f3 value is =', f3, 'and f3 type is', type(f3))

f4 = -273.15
print('f4 value is =', f4, 'and f4 type is', type(f4))

#4. Boolean
b3 = (10 > 100)
print('b3 value is =', b3, 'and b3 type is', type(b3))

b4 = bool(1)
print('b4 value is =', b4, 'and b4 type is', type(b4))

#5. List
l3 = [10.5, 20.5, 30.5]
print('l3 value is =', l3, 'and l3 type is', type(l3))

l4 = [True, "String", 42]
print('l4 value is =', l4, 'and l4 type is', type(l4))

#6. Dictionary
d3 = {'name': 'Alice', 'role': 'Engineer'}
print('d3 value is =', d3, 'and d3 type is', type(d3))

d4 = {101: 'Room A', 102: 'Room B'}
print('d4 value is =', d4, 'and d4 type is', type(d4))

#7. Tuple
t3 = (100, 200, 300)
print('t3 value is =', t3, 'and t3 type is', type(t3))

t4 = ('apple', 'banana', 'cherry')
print('t4 value is =', t4, 'and t4 type is', type(t4))

#8. Set
set3 = {1, 1, 2, 2, 3} # Duplicates will be removed
print('set3 value is =', set3, 'and set3 type is', type(set3))

set4 = {'red', 'green', 'blue'}
print('set4 value is =', set4, 'and set4 type is', type(set4))

#9. Complex
c3 = 0 + 1j
print('c3 value is =', c3, 'and c3 type is', type(c3))

c4 = complex(10, -5)
print('c4 value is =', c4, 'and c4 type is', type(c4))

#10. Range
r3 = range(10, 20)
print('r3 value is =', list(r3), 'and r3 type is', type(r3))

r4 = range(0, -10, -2)
print('r4 value is =', list(r4), 'and r4 type is', type(r4))

#11. Bytes
b3_val = bytes([100, 101, 102])
print('b3_val value is =', b3_val, 'and b3_val type is', type(b3_val))

b4_val = b"Encoded"
print('b4_val value is =', b4_val, 'and b4_val type is', type(b4_val))

#12. Bytearray
ba3 = bytearray(b"Editable")
print('ba3 value is =', ba3, 'and ba3 type is', type(ba3))

ba4 = bytearray([255, 0, 128])
print('ba4 value is =', ba4, 'and ba4 type is', type(ba4))

#13. Frozenset
fs3 = frozenset([10, 20, 30])
print('fs3 value is =', fs3, 'and fs3 type is', type(fs3))

fs4 = frozenset("python")
print('fs4 value is =', fs4, 'and fs4 type is', type(fs4))

#14. NoneType
n3 = None
print('n3 value is =', n3, 'and n3 type is', type(n3))

def empty_func(): pass
n4 = empty_func()
print('n4 value is =', n4, 'and n4 type is', type(n4))

#15. Function
def greet_func():
    return "Hi"
print('greet_func value is =', greet_func, 'and greet_func type is', type(greet_func))

sq_lambda = lambda x: x ** 2
print('sq_lambda value is =', sq_lambda, 'and sq_lambda type is', type(sq_lambda))

#16. Method
class Calculator:
    def power(self, base, exp):
        return base ** exp
calc = Calculator()
print('power value is =', calc.power, 'and power type is', type(calc.power))

class Utils:
    def get_info(self):
        return "Utility class"
util_obj = Utils()
print('get_info value is =', util_obj.get_info, 'and get_info type is', type(util_obj.get_info))

#17. Module
import os
print('os module value is =', os, 'and os module type is', type(os))

import json
print('json module value is =', json, 'and json module type is', type(json))

#18. Class
class Car:
    pass
print('Car value is =', Car, 'and Car type is', type(Car))

class Bike:
    def __init__(self, brand):
        self.brand = brand
print('Bike value is =', Bike, 'and Bike type is', type(Bike))

#19. Type
type3 = type(3.14)
print('type3 value is =', type3, 'and type3 type is', type(type3))

type4 = type([1])
print('type4 value is =', type4, 'and type4 type is', type(type4))

#20. Memoryview
mv3 = memoryview(b'ABCDEF')
print('mv3 value is =', mv3, 'and mv3 type is', type(mv3))

mv4 = memoryview(bytearray(5))
print('mv4 value is =', mv4, 'and mv4 type is', type(mv4))

#21. Generator
def count_gen():
    yield "First"
    yield "Second"
g3 = count_gen()
print('g3 value is =', g3, 'and g3 type is', type(g3))

g4 = (n for n in range(3))
print('g4 value is =', g4, 'and g4 type is', type(g4))

#22. Ellipsis
e3 = Ellipsis
print('e3 value is =', e3, 'and e3 type is', type(e3))

# Using Ellipsis in slicing (common in NumPy)
e4 = ...
print('e4 value is =', e4, 'and e4 type is', type(e4))

#23. NotImplementedType
ni3 = NotImplemented
print('ni3 value is =', ni3, 'and ni3 type is', type(ni3))

ni4 = NotImplemented
print('ni4 value is =', ni4, 'and ni4 type is', type(ni4))