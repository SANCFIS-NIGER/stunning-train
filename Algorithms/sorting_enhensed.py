# !/usr/bin/env python3

"""
    File: <sorting_enhensed>.py
    -------------------

"""

# Importing the random library for being able to generate random floats
import random
# Importing the sys library to be able to interact with the operating system from the python code
import sys
import seaborn as sns
import time
from matplotlib import pyplot as plt

# Constants for terminal outputs colors
COLOR_RED = '\033[91m'
COLOR_GREEN = '\033[32m'
COLOR_RESET = '\033[0m'


class SortingPerformance:

    def __init__(self, list_to_process, sorting_function_list):
        self.sorting_function_list = sorting_function_list
        self.list_to_process = list_to_process

    def process_speed(self):
        dictionary_of_speed = {}

        for i_ndex in range(len(self.sorting_function_list)):
            start_time = time.time()
            self.sorting_function_list[i_ndex](self.list_to_process)
            end_time = time.time()
            dictionary_of_speed[self.sorting_function_list[i_ndex]] = end_time - start_time
        print(dictionary_of_speed)
        return dictionary_of_speed


def bubble_sort(unsorted_list):
    # Swap the elements to arrange in order

    for iter_num in range(len(unsorted_list) - 1, 0, -1):  # Starting the loop from the end
        # Returning a range of integers starting at len(unsorted_list) - 1 ,
        # continuing until it hits 0 , and increasing by -1 (decreasing by 1) each iteration
        for i_ndex in range(iter_num):
            if unsorted_list[i_ndex] > unsorted_list[i_ndex + 1]:
                temp = unsorted_list[i_ndex]
                unsorted_list[i_ndex] = unsorted_list[i_ndex + 1]
                unsorted_list[i_ndex + 1] = temp

    return unsorted_list


def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    # Find the middle point and divide it
    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return list(merge(left_list, right_list))


# Merge the sorted halves
def merge(left_half, right_half):
    halves_list = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            halves_list.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            halves_list.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        halves_list = halves_list + right_half
    else:
        halves_list = halves_list + left_half
    return halves_list


def insertion_sort(unsorted_list):
    for i_ndex in range(1, len(unsorted_list)):
        j = i_ndex - 1
        nxt_element = unsorted_list[i_ndex]
        # Compare the current element with next one
        while (unsorted_list[j] > nxt_element) and (j >= 0):
            unsorted_list[j + 1] = unsorted_list[j]
            j = j - 1
        unsorted_list[j + 1] = nxt_element
    return unsorted_list


def shell_sort(unsorted_list):
    gap = len(unsorted_list) // 2
    while gap > 0:
        for i_ndex in range(gap, len(unsorted_list)):
            temp = unsorted_list[i_ndex]
            j = i_ndex
            # Sort the sub list for this gap
            while j >= gap and unsorted_list[j - gap] > temp:
                unsorted_list[j] = unsorted_list[j - gap]
                j = j - gap
                unsorted_list[j] = temp
                # Reduce the gap for the next element
        gap = gap // 2

    return unsorted_list


def selection_sort(unsorted_list):
    for i_ndex in range(len(unsorted_list)):
        min_idx = i_ndex
        for j in range(i_ndex + 1, len(unsorted_list)):
            if unsorted_list[min_idx] > unsorted_list[j]:
                min_idx = j
        # Swap the minimum value with the compared value i_ndex times
        unsorted_list[i_ndex], unsorted_list[min_idx] = unsorted_list[min_idx], unsorted_list[i_ndex]
    return unsorted_list


def heapify(unsorted_list, one_by_one, i_largest):
    largest = i_largest  # Initialize largest as root
    left = 2 * i_largest + 1  # left = 2*i_largest + 1
    right = 2 * i_largest + 2  # right = 2*i_largest + 2

    # See if left child of root exists and is
    # greater than root
    if left < one_by_one and unsorted_list[largest] < unsorted_list[left]:
        largest = left

    # See if right child of root exists and is
    # greater than root
    if right < one_by_one and unsorted_list[largest] < unsorted_list[right]:
        largest = right

    # Change root, if needed
    if largest != i_largest:
        unsorted_list[i_largest], unsorted_list[largest] = unsorted_list[largest], unsorted_list[i_largest]  # swap

        # Heapify the root.
        heapify(unsorted_list, one_by_one, largest)


# The main function to sort an array of given size
def heap_sort(unsorted_list):
    list_size = len(unsorted_list)

    # Build a maxheap.
    for i_ndex in range(list_size // 2 - 1, -1, -1):
        heapify(unsorted_list, list_size, i_ndex)

    # One by one extract elements
    for one_by_one in range(list_size - 1, 0, -1):
        unsorted_list[one_by_one], unsorted_list[0] = unsorted_list[0], unsorted_list[one_by_one]  # swap
        heapify(unsorted_list, one_by_one, 0)

    return unsorted_list


def random_list(random_start, random_stop, random_decimal, random_number):
    """
    This function will generate a random list and will store them in a list
    First Part

    Parameters
    ----------
    random_start : Lower value of the random numbers to be generated
    random_stop : Highest value of the random numbers to be generated
    random_decimal: NUmber of decimal og the generated number
    random_number: Number of the list elements

    Returns
    -------
    A list of random numbers

    Raises
    ------
    None
    """
    random_float_list = []  # Initializing the list
    for i_ndex in range(0, random_number - 1):  # Starting the loop 11 times
        # Round the random number
        # between random_start and
        # random_end with random_decimal decimals
        x = round(random.uniform(random_start, random_stop), random_decimal)
        random_float_list.append(x)  # Adding the new generated random number to the end of the list
    return random_float_list  # The function returns the list full of random float


def get_user_inputs():
    """
    This function will take input from the user

    Parameters
    ----------

    Returns
    -------
    user_inputs_random_start : Lower value of the random numbers to be generated
    user_inputs_random_stop : Highest value of the random numbers to be generated
    user_inputs_random_decimal: NUmber of decimal og the generated number
    user_inputs_random_number: Number of the list elements

    Raises
    ------
    A ValueError if the input is not the correct type
    """

    try:
        user_inputs_random_start = float(input("Enter the start of the random list): "))
    except ValueError:
        print("That's not a float")
        user_inputs_random_start = 50.50  # Stored the default value

    try:
        user_inputs_random_end = float(input("Enter the end of the random list): "))
    except ValueError:
        print("That's not a float")
        user_inputs_random_end = 500.50  # Stored the default value
    try:
        user_inputs_random_decimal = int(input("Enter the number of decimal): "))
    except ValueError:
        print("That's not an int")
        user_inputs_random_decimal = 2  # Stored the default value

    try:
        user_inputs_random_number = int(input("Enter the number of random generated): "))
    except ValueError:
        print("That's not an int")
        user_inputs_random_number = 10  # Stored the default value

    return random_list(user_inputs_random_start, user_inputs_random_end, user_inputs_random_decimal,
                       user_inputs_random_number)


def print_menu():
    # Text menu

    menu_option = True
    menu_list_option = [0, 1, 2, 3, 4, 5, 6, 101]
    user_choice = 0  # The choice has gone wrong

    while menu_option:

        print(COLOR_RED, "Kindly choose the sorting algorithm you would like to use", COLOR_RESET)
        print(COLOR_GREEN, "Press 1 for Bubble Sort :")
        print(" Press 2 for Merge Sort :")
        print(" Press 3 for Insertion Sort :")
        print(" Press 4 for Shell Sort :")
        print(" Press 5 for Selection Sort :")
        print(" Press 6 for Heap Sort :")
        print(" Press 101 for measuring the speed of each algorithm :")
        print(" Press 0 for Exit :", COLOR_RESET)

        try:
            user_choice = int(input(" Enter your choice : "))

            if isinstance(user_choice, int) and user_choice in menu_list_option:
                menu_option = False  # This will make the while loop to end

        except TypeError:  # Check what choice was entered and act accordingly
            print('Invalid option. Please enter a number between 0 and 5.')

    return user_choice


def check_execution_time(list_to_process, list_of_functions):
    # We will test each function and store the result
    """
    This function will compute the execution time of a set of functions against all the sorting algorithm

    Parameters
    ----------
    list_to_process : The list to be processed
    list_of_functions : The list containing the function to be processed

    Returns
    -------
    dict_to_process : The updated dictionary with the execution time as the value of each entry

    Raises
    ------
    None
    Get the speed of python functions
    It's possible to do so :
    dict_to_process["len() of Python"] = time.time() - start_time
    Need to be sure that the dict does not get some execution time
    The logic behind the next speed is that all the function are executed in the exact same conditions

    """
    sp = SortingPerformance(list_to_process, list_of_functions)

    return sp.process_speed()


def display_speed():
    list_of_functions = [bubble_sort, merge_sort, insertion_sort, shell_sort, selection_sort, heap_sort]

    dict_of_speed_results = check_execution_time(random_list(0, 10000, 3, 10), list_of_functions)

    # Sorting the dictionary by values using a lambda function in the key argument of sorted()
    # This function returns the key-value pairs of a dictionary as a list of tuples
    print(COLOR_GREEN)
    print("{:<25} {:<25}".format('SORTING ALGORITHM', 'SPEED'))  # Specifying the headers and the space between column
    print(COLOR_RESET)

    # Getting the sorted list in a tuple
    # Using lambda function to get the value of a dictionary item
    # without having to import the operator module for itemgetter() and avoiding to import operator package
    # Here, key=lambda item: item[1] returns the values of each key:value pair
    # From each key:value pairs of dict_of_speed_results.item(), sorted() sorts the items based on values (speed)

    sorted_tuples = sorted(dict_of_speed_results.items(), key=lambda item: item[1])  # item[1] = the value

    sorted_dict_of_speed_results = {k: v for k, v in sorted_tuples}
    for key, value in sorted_dict_of_speed_results.items():  # Going throughout the sorted dictionary
        v_function = key
        v_speed = value
        print("{:<25} {:<25}".format(str(v_function), v_speed))

    draw_bars(dict_of_speed_results)
    # draw_seaborn(dict_of_speed_results)


def draw_bars(dict_to_plot):
    # Drawing a bar plot with matplotlib

    names = list(dict_to_plot.keys())
    values = list(dict_to_plot.values())
    plt.title("Sorting Algorithm Performance")
    plt.ylabel("Performance")
    plt.bar(range(len(dict_to_plot)), values, tick_label=names)
    plt.show()


def draw_seaborn(dict_to_plot):
    # Drawing a bar plot with seaborn
    sns.barplot(list(dict_to_plot.keys()), list(dict_to_plot.values()), palette='Blues_d')
    plt.title('Performance')
    plt.xlabel('Algorithm')
    plt.ylabel('Count')
    plt.show()


# Driver code
def main():
    # Define main() function for auto test

    # Need to get over the default recursion limit which is 1.000
    sys.setrecursionlimit(10100)

    # Getting the list of 10.000 floats elements to be sorted
    list_to_process = get_user_inputs()
    # Allowing the user to choose the sorting algorithm he would like to use
    get_algorithm_choice = print_menu()

    if get_algorithm_choice == 0:
        exit(0)
    elif get_algorithm_choice == 1:
        print(bubble_sort(list_to_process))
    elif get_algorithm_choice == 2:
        print(merge_sort(list_to_process))
    elif get_algorithm_choice == 3:
        print(insertion_sort(list_to_process))
    elif get_algorithm_choice == 4:
        print(shell_sort(list_to_process))
    elif get_algorithm_choice == 5:
        print(selection_sort(list_to_process))
    elif get_algorithm_choice == 6:
        print(heap_sort(list_to_process))
    elif get_algorithm_choice == 101:
        display_speed()


if __name__ == '__main__':
    # Execute main() function in standalone mode
    main()
