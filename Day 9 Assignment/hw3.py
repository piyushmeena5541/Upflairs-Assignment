class VowelCounter:
    def count_vowels(self, input_string):
        vowels = "aeiouAEIOU"
        count = 0
        for char in input_string:
            if char in vowels:
                count += 1
        return count

counter = VowelCounter()
input_string = input("Enter a string: ")
vowel_count = counter.count_vowels(input_string)
print("Number of vowels in the string:", vowel_count)
