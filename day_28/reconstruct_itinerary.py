from collections import defaultdict, deque


class Solution:
    def dfs(self, graph, stack, res):
        while stack:
            curr = stack[-1]
            if curr in graph and len(graph[curr]) > 0:
                stack.append(graph[curr].pop())
            else:
                res.append(stack.pop())
        return res

    def findItinerary(self, tickets):
        tickets_graph = defaultdict(list)

        # create an adj list to represent flights graph
        for origin, des in tickets:
            tickets_graph[origin].append(des)

        # sort all destinations in a lexical order O(V*log(V)) where v is the number of airports
        for origin in tickets_graph.keys():
            tickets_graph[origin].sort(reverse=True)

        # dfs to traverse all possible flights, Time: O(N) where N is the number of flights
        fly_path = self.dfs(tickets_graph, ["JFK"], [])

        return fly_path[::-1]


ts = Solution()
print(ts.findItinerary([["JFK", "QQQ"], ["JFK", "AAA"], ["QQQ", "JFK"]]))
