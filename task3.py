# Task 3 - Higher-order function with a callback


def count_if(items, predicate):
    """Return how many items satisfy predicate(item)."""
    count = 0
    for item in items:
        if predicate(item):
            count += 1
    return count


books = [
    {"title": "Dune", "year": 1965, "pages": 612},
    {"title": "The Hobbit", "year": 1937, "pages": 310},
    {"title": "Harry Potter and the Goblet of Fire", "year": 2000, "pages": 636},
    {"title": "The Kite Runner", "year": 2003, "pages": 371},
    {"title": "The Alchemist", "year": 1988, "pages": 163},
    {"title": "Life of Pi", "year": 2001, "pages": 319},
    {"title": "The Little Prince", "year": 1943, "pages": 96},
    {"title": "Gone Girl", "year": 2012, "pages": 145},
]


# Named function callback
def is_classic(book):
    return book["year"] < 1950


# Call with a lambda: books with fewer than 150 pages
short_books = count_if(books, lambda b: b["pages"] < 150)
print("Books with fewer than 150 pages:", short_books)

# Call with the named function: books published before 1950
classics = count_if(books, is_classic)
print("Classic books (before 1950):", classics)

# The same function, unchanged, on a plain list of numbers
numbers = [3, 7, 9, 12, 14, 18, 20, 21, 25]
divisible_by_3 = count_if(numbers, lambda n: n % 3 == 0)
print("Numbers divisible by 3:", divisible_by_3)
