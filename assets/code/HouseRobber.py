class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        previous_rob, current_rob = 0, 0

        for amount in nums:
            current_max = max(amount + previous_rob,  current_rob)
            previous_rob = current_rob
            current_rob = current_max
            
        return current_rob