books = []
books_read = []

no_of_books = int(input())

book_title = ""
for x in range(no_of_books):
    operation_book = input().split(" ")
    # print(operation_book)
    if operation_book[0] == "BUY":
        for word in operation_book[1:]:
            book_title = book_title + " " + word

        book_title = book_title.lstrip(" ")

        # print(book_title)
        books.append(book_title)
        book_title = ""
    elif operation_book[0] == "READ":
        books_read.append(books.pop())

for book in books_read:
    print(book)
