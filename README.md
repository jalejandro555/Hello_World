# Hello_World - First challenge
HellooooO WORLD, my name is Alejandro, and basically the last time I use Python or even needed to write on english was when i was in the school, so at this point the things that i know about python are equivalent to astrophysics, women or polythics. BUUUT i've always liked to challenge myself, SO what a better way to do it than learning again how to code on python doing it this time fully on english, ANNND obviously in record time. 
Could there be mistakes? yes 
Could there be tears? idk
Will I return to Spanish in the future? for sure
## First point: 
Create a function that performs basic operations (addition, subtraction, multiplication, division) between two numbers, according to the user's choice, the input form of the function will be the two operands and the character used for the operation. input: (1,2,"+"), output (3).

```python
def calculate_operation(number1: float, number2: float, operator: str):
    """
    this function performs the specified operation between two operands.

    the arguments of the function are 
        number1 (float): First operand.
        number2 (float): Second operand.
        operator (str): Character representing the operation (+, -, *, or /).

    Returns:
        float: Result of the operation.
    """
    if operator == "+":
        result = number1 + number2  # Adds operands if the operator is "+"
    elif operator == "-":
        result = number1 - number2  # Subtracts operands if the operator is "-"
    elif operator == "*":
        result = number1 * number2  # Multiplies operands if the operator is "*"
    elif operator == "/":
        if number2 != 0:
            result = number1 / number2  # Divides operands if the operator is "/"
        else:
            print("Error: Cannot divide by zero.")
            return None  # Returns None if division by zero is attempted
    else:
        print("Error: Invalid operator. Use +, -, *, or /.")
        return None  # Returns None if the operator is invalid

    return result  # Returns the result of the operation

number1 = float(input("Enter the first operand: "))  # Asks the user for the first operand
number2 = float(input("Enter the second operand: "))  # Asks the user for the second operand
operator = str(input("Enter the operator (+, -, *, /): "))  # Asks the user for the operator

result = calculate_operation(number1, number2, operator)  # Calls the function
if result is not None:
    print(f"Result: {result}")  # Prints the result if it is not None
```
### How does it work?
The calculate_operation function performs a specific operation between two numbers. The function arguments are these:
number1 (float): First operand.
number2 (float): Second operand.
operator (str): Character that represents the operation (+, -, *, or /).
The function checks the value of the operator and performs the corresponding operation. If the operator is “+”, add the operands; if it is “-”, subtracts them; if it is “*”, it multiplies them; and if it is “/”, it divides them. If the second operand is zero in a division, an error message is displayed and None is returned. If the operator is invalid, an error message is also displayed and None is returned. Finally, the function returns the result of the operation. At the end of the code it prompts the user to enter the operands and operator, then calls the calculate_operation function and displays the result if it is not None.
## Second point 
Make a function that allows you to validate if a word is a palindrome. Condition: Slicing cannot be done to invert the word and verify that it is the same as the original.
```python
def is_palindrome_cycles(word):
    """
    Defines a function called is_palindrome_cycles that takes an argument called word.
    The function checks whether the word is a palindrome.
    """
    start = 0  # Initializes a variable called start with the value 0.
    end = len(word) - 1  # Calculates the length of the word and subtracts 1 to obtain the index of the last character.
    # This value is assigned to the variable end.
    while start < end:  # Starts a while loop that runs as long as the start index is less than the end index.
        if word[start] != word[end]:  # Compares the characters at positions start and end in the word.
            return False  # If they are different, the function returns False.
        start += 1  # Increments the start index by 1 to move rightward.
        end -= 1  # Decrements the end index by 1 to move leftward.
    
    return True  # If the while loop completes without finding different characters, the function returns True.

input_word = input("Enter a word: ")
result = is_palindrome_cycles(input_word)
if result:
    print(f"The word '{input_word}' is a palindrome.")
else:
    print(f"The word '{input_word}' is not a palindrome.")
```
### How does it work?
I defined a function called is_palindrome_cycles that checks whether a given word is a palindrome. It initializes two variables, start and end, representing the indices of the first and last characters in the word. The code then enters a while loop, comparing characters at these indices. If any characters differ, the function returns False, indicating that the word is not a palindrome. Otherwise, it continues checking until the indices meet in the middle. If the loop completes without finding different characters, the function returns True, confirming that the word is a palindrome. Finally, the user inputs a word, and the code displays whether it is a palindrome or not.
### Third point 
Write a function that receives a list of numbers and returns only those that are prime. The function must receive a list of integers and return only those that are prime.
```python
def is_prime(number):
    """Verifies if a given number is prime."""
    if number < 2:
        return False  # If the number is less than 2, it's not prime
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0: #Here a for loop is started that loops through the numbers from 2 to the integer square root of the number plus 1.
            return False  # If it's divisible by any number between 2 and its square root, it's not prime
    return True  # If no divisors were found, it's prime

def get_primes_from_list(): #This function takes no arguments and is responsible for obtaining a list of numbers from the user.
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
```
### How does it work?
The is_prime(number) function checks whether a given number is prime. It starts by verifying if the number is less than 2; if so, it returns False. Next, it iterates from 2 up to the integer square root of the number plus 1, checking if the number is divisible by any value in that range. If a divisor is found, it also returns False. If no divisors are found, the function returns True, indicating that the number is prime.

The get_primes_from_list() function prompts the user to input a list of numbers separated by commas. It then converts the input into a list of integers and filters out the prime numbers using the es_primo function. If there are prime numbers in the list, it prints a message with the prime numbers found; otherwise, it indicates that no prime numbers were found. Additionally, it handles errors if the user enters invalid data.

Finally, get_primes_from_list() function is called to execute the entire process. 
## Fourth point 
Write a function that receives a list of integers and returns the largest sum between two consecutive elements.
