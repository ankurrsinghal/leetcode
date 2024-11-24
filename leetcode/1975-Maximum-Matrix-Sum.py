class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        max_sum = 0
        negative_elements_count = 0
        min_element = math.inf
        was_there_a_zero = False

        for row in matrix:
            for col in row:
                max_sum += abs(col)
                if col < 0:
                    negative_elements_count += 1
                if col == 0:
                    was_there_a_zero = True
                min_element = min(min_element, abs(col))

        if negative_elements_count % 2 != 0 and not was_there_a_zero:
            max_sum -= 2 * min_element

        return max_sum