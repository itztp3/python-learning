from collections import Counter

print("=== TEXT INTELLIGENCE ANALYZER ===")

text = input("Enter a paragraph: ")

words = text.lower().split()
clean_words = [
    word.strip(".,!?;:\"'()")
    for word in words
]
clean_words = [word for word in clean_words if word]

characters = len(text)
vowels = sum(
    1 for char in text.lower()
    if char in "aeiou"
)

print("\n=== ANALYSIS REPORT ===")
print("Total words:", len(words))
print("Total characters:", characters)
print("Total vowels:", vowels)

if clean_words:
    longest_word = max(clean_words, key=len)
    frequency = Counter(clean_words)
    common_word, count = frequency.most_common(1)[0]

    print("Longest word:", longest_word)
    print("Most frequent word:", common_word)
    print("Frequency:", count)
else:
    print("No words to analyze.")

print("\nAnalysis completed!")
