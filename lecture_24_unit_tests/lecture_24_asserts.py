user_input = input("Enter a word: ")
assert user_input == "python"
print("You entered", user_input)

user_input = input("Enter a word: ")
message = "Wrong word!"
assert user_input == "python", message
print("You entered", user_input)

try:
    user_input = input("Enter a word: ")
    message = "Wrong word!"
    assert user_input == "python", message
    print("You entered", user_input)
except AssertionError as error:
    print(error)


def test_number(n):
    msg = "A small number"
    assert n > 100, msg
    return n


print(test_number(99))
print(test_number(101))
