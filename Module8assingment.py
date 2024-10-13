Python 3.12.5 (v3.12.5:ff3bc82f7c9, Aug  7 2024, 05:32:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def greaterThan(x,y)
SyntaxError: expected ':'
>>> def greaterThan(x,y)
SyntaxError: expected ':'
>>> 
>>> 
>>> def greaterThan(x,y):
...     return x > y
... 
>>> a = 2
>>> b = 3
>>> result = greaterThan(a, b)
>>> 
>>> print(a)
2
>>> print(b)
3
>>> 
>>> print("The statement " + str(a) + " is greater than " + str(b) + " is " + str(result))
The statement 2 is greater than 3 is False
>>> The statement 2 is greater than 3 is False
SyntaxError: invalid syntax
>>> 
>>> def greaterThan(x,y):
...     return x > y
... 
... a = 10
... b = 6
... result = greaterThan(a, b)
SyntaxError: invalid syntax
>>> print("The statement " + str(a) + " is greater than " + str(b) + " is " + str(result))
The statement 2 is greater than 3 is False
>>> def greaterThan(x,y):
...     return x > y
... 
... a = 10
... b = 6
... result = greaterThan(a, b)
SyntaxError: invalid syntax
>>> 
>>> a = 10
>>> b = 6
>>> result = greaterThan(a, b)
>>> print("The statement " + str(a) + " is greater than " + str(b) + " is " + str(result))
The statement 10 is greater than 6 is True
