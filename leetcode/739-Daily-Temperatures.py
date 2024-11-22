class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):
            temp = temperatures[i]

            while stack and temperatures[stack[-1]] <= temp: stack.pop()

            answer[i] = (stack[-1] if stack else i) - i

            stack.append(i)

        return answer