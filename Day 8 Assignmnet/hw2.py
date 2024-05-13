def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                words = line.split()
                num_words = len(words)
                print(f"Line {line_number}: {num_words} words")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")

# Replace 'example.txt' with the path to your text file
filename = 'example.txt'
count_words_in_file(filename)
