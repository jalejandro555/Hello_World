def is_prime(number):
    """Verifies if a given number is prime."""
    if number < 2:
        return False  # If the number is less than 2, it's not prime
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0: #Here a for loop is started that loops through the numbers from 2 to the integer square root of the number plus 1.
            return False  # If it's divisible by any number between 2 and its square root, it's not prime
    return True  # If no divisors were found, it's prime

def get_primes_from_list():
    try:
        user_input = input("Enter a list of numbers separated by commas: ")
        numbers = [int(num.strip()) for num in user_input.split(",")]
        primes = [num for num in numbers if is_prime(num)]
        if primes:
            print(f"The prime numbers in the list are: {primes}")
        else:
            print("No prime numbers found in the list.")
    except ValueError:
        print("Please enter integer numbers separated by commas correctly.")

get_primes_from_list()  # Execute the function
