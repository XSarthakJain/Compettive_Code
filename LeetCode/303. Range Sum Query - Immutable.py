#303. Range Sum Query - Immutable
class NumArray:

    def __init__(self, nums: List[int]):
        self.numArray = nums
        

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.numArray[left:right+1])
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
