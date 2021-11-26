from List_Node import ListNode
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        seen=set()
        while head not in seen:
            if head.next==None:
                return False
            seen.add(head)
            head=head.next
        return True
    def hare_and_tortoise(self, head: ListNode) -> bool:
        if not head:
            return False
        hare = head
        tortoise = head
        while tortoise:
            hare = hare.next
            tortoise = tortoise.next
            # if not hare, states that i have a single node.
            # hare.next means that we have a tail value. So we do not have a cycle
            if (not hare) or (not hare.next):
                return False
            else:
                hare = hare.next
            if tortoise == hare:
                return True
        # so far we have found the detect the cycle
        # find the start of cycle
        p1,p2=head,tortoise
        while p1!=p2:
            p1=p1.next
            p2=p2.next
        return p1

