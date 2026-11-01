# Library Borrowing Record Analysis

# Sample data: Member ID and books borrowed by each member

library_data = {
    "M001": ["Book A", "Book B"],
    "M002": ["Book C"],
    "M003": [],
    "M004": ["Book A", "Book A"],
    "M005": [],
    "M006": ["Book B", "Book D"]
}

# 1. Calculate the average number of books borrowed

total_members = len(library_data)

total_books_borrowed = sum(
    len(books) for books in library_data.values()
)

if total_members > 0:
    average = total_books_borrowed / total_members
else:
    average = 0

print("Average books borrowed:", average)


# 2. Find the most and least borrowed books

all_books = []

for books in library_data.values():
    all_books.extend(books)

book_counts = {}

for book in all_books:
    if book in book_counts:
        book_counts[book] += 1
    else:
        book_counts[book] = 1

if book_counts:
    highest_count = max(book_counts.values())
    lowest_count = min(book_counts.values())

    most_borrowed = [
        book for book, count in book_counts.items()
        if count == highest_count
    ]

    least_borrowed = [
        book for book, count in book_counts.items()
        if count == lowest_count
    ]

    print("Most borrowed books:", most_borrowed)
    print("Least borrowed books:", least_borrowed)
else:
    print("No books have been borrowed.")


# 3. Count members who borrowed zero books

zero_borrowers = sum(
    1 for books in library_data.values()
    if len(books) == 0
)

print("Members with 0 borrowings:", zero_borrowers)


# 4. Find the most frequently borrowed book (mode)

if book_counts:
    print("Most frequently borrowed book (mode):", most_borrowed)
else:
    print("Mode: No books have been borrowed.")