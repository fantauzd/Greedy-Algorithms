# Dominic Fantauzzo

# You are a pet store owner, and you own few dogs. Each dog has a specific hunger level given
# by array hunger_level [1..n] (ith dog has hunger level of hunger_level [i]). You have couple of
# dog biscuits of size given by biscuit_size [1…m]. Your goal to satisfy maximum number of
# hungry dogs. You need to find the number of dogs we can satisfy.
# If a dog has hunger hunger_level[i], it can be satisfied only by taking a biscuit of size
# biscuit_size [j] >= hunger_level [i] (i.e biscuit size should be greater than or equal to hunger
# level to satisfy a dog.)
# If no dog can be satisfied return 0.
# Conditions:
# You cannot give same biscuit to two dogs.
# Each dog can get only one biscuit.

def feedDogMultipleBiscuits(hunger_level, biscuit_size):
    """
    Solves the feed dog problem  where one dog can receive many biscuits.
    :param hunger_level: an array where each index represents the hunger level of a dog
    :param biscuit_size: an array where each index represents the size of a biscuit
    :return: int, number of dogs that are satisfied
    """
    # sort the input arrays in ascending order
    hunger_level.sort()        # timsort in O(nlogn)
    biscuit_size.sort()
    # initialize variables to track fed dogs and current dog
    result = 0
    dog = 0
    # we repeat until we run our of biscuits or dogs
    for exchange in range(min(len(biscuit_size), len(hunger_level))):
        # start with the smallest biscuit left
        j = 0
        # find the smallest biscuit that will satisfy the dog or use the largest biscuit
        while j < (len(biscuit_size)-1) and hunger_level[dog] > biscuit_size[j]:
            j += 1
        # feed the biscuit to the dog
        hunger_level[dog] -= biscuit_size[j]
        biscuit_size.remove(biscuit_size[j])    #O(n) time complexity
        # if the dog was satisfied then count it
        if hunger_level[dog] <= 0:
            result += 1
            dog += 1

    return result

def feedDog(hunger_level, biscuit_size):
    """
    Solves the feed dog problem and returns the number of dogs that are satisified.
    :param hunger_level: an array where each index represents the hunger level of a dog
    :param biscuit_size: an array where each index represents the size of a biscuit
    :return: int, number of dogs that are satisfied
    """
    # sort the input arrays in ascending order
    hunger_level.sort()
    biscuit_size.sort()
    # use pointers for current dog and biscuit
    dog = 0
    biscuit = 0
    result = 0
    # starting with the smallest dog and biscuit, continue satisfying dogs until we run out of dogs or biscuits
    while dog < len(hunger_level) and biscuit < len(biscuit_size):
        # if a biscuit will satisfy a dog, use it
        if hunger_level[dog] <= biscuit_size[biscuit]:
            result += 1
            dog += 1
            biscuit += 1
        # otherwise look at larger biscuit
        else:
            biscuit += 1

    return result

if __name__ == "__main__":
    print(feedDog([1, 2, 3, 4, 5], [1,2, 4, 3, 1, 4]))