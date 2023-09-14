import numpy as np

arr = [[4, 5, 6, 4], [1, 2, 3, 6]]

num = np.ndim(arr)  # this ndim() method show number of axes in array

arrayShape = np.shape(arr)  # The shape method show Number of Rows and Column in Array

print("axes in array : " + str(num))
print("Number of Row and Column" + str(arrayShape))
