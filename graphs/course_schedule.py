# course numbers and prerequisites array will be given
#prereq:[[1,0],[2,3],[3,4]]

from typing import List
class Solution:
    def can_finish(self,num_courses:int,prerequisites:List[List[int]]):
        # map each course to prereq list
        pre_map={i:[] for i in range(num_courses) }
        for course,pre in prerequisites:
            pre_map[course].append(pre)
        visit_set=set()
        def dfs(crs):
            # first thing in recursive functions, always write the base case first
            if crs in visit_set:
                # that means I run into a loop
                return False
            if pre_map[crs]==[]:
                # this tells us that current course has no prerequisite
                return True
            # add the visited course
            visit_set.add(crs)
            # we are checking if each courses prerequisites can be finished
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
            # we finished visiting
            visit_set.remove(crs)
            # in case this course is visited again, since we already returned True, run base case again
            pre_map[crs]=[]
            return True
        # if graph was not fully connected, we had to run this for each course
        # 1-->2, 3-->4 so check if course 1,2,3,4 can individually be finished
        for crs in range(num_courses):
            if not dfs(crs):
                return False
        return True
s=Solution()
s.can_finish(5,[[0,1],[0,2],[1,3],[1,4],[3,4]])