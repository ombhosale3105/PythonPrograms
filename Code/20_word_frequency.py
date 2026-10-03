def word_frequency(sentence):
    words = sentence.lower().split()
    frequency = {}

    for word in words:
        word = word.strip(".,!?;:")
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    print(word_frequency(sentence))
