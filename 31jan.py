# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
    
    
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
    
    
#give the sum of all the numbers in the list

# def sum_list(l): 

## Binary Search using recursion

# To find whether k is present in array arr
def binary_search(arr, left, right, k):
    if(left>right):
        return -1  # k is not present in the array
    else:
        mid = int((left+right)/2)
        if(arr[mid]==k):
            return mid
        elif(k>arr[mid]):
            # Element is present in the right half of the array
            return binary_search(arr, mid+1, right, k)
        else:
            # Element is present in the left half of the array
            return binary_search(arr, left, mid-1, k)

# print(binary_search([1,2,3,4,5,6,7,8,9,10], 0, 9, 10))


    
#give the sum of all the numbers in the list

def sum_list(l):
    if len(l)==0:
        return 0
    elif len(l)==1:
        return l[0]
    else:
        return l[0] + sum_list(l[1:])
    
    
print(sum_list([1,2,3,4,5,6,7,8,9,10]))
