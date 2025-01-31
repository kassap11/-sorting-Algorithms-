def quick(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot=arr[0]
        left=[]
        right=[]
        for i in arr[1:]:
            if i <pivot:
                left.append(i)
            else:
                right.append(i)
                
        sorted_left=quick(left)
        sorted_right=quick(right)
        return sorted_left+[pivot]+sorted_right 
    
arr = [64, 25, 12, 22, 11]
print(quick(arr))     



