sentence = input("Enter a sentence: ")
words = sentence.split()
word_lengths = {word: len(word) for word in words}
for word, length in sorted(word_lengths.items(), key=lambda x: x[1]):
    print(f"{word}: {length}")
