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

# Test the algorithms with a sample array
sample_array = [64, 34, 25, 12, 22, 11, 90]
comb_sorted_array = sample_array.copy()
gnome_sorted_array = sample_array.copy()

comb_sort(comb_sorted_array)
gnome_sort(gnome_sorted_array)

print("Original Array:", sample_array)
print("Comb Sorted Array:", comb_sorted_array)
print("Gnome Sorted Array:", gnome_sorted_array)
