def find_smallest_factor(n):
    if n < 2:
        print("Invalid input. Enter a number greater than or equal to 2.")
        return

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print(f"The smallest factor other than 1 for {n} is {i}.")
            return

    print(f"{n} is a prime number, and its only factor is 1.")


def main():
    while True:
        try:
            num = int(input("Enter an integer (greater than or equal to 2):"))

            if num < 2:
                print("Invalid input. Enter a numnber greater than 2.")
                break

            find_smallest_factor(num)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()