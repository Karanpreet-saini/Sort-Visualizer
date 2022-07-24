import time

def merge(n, arr, l, m, r,draw,tick):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]
        draw(arr, ['red' if x == l or x == i else 'grey' for x in range(n)])
        time.sleep(tick)

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
        draw(arr, ['red' if x == l or x == j else 'grey' for x in range(n)])
        time.sleep(tick)

    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
            draw(arr, ['green' if x == l or x == i else 'grey' for x in range(n)])
            time.sleep(tick)
        else:
            arr[k] = R[j]
            j += 1
            draw(arr, ['green' if x == l or x == i else 'grey' for x in range(n)])
            time.sleep(tick)
        k += 1
        draw(arr, ['green' if x == l or x == i else 'grey' for x in range(n)])
        time.sleep(tick)

    while i < n1:
        arr[k] = L[i]
        draw(arr, ['green' if x == l or x == j else 'grey' for x in range(n)])
        time.sleep(tick)
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        draw(arr, ['green' if x == l or x == j else 'grey' for x in range(n)])
        time.sleep(tick)
        j += 1
        k += 1


def mergesort(n, arr, left, right, draw, tick):
    if left < right:
        m = (left + right) // 2
        mergesort(n, arr, left, m, draw, tick)
        mergesort(n, arr, m + 1, right, draw, tick)
        merge(n, arr, left, m, right, draw, tick)