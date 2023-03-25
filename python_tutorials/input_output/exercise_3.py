sentence = input("Enter a sentence: ")
with open("words.txt", "w") as f:
    words = sentence.split()
    for word in words:
        f.write(word + "\n")
