from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue=deque([])
        out=[]
        for i in range(len(nums)):

            if queue and i-queue[0]>=k:
                # we dont want the leftmost element which is beyond the window
                queue.popleft()

            while queue and nums[queue[-1]]<nums[i]:
                queue.pop()

            queue.append(i)

            out.append(nums[queue[0]])

        return out[k-1:]
'''
8 3
1 3 -1 -3 5 3 6 7
'''
