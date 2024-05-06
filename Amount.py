# Given a collection of amount values (A) and a target sum (S), find all unique combinations in
# A where the amount values sum up to S. Return these combinations in the form of a list.
# Each amount value may be used only the number of times it occurs in list A. The solution set
# should not contain duplicate combinations. Amounts will be positive numbers.
# Return an empty list if no possible solution exists.

def amount(A, S):
    """
    Given a collection of amount values (A) and a target sum (S), find all unique combinations in
    A where the amount values sum up to S.
    :param A: An array of amount values
    :param S: int, a target sum
    :return: An array of combinations such that the sum of each combination equals S
    """
    # sort the nums into ascending order using Timsort O(nlogn)
    A.sort()
    result = []
    amount_helper(A, S, 0, [], result)
    return result

def amount_helper(A, S, pointer, combo, result):
    """
    A helper function for amount
    :param A: An array of amount values
    :param S: int, a target sum
    :param pointer: int, the first number in A to be examined
    :param combo: An array of the current selection of numbers to meet the target sum
    :param result: An array holding combinations that sum to S
    :return: None
    """
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
        # add number to combo, lessen the remaining sum to be found, increment pointer to look at new number
        amount_helper(A, S - A[i], i + 1, combo + [A[i]], result)

if __name__ == "__main__":
    print(amount([11, 1, 3, 2, 6, 1, 5], 8))


