class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_value_map = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1,
        }
        result = 0
        for k, v in symbol_value_map.items():
            while s.startswith(k):
                result += v
                s = s[len(k):]
        return result
