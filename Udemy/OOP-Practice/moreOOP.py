class Book():

    def __init__(self, title, author, pages):

        self.title = title
        self.author = author
        self.pages = pages

    # Whenever a string is wanted to be returned this method is used
    def __str__(self):
        return f'{self.title} by {self.author}'

    # Whenever a len of a method is wanted, in this case pages is most likely wanted
    def __len__(self):
        return self.pages

    # Whenever del  is run on the method, it will delete and print this out
    def __del__(self):
        print("Book object deleted")





b = Book('Python rocks', 'Jose', 200)
print(b)