def is_palindrome_string(text):
    text = text.lower()
    return text == text[::-1]


if __name__ == "__main__":
    text = input("Enter a string: ")
    print("Palindrome" if is_palindrome_string(text) else "Not Palindrome")
