import numpy as np


arr = [4,1,1,9,1]
def ref_opt(arr,i):
    if i == 0:
        return arr[0]
    elif i == 1:
        return max(arr[0],arr[1])
    else:
        A = ref_opt(arr,i - 2) + arr[i]
        B = ref_opt(arr,i - 1)
        return max(A,B) 
print(ref_opt(arr,4)) 


def dp_opt(arr):
    opt = np.zeros(len(arr)) 
    opt[1] = max(arr[0],arr[1])
    for i in range(2,len(arr)):
         A = opt[i - 2] + arr[i]
         B = opt[i - 1]
         opt[i] = max(A,B)
    return opt[len(arr) - 1]    
print(dp_opt(arr))


arr = [3,34,4,12,5,2]
def rec_subSet(arr,i,s):
    if s == 0:
        return True
    elif i == 0:
        return arr[0] == s
    elif arr[i] > s:
        return  rec_subSet(arr,i - 1,s)
    else:
        A = rec_subSet(arr,i - 1,s - arr[i])
        B = rec_subSet(arr,i - 1,s)
        return A or B
print(rec_subSet(arr,len(arr) - 1,9))

def dp_subSet(arr,S):
    subSet =np.zeros((len(arr),S + 1),dtype=bool)
    subSet[:,0] = True
    subSet[0,:] = False
    subSet[0,arr[0]] = True

    for i in range(1,len(arr)):
        for s in range(1,S + 1):
            if arr[i] > s:
                subSet[i,s] = subSet[i - 1,s]
            else:
                A = subSet[i - 1,s - arr[i]]
                B = subSet[i - 1,s]
                subSet[i,s] = A or B
    r,c = subSet.shape
    return subSet[r - 1,c - 1]

print(dp_subSet(arr,13))
print(dp_subSet(arr,12))
print(dp_subSet(arr,11))
print(dp_subSet(arr,10))
print(dp_subSet(arr,9))