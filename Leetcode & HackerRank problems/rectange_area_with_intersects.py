class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        intersect_area = self.find_intersect(A,B,C,D,E,F,G,H)
        area_1 = self.find_area(A,B,C,D)
        area_2 = self.find_area(E,F,G,H)
        return area_1 + area_2 - intersect_area
    
    def find_area(self, c_1A, c_1B, c_2A, c_2B):
        width = abs(c_1A-c_2A)
        height = abs(c_1B-c_2B)
        return height*width
    
    def find_intersect(self, A, B, C, D, E, F, G, H):
        upper_height = min(H, D)
        lower_height = max(F, B)
        left_width = max(A,E)
        right_width = min(C,G)
        if left_width >= right_width: return 0
        if upper_height <= lower_height: return 0
        return (upper_height-lower_height)*(right_width-left_width)
