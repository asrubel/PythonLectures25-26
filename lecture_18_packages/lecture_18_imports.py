import lecture_18_modules as l18
from lecture_18_modules import MyClass as SomeClass, my_fun as some_fun
from lecture_18_modules import x as y

import package1.module1 as m1
import package1.module2 as m2

from package2.module1 import Class1
from package2.module2 import Class2

import numpy as np

print(__name__)

print(l18.x)
print(id(l18.x))
print(l18.my_fun(10, 15))
print(type(l18.MyClass))

print(m1.my_fun(10))
print(m2.my_fun(10))

print(y)
print(id(y))
print(some_fun(10, 15))
print(type(SomeClass))

print(Class1())
print(Class2())

my_array = np.array([1, 2, 3])
print(my_array)
print(type(my_array))
