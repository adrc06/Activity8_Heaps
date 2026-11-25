import heapq

heap = []

numbers = [5, 9, 11, 14, 19, 17, 18, 13]

for num in numbers:
    heapq.heappush(heap, num)

print("Size:", len(heap))
print("Peek:", heap[0])

print("Extraction Order:")
while heap:
    print(heapq.heappop(heap), end=" ")
