def twoSum(nums, target):
    n = len(nums)
    for i in range(n):
        for j  in range(i+1, n):
            if nums[i] + nums[j] == target:
                return True
    return False
#완전접근방법 O(n^2)

#정렬 => nlogn > 완전접근O(n^2) 시간복잡도 유리

def soltTwoSome(nums, target):
    nums.sort()
    l ,r = 0, len(nums)-1

    while l<r:
        if nums[l] + nums[r] > target:
            r = r-1
        elif nums[l] + nums[r] < target:
            l = l+1
        elif nums[l] + nums[r] == target:
            return True
    return False





print(twoSum(nums=[4,1,9,7,5,3,16],target=14))
print(soltTwoSome(nums=[4,1,9,7,5,3,16],target=14))         