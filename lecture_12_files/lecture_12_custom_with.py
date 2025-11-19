class ContextClass:
    def __enter__(self):
        print("Entering context class")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context class")

    def my_method(self):
        print(f"My method in {self}")


with ContextClass() as context:
    context.my_method()

print("The end!")
