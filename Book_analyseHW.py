import requests

# URLs for the two books
book1_url = "https://www.gutenberg.org/cache/epub/15237/pg15237.txt"
book2_url = "https://www.gutenberg.org/cache/epub/32472/pg32472.txt"


# Function to get unique word count from a book URL
def get_unique_word_count(url):
    response = requests.get(url)
    text = response.text.lower()  # Convert to lowercase to treat words case-insensitively
    unique_words = {}
    punctuation = ",.'?!=()\";:[]{}-*"

    for line in text.splitlines():
        for p in punctuation:
            line = line.replace(p, " ")  # Remove punctuation
        words = line.split()
        for word in words:
            unique_words[word] = unique_words.get(word, 0) + 1

    return unique_words


# Get unique word counts for both books
book1_words = get_unique_word_count(book1_url)
book2_words = get_unique_word_count(book2_url)

# Count of unique words in each book
book1_unique_count = len(book1_words)
book2_unique_count = len(book2_words)

# Determine which book has more unique words
if book1_unique_count > book2_unique_count:
    winner = "Book 1 has more unique words."
elif book2_unique_count > book1_unique_count:
    winner = "Book 2 has more unique words."
else:
    winner = "Both books have the same number of unique words."

# Print results
print(f"Book 1 Unique Words: {book1_unique_count}")
print(f"Book 2 Unique Words: {book2_unique_count}")
print(winner)


