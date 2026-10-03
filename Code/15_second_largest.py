def second_largest(numbers):
    unique_numbers = list(set(numbers))

    if len(unique_numbers) < 2:
        return None

    unique_numbers.sort()
    return unique_numbers[-2]


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))
    result = second_largest(numbers)

    if result is None:
        print("Second largest does not exist")
    else:
        print("Second largest:", result)
