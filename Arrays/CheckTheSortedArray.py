def check(nums):
        n = len(nums)
        count = 0
        for i in range(n-1):
            if nums[i] > nums[i + 1]:
                count += 1      # count will +1 that means first drop exp. 2>1

        # Check the last element with the first to complete the rotation check exp. 4>1
        if nums[-1] > nums[0]:
            count += 1

        if count <= 1:
            return True
        else:
            return False
#Example
nums = [3,4,5,1,2]
result = check(nums)
print(result)