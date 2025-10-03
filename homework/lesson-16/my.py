import numpy as np

lst = [12.23, 13.32, 100, 36.32]
arr = np.array(lst)

print("Original List:", lst)
print("One-dimensional NumPy array:", arr)

arr = np.arange(2, 11).reshape(3, 3)
print(arr)
arr = np.zeros(10)
print("Null Vector:", arr)

arr[5] = 11
print("Update sixth value to 11:", arr)
arr = np.arange(12, 38)
print(arr)
arr = np.array([1, 2, 3, 4])
print("Original array:", arr)

arr_float = arr.astype(float)
print("Converted to float:", arr_float)
celsius = np.array([0, 12, 45.21, 34, 99.91, 0])
fahrenheit = celsius * 9/5 + 32

print("Values in Celsius degrees:", celsius)
print("Values in Fahrenheit degrees:", fahrenheit)
arr = np.array([10, 20, 30])
print("Original array:", arr)

arr = np.append(arr, [40, 50, 60, 70, 80, 90])
print("After append values to the end of the array:", arr)
arr = np.random.randint(1, 100, 10)
print("Array:", arr)

print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))
arr = np.random.rand(10, 10)
print("10x10 Array:\n", arr)

print("Minimum value:", np.min(arr))
print("Maximum value:", np.max(arr))
arr = np.random.rand(3, 3, 3)
print(arr)
