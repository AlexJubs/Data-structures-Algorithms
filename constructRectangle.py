class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        if area == 1 or area == 0: return [area,area]
        if area**0.5%1 == 0: return [int(area**0.5),int(area**0.5)]
        L = int(area**0.5)+1
        while L > 0:
            if area/L%1 == 0:
                return [max(int(area/L),L),min(int(area/L),L)]
            L = L-1
        return [area,1]
