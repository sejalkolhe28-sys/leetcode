
from sortedcontainers import SortedList
import heapq

class Solution:
    def busiestServers(self, k, arrival, load):
        available = SortedList(range(k))
        busy = []
        count = [0] * k

        for i in range(len(arrival)):
            time = arrival[i]

            # Free servers whose requests have finished
            while busy and busy[0][0] <= time:
                finish, server = heapq.heappop(busy)
                available.add(server)

            if not available:
                continue

            # Find server i % k or the next available server
            idx = available.bisect_left(i % k)

            if idx == len(available):
                idx = 0

            server = available.pop(idx)

            # Assign request
            count[server] += 1
            finish_time = time + load[i]

            heapq.heappush(busy, (finish_time, server))

        max_requests = max(count)

        return [i for i in range(k) if count[i] == max_requests]
