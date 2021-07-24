class Solution:
    def with_array(self,head:ListNode)->bool:
        # this makes S:O(N)
        nums=[]
        while head:
            nums.append(head.val)
            head=head.next
        l,r=0,len(nums)-1
        while l<=r:
            if nums[l]!=nums[r]:
                return False
            l+=1
            r-=1
        return True

    def optimum(self,head:ListNode)->bool:
        fast_pointer=head
        slow_pointer=head
        while fast_pointer and fast_pointer.next:
            # we are forwarding fast_pointer twice
            fast_pointer=fast_pointer.next.next
            # while slow reach middle, fast will reach to the end
            slow_pointer=slow_pointer.next
        # reverse the second half of the list
        prev=None
        while slow_pointer:
            temp=slow_pointer.next
            slow_pointer.next=prev
            # eventually prev will point to the last node
            prev=slow_pointer
            slow_pointer=temp
        # check if it is a palindrome
        left,right=head,prev
        while right:
            if left.val!=right.val:
                return False
            left=left.next
            right=right.next
        return True


