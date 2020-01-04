class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        upper_height = min(rec1[3], rec2[3])
        lower_height = max(rec1[1], rec2[1])
        left_width = max(rec1[0], rec2[0])
        right_width = min(rec1[2],rec2[2])
        return right_width > left_width and upper_height > lower_height
