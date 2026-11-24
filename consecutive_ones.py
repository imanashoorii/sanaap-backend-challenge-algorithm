class Solution:
    def hasFourConsecutiveOnes(self, s: str) -> bool:
        if len(s) < 4:
            return False

        circular_string = s + s

        return "1111" in circular_string


s = "1010111"
solution = Solution()

print(solution.hasFourConsecutiveOnes(s))
