import random


class RandomizedSet:
    """
    RandomizedSet is a data structure built with O(1) time to insert, remove, and pick a random item from it.
    """

    def __init__(self):
        """
        Initialize of data structure.
        """
        self.myDict = {}
        self.myList = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.myDict:
            return False
        self.myDict[val] = len(self.myList)
        self.myList.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.myDict:
            return False
        val_ind = self.myDict[val]
        # update the index of the last value in the dictionary to be equal to the index of the deleted element
        self.myDict[self.myList[-1]] = val_ind
        self.myList[-1], self.myList[val_ind] = self.myList[val_ind], self.myList[-1]
        self.myList.pop()
        del self.myDict[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.myList)


mySet = RandomizedSet()
print(mySet.insert(0))
print(mySet.insert(1))
print(mySet.remove(0))
print(mySet.insert(2))
print(mySet.remove(1))
print(mySet.getRandom())
print(mySet.insert(2))
print(mySet.remove(1))

