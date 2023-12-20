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

# Function to perform performance testing
def performance_test(sort_function, array_size):
    # Generate a random array
    arr = [random.randint(1, 1000) for _ in range(array_size)]

    # Measure the execution time
    start_time = timeit.default_timer()
    sort_function(arr)
    end_time = timeit.default_timer()

    return end_time - start_time

# Test performance with different array sizes
array_sizes = [100, 500, 1000, 5000, 10000]

for size in array_sizes:
    comb_time = performance_test(comb_sort, size)
    gnome_time = performance_test(gnome_sort, size)

    print(f"Array Size: {size}")
    print(f"Comb Sort Time: {comb_time:.6f} seconds")
    print(f"Gnome Sort Time: {gnome_time:.6f} seconds")
    print("---")
