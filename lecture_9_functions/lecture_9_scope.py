# LEGB rule
# Local
# Enclosing
# Global
# Built-in

my_var = "C++"

def my_fun():
    global my_var
    my_var = "Python"
    print(my_var)


my_fun()
print(my_var)

var = "global"


def outer():
    var = "enclosing"

    def inner():
        nonlocal var
        var = "local"
        print(var)

    inner()
    print(var)


outer()
print(var)
