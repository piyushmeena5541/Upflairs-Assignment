def find_longest_word(words):
    if not words:
        return None
    
    longest_word = words[0]

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    
    return longest_word

# Example usage:
word_list = ["apple", "banana", "kiwi", "orange", "strawberry"]
longest_word = find_longest_word(word_list)
print("Longest word:", longest_word)
