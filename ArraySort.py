def sortThis(array):
    for num in range(len(array)-1,0,-1):
        for i in range(num):
            if array[i]>array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
    return array


array = [1,2,5,-1,3]
print(sortThis(array))