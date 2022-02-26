'''
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.
'''

class TwoSum:
    def __init__(self):
        self.store = []
    def add(self, number):
        self.store.append(number)

    def find(self, value):
        if (len(self.store)) < 2:
            return False
        n = len(self.store) - 1
        s = self.store
        s.sort()

        left, right = 0, n
        while left < right:
            if value == (s[left] + s[right]):
                return True
            elif value < (s[left] + s[right]):
                right -= 1
            else:
                left += 1
        return False