from collections import deque
from typing import List

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue=deque([start])
        visited=set()
        while queue:
            for i in range(len(queue)):
                temp=queue.popleft()
                visited.add(temp)
                if arr[temp]==0:
                    return True
                if temp+arr[temp] in range(len(arr)) and temp+arr[temp] not in visited:
                    queue.append(temp+arr[temp])
                if temp-arr[temp] in range(len(arr)) and temp-arr[temp] not in visited:
                    queue.append(temp-arr[temp])
        return False