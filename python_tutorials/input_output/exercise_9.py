def count_word_frequency(input_file, output_file):
    with open(input_file, "r") as f:
        words = f.read().split()

    freq_dict = {}
    for word in words:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1

    with open(output_file, "w") as f:
        for word, freq in sorted(freq_dict.items()):
            f.write(f"{word}: {freq}\n")
