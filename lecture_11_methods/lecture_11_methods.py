class Ship:
    num = 0

    def __new__(cls, *args, **kwargs):
        if cls.num >= 2:
            raise Exception
        else:
            cls.num += 1
        print("New ship")
        return object.__new__(cls)

    def __init__(self, name, capacity):
        print("Ship initialized")
        self.name = name
        self.capacity = capacity
        self.cargo = 0
        self.captain = None

    def sail(self):
        print(f"{self.name} is sailing...")

    def name_captain(self, captain):
        self.captain = captain
        print(f"New captain assigned to this ship: {self.captain}")

    def load_cargo(self, weight):
        status = f"Loading {weight} tons."
        if self.cargo + weight > self.capacity:
            print(f"{status} Oops! Cannot do that!")
        else:
            self.cargo += weight
            print(f"{status} Done!")

    def unload_cargo(self, weight):
        status = f"Unloading {weight} tons."
        if self.cargo - weight < 0:
            print(f"{status} Oops! Cannot do that!")
        else:
            self.cargo -= weight
            print(f"{status} Done!")

    def __str__(self):
        # return ("Ship: " + self.name +
        #         " with capacity: " + str(self.capacity) +
        #         ", cargo: " + str(self.cargo) +
        #         ", captain: " + self.captain)
        return f"""
                Ship: {self.name} 
                Captain: {self.captain} 
                Capacity: {self.capacity} 
                Cargo: {self.cargo} tons"""

    def show_declaration(self):
        print(self)

    def __add__(self, other):
        self.load_cargo(other)
        return self

    def __sub__(self, other):
        self.unload_cargo(other)
        return self


print(Ship.num)
ship1 = Ship("Black Pearl", 100)
ship1.name_captain("Jack Sparrow")
print(Ship.num)
ship1.sail()
Ship.sail(ship1)
print(ship1.name)
print(ship1.capacity)
print(ship1.cargo)
print(ship1.captain)

ship1.load_cargo(90)
ship1.show_declaration()
ship1.unload_cargo(100)
ship1.show_declaration()
ship1.load_cargo(20)
ship1.show_declaration()
ship1.unload_cargo(60)
ship1.show_declaration()

ship1 = ship1 + 10
ship1.show_declaration()
ship1 = ship1 - 5
ship1.show_declaration()
ship1 += 18
ship1.show_declaration()
ship1 -= 1
ship1.show_declaration()

ship2 = Ship("Victory", 200)
print(Ship.num)
ship2.sail()
print(ship2.name)
print(ship2.capacity)
print(ship2.cargo)
print(ship2.captain)

# ship3 = Ship("Flying Dutch", 150)
# print(Ship.num)
