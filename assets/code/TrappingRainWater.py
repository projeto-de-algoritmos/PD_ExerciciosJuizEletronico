class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        size = len(height)
        left_max = [0] * size
        right_max = [0] * size

        left_max[0] = height[0]
        for i in range(1, size):
            left_max[i] = max(left_max[i-1], height[i])

        right_max[size-1] = height[size-1]
        for i in range(size-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])

        water = 0
        for i in range(size):
            water += min(left_max[i], right_max[i]) - height[i]

        return water