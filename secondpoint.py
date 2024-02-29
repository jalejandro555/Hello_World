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
