class NegativeResultError(Exception):
    def __init__(self, value):
        self.message = f"The result is negative: {value}"
        super().__init__(self.message)

    def __str__(self):
        return self.message


def num_div(x, y):
    if y == 0:
        raise ZeroDivisionError("The second number is sero!")
    elif y < 0:
        raise NegativeResultError(y)
    else:
        return x / y


def exception_example(x, y):
    try:
        if y < 0:
            raise NegativeResultError(y)
        else:
            return x / y
    except NegativeResultError as error:
        print(error)


# print(num_div(5, 0))
# print(num_div(5, -2))

print(exception_example(3, 5))
print(exception_example(3, -5))
