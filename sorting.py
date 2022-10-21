import sys


# insertion sort printing after each iteration
def insertion_sort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
        print(*A, sep=",")


# selection sort printing after each iteration
def selection_sort(A):
    for i in range(len(A)):
        min = i
        for j in range(i + 1, len(A)):
            if A[j] < A[min]:
                min = j
        if i != min:
            A[i], A[min] = A[min], A[i]
            print(*A, sep=",")


# merge sort iteratively printing after each iteration
def merge_iterative(A, temp, frm, mid, to):
    k = frm
    i = frm
    j = mid + 1
    while i <= mid and j <= to:
        if A[i] < A[j]:
            temp[k] = A[i]
            i = i + 1
        else:
            temp[k] = A[j]
            j = j + 1

        k = k + 1

    # fill in residual elements
    while i < len(A) and i <= mid:
        temp[k] = A[i]
        k = k + 1
        i = i + 1
    # waste of memory but need to reflect the sorted list
    for i in range(frm, to + 1):
        A[i] = temp[i]


# Iteratively sort sublist `A[low…high]` using a temporary list
def mergesort_iterative(A):
    print(*A, sep=",")
    low = 0
    high = len(A) - 1
    temp = A.copy()
    m = 1
    while m <= high - low:
        for i in range(low, high, 2 * m):
            frm = i
            mid = i + m - 1
            to = min(i + 2 * m - 1, high)
            merge_iterative(A, temp, frm, mid, to)
        m = 2 * m
    print(*A, sep=",")


# merge sort recursively printing after each iteration
# MergeSort in Python

def merge_sort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid + 1, end)
        merge(arr, start, mid, end)


def merge(arr, start, mid, end):
    # creating a temp array
    temp = [0] * (end - start + 1)
    # initial indexes of first and second subarrays
    i, j = start, mid + 1
    # initial index of merged subarry array
    k = 0
    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            k += 1
            i += 1
        else:
            temp[k] = arr[j]
            k += 1
            j += 1
    # add remaining elements of the first subarray
    while i <= mid:
        temp[k] = arr[i]
        k += 1
        i += 1
    # add remaining elements of the second subarray
    while j <= end:
        temp[k] = arr[j]
        k += 1
        j += 1
    # copy temp array to the original array
    for i in range(start, end + 1):
        arr[i] = temp[i - start]
    print(*arr, sep=",")


# quick sort recursively printing after each iteration and choosing first element as pivot
def quick_sort(arr, low, high):
    if low <= high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


# quick sort partition with first element being the pivot and two pointers starting from low and high
def partition(arr, low, high):
    init_high= high
    init_low= low
    search_from_high = True
    pivot = arr[low]
    while low < high and low < len(arr):

        # search starting from high
        if search_from_high:
            while arr[high] > pivot and high != low:
                high -= 1
            if high > low:
                arr[low] = arr[high]
                print(*arr, sep=",")
                low += 1
                search_from_high = False
        else:
            while arr[low] <= pivot and high != low :
                low += 1
            arr[high] = arr[low]
            print(*arr, sep=",")
            high -= 1
            search_from_high = True
    arr[low] = pivot
    print(*arr, sep=",")
    return low



# arr = [9, 3, 6, 4, 0, 1, 2, 7, 8, 0]
# print(*arr, sep=",")
# insertion_sort(arr)
# selection_sort(arr)
# mergesort_iterative(arr)
# merge_sort(arr, 0, len(arr) - 1)
# quick_sort(arr, 0, len(arr) - 1)
# print(*arr, sep=",")

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 0:
        print("Please enter a list of numbers to sort")
        sys.exit(1)
    passed_args = [x for x in args]
    filename, option = passed_args[0], passed_args[1]
    file = open(filename, "r")
    arr = [int(x) for x in file.readline().strip().split(',') if x.isdigit()]
    print(*arr, sep=",")
    if option == "1":
        insertion_sort(arr)
    elif option == "2":
        selection_sort(arr)
    elif option == "3":
        quick_sort(arr, 0, len(arr) - 1)
    elif option == "4":
        merge_sort(arr, 0, len(arr) - 1)
    print(*arr, sep=",")
pass
