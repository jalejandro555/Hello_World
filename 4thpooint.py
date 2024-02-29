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

    max_sum = float()  

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

