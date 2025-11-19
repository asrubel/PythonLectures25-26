class River:
    all_rivers = []

    def __init__(self, name, length):
        self.name = name
        self.length = length
        print(f"{self.name} was created!")
        River.all_rivers.append(self)

    def show_info(self):
        print(f"{self.name} has a length of {self.length}")


dnipro = River("Dnipro", 3000)
print(dnipro.name)
print(dnipro.length)
print(River.all_rivers)

dnistro = River("Dnistro", 2000)
print(River.all_rivers)
danube = River("Danube", 4000)
print(River.all_rivers)

for river in River.all_rivers:
    river.show_info()
    River.show_info(river)
