# Task 1 - Imperative style: loops and conditions only
# (no map(), filter(), reduce() or lambda, and no max())

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

# Part 1: titles of books published after 2000 with more than 200 pages
selected_titles = []
for book in books:
    if book["year"] > 2000 and book["pages"] > 200:
        selected_titles.append(book["title"])

print("Books after 2000 with more than 200 pages:")
for title in selected_titles:
    print(" -", title)

# Part 2: book with the largest number of pages (without max())
biggest = books[0]
for book in books:
    if book["pages"] > biggest["pages"]:
        biggest = book

print()
print("Book with the most pages:", biggest["title"], "-", biggest["pages"], "pages")
