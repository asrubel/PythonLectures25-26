def capital(**kwargs):
    for key, value in kwargs.items():
        print(value, "is the capital city of", key)


capital(Canada="Ottawa", Estonia="Tallinn", Venezuela="Caracas", Finland="Helsinki")


def func(positional_args, defaults, *args, **kwargs):
    pass


def locate(place, planet="Earth"):
    print(place, "on", planet)


locate("Berlin")
locate("Breakfast", planet="Pluto")
locate("Craters", "Mercury")
