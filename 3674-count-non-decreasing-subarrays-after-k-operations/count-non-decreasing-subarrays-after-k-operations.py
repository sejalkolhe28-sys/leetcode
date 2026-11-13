
from collections import deque

class Solution:
    def countNonDecreasingSubarrays(self, nums, k):
        n = len(nums)
        dq = deque()

        right = n - 1
        cost = 0
        ans = 0

        for left in range(n - 1, -1, -1):
            x = nums[left]
            count = 1

            # Merge smaller or equal values
            while dq and dq[0][0] <= x:
                val, cnt = dq.popleft()

                cost += (x - val) * cnt
                count += cnt

            dq.appendleft([x, count])

            # Reduce window while cost exceeds k
            while cost > k:
                val, cnt = dq[-1]

                cost -= val - nums[right]
                cnt -= 1

                if cnt == 0:
                    dq.pop()
                else:
                    dq[-1][1] = cnt

                right -= 1

            # Count valid subarrays
            ans += right - left + 1

        return ans
