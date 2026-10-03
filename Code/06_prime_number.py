def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print("Prime" if is_prime(number) else "Not Prime")
