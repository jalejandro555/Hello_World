# Hello_World - First challenge
HellooooO WORLD, my name is Alejandro, and basically the last time I use Python or even needed to write on English was when I was in the school, so at this point the things that i know about python are equivalent to my knowledge on football, women or polythics (not an expert). BUUUT i've always liked to challenge myself, SO what a better way to do it than learning again how to code on python doing it this time fully on english, ANNND obviously in record time. 
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
```python
def maximum_consecutive_sum(number_list):
    """
    this function calculates the maximum sum betwen consecutive numbers in a list of integers.

    Args:
        number_list (list): A list of integers.

    Returns:
        float: The maximum sum between consecutive numbers.
    """
    if not number_list:
        return 0  # If the list is empty, the sum is 0

    max_sum = float("-inf")  # Initialize with a very small value (negative infinity)

    for i in range(len(number_list) - 1):
        current_sum = number_list[i] + number_list[i + 1]
        max_sum = max(max_sum, current_sum)

    return max_sum

try:
    user_input = input("Enter a list of numbers separated by commas: ")
    number_list = [int(num) for num in user_input.split(",")]  # Split user input into a list of strings using comma as a separator.
    result = maximum_consecutive_sum(number_list)
    print(f"The maximum sum between consecutive numbers is: {result}")
except ValueError:
    print("Error: Enter a valid list of numbers separated by commas.")

```
### How does it work?
the first thing that I did, was define a function called maximum_consecutive_sum. Its purpose is to find the maximum sum between consecutive numbers in a given list of integers. The maximum_consecutive_sum function takes a single argument, number_list, which is expected to be a list of integers, if the input list is empty the function immediately returns 0. It initializes max_sum with a very small value. This ensures that any valid sum encountered during iteration will be greater than this initial value. The function iterates through the list of numbers (excluding the last one) using a "for" loop, for each pair of consecutive numbers, it calculates their sum (current_sum), the maximum of the current sum and the previously calculated maximum sum (max_sum) is stored in max_sum. After processing all pairs of consecutive numbers, the function returns the maximum sum found. Finally the try and except block handles user input. If the user enters an invalid list, it displays an error message.
## Fifth point
Write a function that receives a list of strings and returns only those elements that have the same characters. input: ["love", "rome", "dog"], output ["love", "rome"]
```python
def is_anagram(cadena1, cadena2):
    # Convert both strings to lowercase
    cadena1 = cadena1.lower()
    cadena2 = cadena2.lower()

    # Convert the strings to lists
    lista1 = list(cadena1)
    lista2 = list(cadena2)

    # Sort thethe lists
    lista1.sort()
    lista2.sort()

    # Convert the lists back to strings
    cadena1_sorted = "".join(lista1)
    cadena2_sorted = "".join(lista2)

    # Check if the sorted strings are equal (i.e., anagrams)
    return cadena1_sorted == cadena2_sorted

def filter_anagrams(lista):
    # Create an empty dictionary called 'anagrams' to store anagram words
    anagrams = {}
    # Create an empty set to store non-anagram words
    non_anagrams = set()

    for word in lista:
        # Generate a unique 'code' for each word by sorting its characters alphabetically
        code = "".join(sorted(word))

        # Check if the code is already in the 'anagrams' dictionary
        if code in anagrams:
            anagrams[code].append(word)
            """"
             If the code already exists, we add the word to the corresponding list
             in the anagram dictionary. If it does not exist,
             We create a new entry in the dictionary with the word.
             """
        else:
            # If not, create a new entry with the word
            anagrams[code] = [word]

    # Iterate over the entries in the 'anagrams' dictionary
    for code, words in anagrams.items():
        # If there are more than one word with the same code, add them to the non-anagrams set
        if len(words) > 1:
            """
             If there is more than one word associated with the same code
             (that is, they are anagrams), we add them
             to the set no_anagrams.
             """
            non_anagrams.update(words)

    # Convert the non-anagrams set back to a list
    return list(non_anagrams)

# Ask the user for a list of words
user_input = input("Enter a list of words separated by commas: ")
word_list = user_input.split(",")

# Filter out the anagrams
result = filter_anagrams(word_list)
print("Words with the same letters are:", result)
```
### How does ir work?
The is_anagram function checks if two strings are anagrams. Converts strings to lowercase, converts them to lists, sorts them, and converts them back to strings. Finally, compare the sorted strings to see if they are equal.
The filter_anagrams function takes a list of words as input and returns a list of the words that are anagrams. Create a dictionary to store anagram words and a set to store non-anagram words. For each word, calculate a "code" by ordering its characters. If the code already exists in the dictionary, it adds the word to the corresponding list. If it doesn't exist, create a new dictionary entry with the word. Finally, it iterates over the dictionary and adds to the no_anagrams set the words that have more than one entry in the list.
