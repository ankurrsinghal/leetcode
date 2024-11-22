class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(prices)

        for i in range(len(prices) - 1, -1, -1):
            price = prices[i]

            while stack and stack[-1] > price:
                stack.pop()
            
            answer[i] = price - (stack[-1] if stack else 0)

            stack.append(price)

        return answer