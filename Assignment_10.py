import numpy as np

arr = np.arange(1, 11)

print("Original Array:", arr)

print("Slicing [1:5]:", arr[1:5])
print("First Three Elements:", arr[:3])
print("Last Three Elements:", arr[-3:])
print("Every Second Element:", arr[::2])
print("Reverse Array:", arr[::-1])

print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

print("Array + 5:", arr + 5)
print("Array * 2:", arr * 2)
