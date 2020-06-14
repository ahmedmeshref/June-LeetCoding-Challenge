"""
There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the
cheapest price from src to dst with up to k stops. If there is no such route, output -1.
"""

from collections import defaultdict


class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        graph = defaultdict(list)
        for s, d, w in flights:
            graph[s].append((d, w))
        self.ans = float('inf')

        def dfs(src, des, k, cost):
            if src == des:
                self.ans = min(self.ans, cost)
                return
            if k == 0:
                return
            for n_src, price in graph[src]:
                new_cost = cost + price
                if new_cost >= self.ans:
                    continue
                dfs(n_src, des, k - 1, new_cost)

        dfs(src, dst, k + 1, 0)
        return self.ans if self.ans != float('inf') else -1


n = 4
edges = [[0, 1, 100], [1, 3, 50], [3, 2, 100], [1, 2, 100], [0, 2, 500]]
src = 0
dst = 2
k = 2
g = Solution()
print(g.findCheapestPrice(n, edges, src, dst, k))
