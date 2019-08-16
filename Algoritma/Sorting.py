import time
import random
import InsertionSort, MergeSort
    
if __name__ == "__main__":
    array_size = 10000
    arr = random.sample(range(1, 10001), array_size)
    arr_2 = list(arr)

    start_merge = time.time()
    MergeSort.merge_sort(arr)
    end_merge = time.time()

    start_insertion = time.time()
    InsertionSort.insertion_sort(arr_2)
    end_insertion = time.time()

    print("Merge sort :  %s seconds" % (end_merge - start_merge))
    print("Insertion sort :  %s seconds" % (end_insertion - start_insertion))
