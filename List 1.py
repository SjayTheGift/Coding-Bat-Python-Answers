#List-1 > make_pi 
def make_pi():
  return [3,1,4]
  
#List-1 > common_end 
def common_end(a, b):
  return a[0] == b[0] or a[-1] == b[-1]
  
#List-1 > sum3 
def sum3(nums):
  return sum(nums)
  
#List-1 > rotate_left3
def rotate_left3(nums):
  return [nums[1],nums[-1],nums[0]]
  
#List-1 > reverse3 
 def reverse3(nums):
  return nums[::-1]

#List-1 > max_end3 
def max_end3(nums):
  if nums[0] > nums[-1]:
    return [nums[0]]*3
  else:
    return [nums[-1]]*3
 
#List-1 > sum2 
def sum2(nums):
  return sum(nums[0:2])

#List-1 > middle_way 
def middle_way(a, b):
  return [j for j in a[1:-1]] + [i for i in b[1:-1]]
 
#List-1 > make_ends 
 def make_ends(nums):
  return [nums[0],nums[-1]]
  
#List-1 > has23 
  def has23(nums):
    return  nums[0] == 2 or nums[1] == 2 or  nums[0]== 3 or nums[1] == 3
  OR 
    return 2 in nums or 3 in nums
  
#List-1 > same_first_last 
  def same_first_last(nums):
    return len(nums) >= 1 and nums[0] == nums[-1]
  
#List-1 > first_last6 
 def first_last6(nums):
  return len(nums) >= 1 and nums[0] == 6 or nums[-1] == 6