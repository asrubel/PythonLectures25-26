# DRY - Don't Repeat Yourself
# PEP8

def my_fun(par1, par2):
    """My function: adding two numbers"""
    print(par1, par2)
    res = par1 + par2
    print(res)
    return res


def empty_fun():
    # TODO - Write function body
    pass


res1 = my_fun(1, 2)
res2 = my_fun(10, 20)
print(res1)
print(res2)
print(my_fun(50, 100))
