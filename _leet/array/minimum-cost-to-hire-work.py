# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/solution/


class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        from fractions import Fraction
        ans = float('inf')

        N = len(quality)
        for captain in xrange(N):
            # Must pay at least wage[captain] / quality[captain] per qual
            factor = Fraction(wage[captain], quality[captain])
            prices = []
            for worker in xrange(N):
                price = factor * quality[worker]
                if price < wage[worker]: continue
                prices.append(price)

            if len(prices) < K: continue
            prices.sort()
            ans = min(ans, sum(prices[:K]))

        return float(ans)

s=Solution()
quality = [10,20,5]
wage = [70,50,30]
K = 2
print(s.mincostToHireWorkers(quality, wage, K))
