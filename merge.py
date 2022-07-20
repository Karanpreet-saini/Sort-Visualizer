import time


def mergesort(n, arr, left, right, draw, tick):
    if left < right:
        m = (left + right) // 2
        mergesort(n, arr, left, m, draw, tick)
        mergesort(n, arr, m + 1, right, draw, tick)

        j = m + 1
        if arr[m] <= arr[m + 1]:
            return

        while left <= m and j <= right:
            draw(arr, ['blue' if x == left or x == j else 'grey' for x in range(n)])
            time.sleep(tick)
            if arr[left] <= arr[j]:
                left += 1
            else:
                draw(arr, ['red' if x == left or x == j else 'grey' for x in range(n)])

                # array of colours where only the focused bars
                # are displayed red since left > arr[j]
                time.sleep(tick)
                temp = arr[j]
                i = j
                while i != left:
                    arr[i] = arr[i - 1]
                    draw(arr, ['red' if x == i or x ==
                                        j else 'grey' for x in range(n)])
                    time.sleep(tick)
                    i -= 1
                arr[left] = temp

                draw(arr, ['green' if x == left or x == j else 'grey' for x in range(n)])
                time.sleep(tick)
                left += 1
                m += 1
                j += 1

