# You are a pet store owner and you own few dogs. Each dog has a specific hunger level given
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

def feedDog(hunger_level, biscuit_size):
    """
    Solves the feed dog problem and returns the number of dogs that are satisified.
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
    # for each biscuit we have
    for biscuit in range(len(biscuit_size)):
        # start with the largest biscuit left
        j = len(biscuit_size) - 1
        # find the smallest biscuit that will satisfy the dog or use the smallest biscuit
        while j > 0 and hunger_level[dog] != biscuit_size[j]:
            j -= 1
        # feed the biscuit to the dog
        hunger_level[dog] -= biscuit_size[j]
        biscuit_size.remove(biscuit_size[j])
        # if the dog was satisfied move to next dog
        if hunger_level[dog] <= 0:
            dog += 1
            result += 1

    return result

if __name__ == "__main__":
    print(feedDog([1,2,3], [1,1]))