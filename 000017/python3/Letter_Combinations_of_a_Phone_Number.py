from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_letter_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        result = list()
        stack = list()

        def dfs(i: int):
            if i == len(digits):
                result.append("".join(stack))
                return
            for l in digit_letter_map[digits[i]]:
                stack.append(l)
                dfs(i + 1)
                stack.pop()
        
        dfs(0)
        return result if digits else []
