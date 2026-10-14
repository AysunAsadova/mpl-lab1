# Task 2 - Functional style: no for/while loops, no list comprehensions

from functools import reduce

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

# Same list of titles as Task 1, using filter() and map() with lambda
selected = filter(lambda b: b["year"] > 2000 and b["pages"] > 200, books)
titles = list(map(lambda b: b["title"], selected))
print("Books after 2000 with more than 200 pages:")
print(titles)

# All books ordered by year, using sorted() with key=lambda
by_year = sorted(books, key=lambda b: b["year"])
print()
print("Books ordered by year:")
print("\n".join(map(lambda b: f"{b['year']} - {b['title']}", by_year)))

# Total number of pages with reduce()
total_pages = reduce(lambda acc, b: acc + b["pages"], books, 0)
print()
print("Total pages:", total_pages)
