"""
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k),
 where h is the height of the person and k is the number of people in front of this person who have a height greater
 than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

Example
Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
"""


# def reconstructQueue(people):
#     """
#     people reconstructs the given queue n people.
#     :param people: list of list, where elements are pairs of integers [h, k], where h is the height of the person and k
#      is the number of people in front of this person who have a height greater than or equal to h
#     :return: lists of lists represents the constructed queue.
#     """
#     people.sort(key=lambda x: (x[0], -x[1]))
#     n = len(people)
#     cons_people = [0] * n
#     for person in people:
#         people_before = person[1]
#         i = 0
#         while people_before > 0 or cons_people[i]:
#             if not cons_people[i]:
#                 people_before -= 1
#             i += 1
#             if i == n - 1:
#                 break
#         cons_people[i] = person
#     return cons_people


# shorter solution
def reconstructQueue(people):
    """
    people reconstructs the given queue n people.
    :param people: list of list, where elements are pairs of integers [h, k], where h is the height of the person and k
     is the number of people in front of this person who have a height greater than or equal to h
    :return: lists of lists represents the constructed queue.
    """
    people.sort(key=lambda x: (-x[0], x[1]))
    cons_people = []
    for person in people:
        cons_people.insert(person[1], person)
    return cons_people


# Note: this part is for testing only and it is not part of the leetcode solution
lst = [[9, 0], [7, 0], [1, 9], [3, 0], [2, 7], [5, 3], [6, 0], [3, 4], [6, 2], [5, 2]]
print(reconstructQueue(lst))
