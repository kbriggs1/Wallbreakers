class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        
        def loop(n):
            if n == 1:
                return [0, 1]

            prev = loop(n - 1)
            return prev + [(1 << n - 1) + i for i in reversed(prev)]
   
        return loop(n)
