from fastapi import FastAPI

app=FastAPI()

BOOKS=[
    {'title':'Title one','Author':'Author One','category':'math'},
    {'title':'Title two','Author':'Author Two','category':'math'},
    {'title':'Title three','Author':'Author Three','category':'english'},
    {'title':'Title four','Author':'Author Four','category':'computer'},
    {'title':'Title five','Author':'Author Five','category':'computer'}
]

@app.get("/books")
def read_all_books():
    return BOOKS
#dynamic path parameter
#fastapi ecexutes the functions in cronological order i.e from top to buttom
#you can use path parameter to dynamically pass values through request
@app.get("/books/{book_title}")
def read_book(book_title:str):
    for book in BOOKS:
        if book.get('title').casefold()==book_title.casefold():
            return book

#query parameter
#query parameter is when you pass values using key value pair
#passed in url after question mark

@app.get("/books/")       
def read_category_by_query(category:str):
    book_category=[]
    for book in BOOKS:
        if book.get('category')==category:
            book_category.append(book)
    return book_category

