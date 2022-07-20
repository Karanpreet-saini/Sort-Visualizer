import time


def insertion(N, array, display, timeTick):
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        display(array, ['yellow' if a == i or a == i + 1 else 'green' if a <= j
        else 'cyan' for a in range(N)])
        time.sleep(timeTick)
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            display(array, ['pink' if a == i else 'green' if a <= j else 'cyan' for a in range(N)])
            time.sleep(timeTick)
            i -= 1
        array[i + 1] = key
    display(array, ['yellow' for _ in range(N)])
