
class Solution {
public:
    static const int MOD = 1e9 + 7;

    int uniquePaths(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();

        vector<vector<int>> right(m, vector<int>(n, -1));
        vector<vector<int>> down(m, vector<int>(n, -1));

        // Precompute mirror destinations in reverse order.
        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {

                if (grid[i][j] == 0) {
                    right[i][j] = i * n + j;
                    down[i][j] = i * n + j;
                } 
                else {
                    // Entering mirror while moving right:
                    // reflected downward.
                    if (i + 1 < m)
                        right[i][j] = down[i + 1][j];

                    // Entering mirror while moving down:
                    // reflected rightward.
                    if (j + 1 < n)
                        down[i][j] = right[i][j + 1];
                }
            }
        }

        vector<vector<int>> dp(m, vector<int>(n, 0));
        dp[0][0] = 1;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {

                if (grid[i][j] == 1 || dp[i][j] == 0)
                    continue;

                // Attempt to move right.
                if (j + 1 < n) {
                    int dest = right[i][j + 1];

                    if (dest != -1) {
                        int x = dest / n;
                        int y = dest % n;

                        dp[x][y] = (dp[x][y] + dp[i][j]) % MOD;
                    }
                }

                // Attempt to move down.
                if (i + 1 < m) {
                    int dest = down[i + 1][j];

                    if (dest != -1) {
                        int x = dest / n;
                        int y = dest % n;

                        dp[x][y] = (dp[x][y] + dp[i][j]) % MOD;
                    }
                }
            }
        }

        return dp[m - 1][n - 1];
    }
};
