def merg(arr):
    if len(arr)<=1:
        return arr
    else:
        mid=len(arr)//2
        left= merg(arr[:mid])
        right= merg(arr[mid:])
        return merg_sort(left,right)
    
def merg_sort(left,right):
    sorted_list=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            sorted_list.append(left[i])
            i=i+1 
        else:
            sorted_list.append(right[j])
            j=j+1
    if i==len(left):
        sorted_list.extend(right[j:])
    else:
        sorted_list.extend(left[i:])
    return sorted_list                 
                   
arr = [64, 25, 12, 22, 11]
print(merg(arr))
        
        
       

                         