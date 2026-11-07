
import heapq

class Solution:
    def assignTasks(self, servers, tasks):

        n = len(servers)

        # Available servers: (weight, index)
        available = [(servers[i], i) for i in range(n)]
        heapq.heapify(available)

        # Busy servers: (free_time, weight, index)
        busy = []

        ans = []
        time = 0

        for j in range(len(tasks)):

            # Task j arrives at second j
            time = max(time, j)

            # Release all servers that have finished
            while busy and busy[0][0] <= time:
                free_time, weight, index = heapq.heappop(busy)
                heapq.heappush(available, (weight, index))

            # If no server is free, wait
            if not available:
                time = busy[0][0]

                # Release all servers free at this time
                while busy and busy[0][0] <= time:
                    free_time, weight, index = heapq.heappop(busy)
                    heapq.heappush(available, (weight, index))

            # Select the best available server
            weight, index = heapq.heappop(available)

            # Store the assigned server
            ans.append(index)

            # Calculate when this server becomes free
            heapq.heappush(
                busy,
                (time + tasks[j], weight, index)
            )

        return ans
