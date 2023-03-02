class Solution:
    def containsDuplicateDict(self, nums):
        index = {}
        for element in nums:
            if element not in index:
                index[element] = 1
            else:
                index[element] += 1
        print(index)
        if max(index.values()) > 1:
            return True
        return False
        
    def containsDuplicateOrder(self, nums):
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
    def containsDuplicateSet(self, nums):
        temp = list(set(nums))
        print(temp)
        return len(temp) < len(nums)

    def containsDuplicateHashset(self, nums):
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False

test_data = [2,14,18,22,22]
solution = Solution()
print(solution.containsDuplicateHashset(test_data))