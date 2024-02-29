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
