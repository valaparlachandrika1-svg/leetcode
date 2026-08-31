# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        
        prev = head
        curr = head.next
        
        index = 1
        
        first = -1
        last = -1
        minDistance = float('inf')
        
        while curr.next:
            # Check if curr is a critical point
            if ((curr.val > prev.val and curr.val > curr.next.val) or
                (curr.val < prev.val and curr.val < curr.next.val)):
                
                if first == -1:
                    # First critical point
                    first = index
                else:
                    # Distance from previous critical point
                    distance = index - last
                    minDistance = min(minDistance, distance)
                
                # Update last critical point
                last = index
            
            prev = curr
            curr = curr.next
            index += 1
        
        # Fewer than 2 critical points
        if first == -1 or first == last:
            return [-1, -1]
        
        maxDistance = last - first
        
        return [minDistance, maxDistance]