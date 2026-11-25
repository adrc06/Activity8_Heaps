import heapq

jobs = [
    ("Job A", 3),
    ("Job B", 5),
    ("Job C", 1),
    ("Job D", 4)
]

priority_queue = []

for job, priority in jobs:
    heapq.heappush(priority_queue, (-priority, job))

print("Release Order:")

while priority_queue:
    priority, job = heapq.heappop(priority_queue)
    print(job)