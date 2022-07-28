from List_Node import ListNode
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        store = set()
        while head and head.next:
            if head in store:
                return True
            store.add(head)
            head = head.next
        return False
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

    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        visit = set()
        visit.add(head)
        while head:
            if head.next in visit:
                return True
            head = head.next
            visit.add(head)
        return False


