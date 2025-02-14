def two_sum(target,arr):
    l= len(arr)
    for i in range(l-1):
        for j in range(i+1,l):
            if arr[i]+arr[j] == target:
                return 'YES'
    return 'NO'    
            
print(two_sum(204,[575,330,339,584,239,31,173,929,967]))