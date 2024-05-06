 # Problem: Given a sorted array of positive integers nums[] and a sum of value k,
 # find all unique combinations of integers from the nums[] array whose sum is equal to k.
 # Any integer in the array can be chosen an unlimited number of times.

from copy import deepcopy
def combination_sum(nums, target):
    result = []
    # sort the nums into ascending order
    nums.sort()                     # Uses Timsort in O(n log n)
    combination_sum_helper(nums, target, result, pointer=0, combination=[])
    return result

def combination_sum_helper(nums, target, result, pointer, combination):
    # store valid solutions
    if target == 0:
        # avoid adding repeating solutions when nums has duplicate of a number
        if combination not in result:    # O(k) where k is number of combinations in result
            result.append(deepcopy(combination))
        return
    # if we went over target, backtrack
    if target < 0:
        return
    # attempt to use each number in a combination, starting with smallest
    for i in range(pointer, len(nums)):
        # try each value in the combination
        combination.append(nums[i])
        # when a value is used remove it from nums
        cur_val = nums[i]
        copy_nums = deepcopy(nums)
        copy_nums.remove(cur_val)     # O(n) time
        combination_sum_helper(copy_nums, target - cur_val, result, i, combination)
        # backtrack
        combination.pop()

def amount(A, S):
    # sort the nums into ascending order using Timsort O(nlogn)
    A.sort()
    result = []
    amount_helper(A, S, 0, [], result)
    return result

def amount_helper(A, S, pointer, combo, result):
# if the combination is too large, then we return and remove the last number added to the combination
  if S < 0:
    return
  # if the combination is a solution, add to results
  if S == 0:
    result.append(combo)
    return
  # start from the first number and add it to the combination
  for i in range(pointer, len(A)):
    # skip duplicates to avoid repeated answers when A has more than one of some number
    if A[i] == A[i-1]:
        # we have already used first duplicate in combo
        if i > pointer:
            continue

    amount_helper(A, S - A[i], i + 1, combo + [A[i]], result)

if __name__ == "__main__":
    print(combination_sum([11, 1, 3, 2, 6, 1, 5], 8))
    print(amount([11, 1, 3, 2, 6, 1, 5], 8))

# Given a collection of amount values (A) and a target sum (S), find all unique combinations in
# A where the amount values sum up to S. Return these combinations in the form of a list.
# Each amount value may be used only the number of times it occurs in list A. The solution set
# should not contain duplicate combinations. Amounts will be positive numbers.
# Return an empty list if no possible solution exists.

