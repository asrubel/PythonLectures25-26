class MyClass:
    ...


class AnotherClass(object):
    ...


print(dir(AnotherClass))


class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    ...


cat = Animal("Fluffy")
dog = Dog("Rex")

print(type(cat))
print(type(dog))

print(isinstance(cat, Animal))
print(isinstance(cat, Dog))
print(isinstance(dog, Animal))
print(isinstance(dog, Dog))
print(isinstance(dog, object))

print(issubclass(Dog, Animal))
print(issubclass(Animal, Dog))
