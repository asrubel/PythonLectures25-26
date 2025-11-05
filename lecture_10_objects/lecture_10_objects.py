class MyClass(object):
    ...


my_obj = MyClass()
print(my_obj)

base_obj = object()
print(base_obj)
print(dir(base_obj))


class Student:
    university = 'KhAI'

    def my_method(self):
        print("My method from " + str(self))


student1 = Student()
student2 = Student()
print(student1)
print(student2)

print(student1.university)
print(student2.university)

student1.my_method()
student2.my_method()

Student.my_method(student1)
Student.my_method(student2)


class Book:
    material = "paper"
    cover = "hard"
    all_books = []

    def __str__(self):
        return ("<Book --> " + self.material + " --> " + self.cover +
                "; id: " + str(id(self)) + ">")


print(Book.material)
print(Book.cover)
print(Book.all_books)

my_book = Book()
print(my_book.material)
print(my_book.cover)
print(my_book.all_books)

my_book.all_books.append("Clean architecture")
print(my_book.all_books)
print(Book.all_books)

my_book.cover = "soft"
print(my_book.cover)
print(Book.cover)

other_book = Book()
print(other_book.cover)
another_book = Book()
print(another_book.cover)

Book.cover = "mixed"
print(Book.cover)
print(my_book.cover)
print(other_book.cover)
print(another_book.cover)

other_book.all_books.append("Python for Beginners")
print(my_book.all_books)
print(other_book.all_books)
print(Book.all_books)

print(my_book)
print(other_book)
print(another_book)
print(Book)
