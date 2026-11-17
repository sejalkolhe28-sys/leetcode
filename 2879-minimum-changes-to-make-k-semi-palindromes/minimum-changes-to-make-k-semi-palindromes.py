
class Solution:
    def minimumChanges(self, s, k):
        n = len(s)
        INF = float('inf')

        # Precompute minimum changes for every substring.
        cost = [[INF] * n for _ in range(n)]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0
                    group_size = length // d

                    for r in range(d):
                        for t in range(group_size // 2):
                            left = i + r + t * d
                            right = i + r + (group_size - 1 - t) * d

                            if s[left] != s[right]:
                                changes += 1

                    cost[i][j] = min(cost[i][j], changes)

        # DP: minimum changes to divide prefix into p parts.
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for p in range(1, k + 1):
            for end in range(2 * p, n + 1):
                for start in range(2 * (p - 1), end - 1):
                    dp[end][p] = min(
                        dp[end][p],
                        dp[start][p - 1] + cost[start][end - 1]
                    )

        return dp[n][k]
