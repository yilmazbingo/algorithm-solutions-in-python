class Solution:
    def numberToWords(self, num: int) -> str:
        under_twenty = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                        "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        # if it is under 20 it will be handled by under_twenty
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        chunks = ["Thousand", "Million", "Billion"]
        def dfs(num):
            if num==0:
                return []
            if num<20:
                return [under_twenty[num]]
            if num<100:
                return [tens[num//10]]+dfs(num%10)
            if num<1000:
                quotient,remainder=num//100,num%100
                return [under_twenty[quotient],"Hundred"] + dfs(remainder)
            for power,chunk in enumerate(chunks,1):
                if num < 1000 ** (power + 1):
                    quotient, remainder = num // 1000 ** power, num % 1000 ** power
                    return dfs(quotient) + [chunk] + dfs(remainder)
        return " ".join(dfs(num)) or 'Zero'

# T:O(1) and S:O(1)