import heapq

def merge_sorted_arrays(arrays):
    heap = []
    result = []

    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(heap, (arr[0], i, 0))

    while heap:
        value, arr_index, element_index = heapq.heappop(heap)
        result.append(value)

        if element_index + 1 < len(arrays[arr_index]):
            next_value = arrays[arr_index][element_index + 1]
            heapq.heappush(
                heap,
                (next_value, arr_index, element_index + 1)
            )

    return result

arrays = [
    [1, 4, 7],
    [2, 5, 8, 11],
    [3, 6, 9, 10]
]

print("Merged Array:")
print(merge_sorted_arrays(arrays))