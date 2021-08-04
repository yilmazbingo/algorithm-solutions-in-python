# if we did brute force solution T:O(K * N)
# if I do merge of 2 and merge each pair T:O(LogK * N)

from typing import List
from List_Node import ListNode

class Solution:
    def merge_k_list(self,lists:List[ListNode])->ListNode:
        if not lists or len(lists)==0:
            return None
        while len(lists)>1:
            merged_lists=[]
            for i in range(0,len(lists),2):
                l1=lists[i]
                # if we had odd number of list we migh go out of bounds
                l2=lists[i+1] if (i+1)<len(lists) else None
                merged_lists.append(self.merge_two(l1,l2))
            lists=merged_lists
        return lists[0]

    def merge_two(self,l1:ListNode,l2:ListNode):
        dummy=ListNode()
        tail=dummy

        while l1 and l2:
            if l1.val<l2.val:
                tail.next=l1
                l1=l1.next
            else:
                tail.next=l2
                l2=l2.next
            tail=tail.next

        if l1:
            tail.next=l1
        if l2:
            tail.next=l2
        return dummy.next