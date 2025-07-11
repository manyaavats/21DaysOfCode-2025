Your task: Find any peak element's index using efficient divide-and-conquer approach.

def find_peak_element(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        mid = (start + end) // 2

        if arr[mid] > arr[mid + 1]:
            end = mid
        else:
            start = mid + 1

    return start
