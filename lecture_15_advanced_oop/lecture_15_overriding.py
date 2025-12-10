class ParentClass:
    def __init__(self, name):
        self.name = name
        print("Parent __init__ called")

    def do_something(self):
        print("Parent do_something called")


class ChildClass(ParentClass):
    def __init__(self, name):
        super().__init__(name)
        print("Child __init__ called")

    def do_something(self):
        print("Child do_something called")


parent = ParentClass("John")
child = ChildClass("Mary")

parent.do_something()
child.do_something()


class Car:
    def __init__(self, number):
        self.number = number

    def move(self):
        print(f"Car [{self.number}] is moving...")

    def carry(self, cargo):
        print(f"Car [{self.number}] is carrying {cargo}")


class Tractor(Car):
    def carry(self, cargo):
        print(f"Tractor is carrying cargo: {cargo}")


class Ambulance(Car):
    def carry(self, cargo):
        super().carry(cargo)
        print(f"Siren is wheeling!!!")


class Auto(Car):
    def __init__(self, number, body):
        super().__init__(number)
        self.body = body

    def move(self):
        print(f"Auto [{self.body}] is moving...")


tractor = Tractor("XA3456")
ambulance = Ambulance("XA1256")

tractor.move()
tractor.carry("10 tons of rubbish")

ambulance.move()
ambulance.carry("1 patient")

auto = Auto("XA7890", "sedan")
auto.move()
auto.carry("1 passenger")
