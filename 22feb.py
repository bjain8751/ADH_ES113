#Heap sort on arrays

#fuctions: buildheap, shift_down, heap_sort

array=[8,9,2,3,4,53,5,43,9] #array to be sorted #is not currently a heap

#buildheap: builds a heap from an array
def buildheap(l, index):
    if(index>=len(l)): #if the index is out of bounds simply return 
        return
    buildheap(l, 2*index+1) #calls build heap on the left and right children
    buildheap(l, 2*index+2) 
    shift_down(l, index)
    return

#shiftdown: shifts the value at the root node to the correct position, given both the children are heap
def shift_down(l, index):
    if(index*2+1>=len(l)): #if no children, simply return
        return
    min_value=l[index]
    min_index=index
    if(index*2+1<len(l)): #if left child exists, check if it is smaller than the root
        if(l[index*2+1]<min_value):
            min_value=l[index*2+1]
            min_index=index*2+1
    if(index*2+2<len(l)):  #if right child exists, check if it is smaller than the root
        if(l[index*2+2]<min_value):
            min_value=l[index*2+2]
            min_index=index*2+2
    if(min_index!=index): #if the root is not the smallest, swap it with the smallest child and call shiftdown on the child
        l[index], l[min_index]=l[min_index], l[index]
        shift_down(l, min_index)
    return

#takes any array, builds a heap and then sorts it
def heapsort(l):
    sorted_list=[]
    n=len(l)
    buildheap(l,0) #builds a heap from the array
    for i in range(n): #takes the root of the heap and appends it to the sorted list, then replaces the root with the last element and calls shiftdown on the root
        sorted_list.append(l[0])
        l[0]=l[len(l)-1]
        l.pop()
        shift_down(l, 0)
        
    return sorted_list

print(heapsort(array))
    