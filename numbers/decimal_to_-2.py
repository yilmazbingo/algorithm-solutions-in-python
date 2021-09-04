class Solution:
    def baseNeg2(self, N: int) -> str:
        res = []
        while N != 0:
            r = N % (-2)
            if r == -1:
                r = 1
            N = (N - r) // (-2)
            res.append(str(r))

        return ''.join(res[::-1]) or "0"