class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        s = sorted(heights)
        c = 0
        for i in range(len(heights)):
            if heights[i] != s[i]:
                c += 1
        return c
