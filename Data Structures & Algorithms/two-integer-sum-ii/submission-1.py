class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            two_sum = numbers[i] + numbers[j]
            if two_sum == target:
                return [i+1, j+1]
            if two_sum < target:
                i += 1
            else:
                j -= 1
        return [-1, -1]
        