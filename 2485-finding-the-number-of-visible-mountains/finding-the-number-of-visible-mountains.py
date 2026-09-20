class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        n = len(peaks)
        #Google problems
        #sort by x-intercept of left mountain ascending first and x-intercept(x+y) of right mountain descending
        peaks.sort(key = lambda x: (x[0] - x[1], -(x[0] + x[1])))
        count = 0
        maxEnd = -inf
        #while interating peaks, count the number of visible peak which has larger x of the right mountain 
        for i, (x,y) in enumerate(peaks):
            if x + y > maxEnd:
                maxEnd = x + y
                #consider dup
                if i < n - 1 and peaks[i] == peaks[i+1]: continue
                count += 1
        return count 