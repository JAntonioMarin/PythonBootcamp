my_list = [1,2,3]
print(len(my_list))

class Sample():
    pass

my_sample = Sample()
print(my_sample)


class Book():
    def __init__(self, title, author, pages):

        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book object has been deleted")

b = Book('Python rocks', 'Jose', 200)
print(b)
print(str(b))
print(len(b))
del b # And when finish the program