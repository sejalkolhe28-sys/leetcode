
class Solution:
    def countServers(self, n, logs, x, queries):

        logs.sort(key=lambda a: a[1])

        # Store queries with their original indices
        sorted_queries = sorted(
            [(q, i) for i, q in enumerate(queries)]
        )

        count = {}
        ans = [0] * len(queries)

        left = 0
        right = 0
        active = 0

        for q, idx in sorted_queries:

            start = q - x

            # Add logs within the right boundary
            while right < len(logs) and logs[right][1] <= q:
                server = logs[right][0]

                if count.get(server, 0) == 0:
                    active += 1

                count[server] = count.get(server, 0) + 1
                right += 1

            # Remove logs outside the left boundary
            while left < right and logs[left][1] < start:
                server = logs[left][0]

                count[server] -= 1

                if count[server] == 0:
                    active -= 1

                left += 1

            ans[idx] = n - active

        return ans
