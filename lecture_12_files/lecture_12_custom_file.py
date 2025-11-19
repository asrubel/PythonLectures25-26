class CustomFile:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.file = open(self.file_name, mode)

    def __enter__(self):
        print("Enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exit")
        self.file.close()

    def print_content(self):
        print(self.file.readlines())


with CustomFile("courses.txt", "r") as f:
    f.print_content()

print("Done")
