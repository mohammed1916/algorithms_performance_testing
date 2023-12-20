import random
import timeit
# Comb Sort Implementation
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

# Gnome Sort Implementation
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

# Function to create a partially sorted array
def generate_partially_sorted_array(size, percent_sorted):
    arr = list(range(1, size + 1))
    num_elements_to_shuffle = int((100 - percent_sorted) / 100 * size)
    random.shuffle(arr[:num_elements_to_shuffle])
    return arr

# Function to perform performance testing on partially sorted array
def performance_test_on_partially_sorted(sort_function, array_size, percent_sorted):
    arr = generate_partially_sorted_array(array_size, percent_sorted)

    start_time = timeit.default_timer()
    sort_function(arr)
    end_time = timeit.default_timer()

    return end_time - start_time

# Test performance with different array sizes and degrees of sortedness
array_sizes = [100, 500, 1000, 5000, 10000]
percentages_sorted = [10, 30, 50, 70, 90]

for size in array_sizes:
    for percent_sorted in percentages_sorted:
        comb_time = performance_test_on_partially_sorted(comb_sort, size, percent_sorted)
        gnome_time = performance_test_on_partially_sorted(gnome_sort, size, percent_sorted)

        print(f"Array Size: {size}, Percent Sorted: {percent_sorted}%")
        print(f"Comb Sort Time: {comb_time:.6f} seconds")
        print(f"Gnome Sort Time: {gnome_time:.6f} seconds")
        print("---")