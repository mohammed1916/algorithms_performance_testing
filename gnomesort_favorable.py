import timeit
import random

def comb_sort(arr):
    gap = len(arr)
    shrink = 1.3
    swapped = True

    while gap > 1 or swapped:
        gap = max(1, int(gap / shrink))
        swapped = False

        for i in range(len(arr) - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True

def gnome_sort(arr):
    index = 0

    while index < len(arr):
        if index == 0:
            index += 1
        if arr[index] >= arr[index - 1]:
            index += 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1

# Function to generate a dataset favoring Gnome Sort
def generate_gnome_sort_favorable_data(size):
    arr = list(range(1, size + 1))
    # Reverse the first few elements
    reverse_start = int(0.2 * size)
    arr[:reverse_start] = reversed(arr[:reverse_start])
    return arr

# Function for performance testing
def performance_test(sort_function, arr):
    start_time = timeit.default_timer()
    sort_function(arr)
    end_time = timeit.default_timer()
    return end_time - start_time

# Test performance with a dataset favoring Gnome Sort
array_size = 1000
gnome_sort_favorable_data = generate_gnome_sort_favorable_data(array_size)

comb_time = performance_test(comb_sort, gnome_sort_favorable_data.copy())
gnome_time = performance_test(gnome_sort, gnome_sort_favorable_data.copy())

print("Array Size:", array_size)
print("Comb Sort Time:", comb_time, "seconds")
print("Gnome Sort Time:", gnome_time, "seconds")
