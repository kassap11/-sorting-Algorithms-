def selection(arr):
    min=0
    for i in range(len(arr)):
        min=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[i]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]
        
arr = [64, 25, 12, 22, 11]
print("Original array:", arr)
# Call the selection_sort function
selection(arr)

# Print the sorted array
print("Sorted array:", arr)               












