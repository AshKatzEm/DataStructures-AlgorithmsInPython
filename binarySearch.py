"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""
# recursive
# def binary_search(input_input_arrayay, value):
#     n = len(input_input_arrayay) - 1
#     if n % 2 == 0:
#         index = int(n/2)
#     elif n % 2 != 0:
#         index = int((n+1)/2)
#     else:
#         return "error"
#     midpoint = input_input_arrayay[index]
#     #print("input_input_arrayay: ", input_input_arrayay, " value: ", value, "n: ", n, " index: ", index, " midpoint: ", midpoint)
#     if value > midpoint and n > 0:
#         #print(value," is greater than ", midpoint, " so ninput_arrayow it to: ",input_input_arrayay[index+1:n+1])
#         return binary_search( input_input_arrayay[index+1:n+1], value)
#     elif value < midpoint and n > 0:
#         #print(value," is less than ", midpoint, " so ninput_arrayow it to: ", input_input_arrayay[0:index])
#         return binary_search( input_input_arrayay[0:index], value)
#     else:
#         if value == midpoint:
#             return midpoint
#         else:
#             return "no such value"

def binary_search(input_array, value):
    print(input_array)
    low = 0
    high = len(input_array) - 1
    mid = 0
    print("low, mid, high:", low, mid, high, sep = " ")
    while low <= high:
        mid = (high + low) // 2
        print(low, " is less then or equal to", high, "so mid=", high, "+", low, "/", 2, sep=" ")
        # If value is greater, ignore left half
        if input_array[mid] < value:
            low = mid + 1
            print("input_array[",mid,"] is less than ", value, "so low =", mid, "+", 1, sep=" ")

        # If value is smaller, ignore right half
        elif input_array[mid] > value:
            high = mid - 1
            print("input_array[",mid,"] is greater than ", value, "so high =", mid, "-", 1, sep=" ")

        # means value is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1


test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))