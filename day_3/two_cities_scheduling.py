"""
There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0],
and the cost of flying the i-th person to city B is costs[i][1].
Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

Example 1:
Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation:
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.

Note:
1 <= costs.length <= 100
It is guaranteed that costs.length is even.
1 <= costs[i][0], costs[i][1] <= 1000
"""


def two_city_sched_cost(costs):
    """
    :param costs: List of lists where costs[i] = [A[i], B[i]] where A[i] represents the cost of flying the i-th person
     to city A and B[i] is the costs of flying the i-th person to city B.
    :return: Number represents the the min cost to fly every person to a city such that exactly N people arrive in
     each city
    """
    # sort the given costs based on the difference between A[i] and B[i]
    costs.sort(key=lambda x: -(abs(x[0] - x[1])))
    tot = 0
    r = l = len(costs) // 2
    for c in costs:
        if (c[0] < c[1] and l) or (not r):
            tot += c[0]
            l -= 1
        else:
            tot += c[1]
            r -= 1
    return tot


if __name__ == "__main__":
    lst = [[518, 518], [71, 971], [121, 862], [967, 607], [138, 754], [513, 337], [499, 873], [337, 387], [647, 917],
           [76, 417]]
    print(two_city_sched_cost(lst))
