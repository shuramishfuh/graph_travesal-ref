# insertion sort printing after each iteration
def insertion_sort(A):
    print(A)
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
        print(A)
    print(A)


# selection sort printing after each iteration
def selection_sort(A):
    for i in range(len(A)):
        copy = A.copy()
        min = i
        for j in range(i + 1, len(A)):
            if A[j] < A[min]:
                min = j
        A[i], A[min] = A[min], A[i]
        if not copy.__eq__(A): print(copy)
    print(A)
    print(A)


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
    print(A)
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
    print(A)





arr = [9, 3, 6, 4, 0, 1, 2, 7, 8, 0]
# insertion_sort(arr)
# selection_sort(arr)
# mergesort_iterative(arr)
