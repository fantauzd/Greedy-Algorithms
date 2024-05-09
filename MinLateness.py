# Problem: You have a list of assignments [A, B, C, D]. You are provided with the time that it takes to solve these assignments, timetaken[t1, t2, t3, t4] and the deadline of each of the assignment, deadline[d1, d2, d3, d4].
#
# Where t1 corresponds to the time taken to complete Assignment A, which is due on d1.
#
# Your goal is to complete the assignments in such a way that you minimize the total lateness for the assignments. You need to return the minimum (Maximum lateness).
#
# Assume units for timetaken and deadline are days.
#
# For example:
#
# If assignments = [A, B, C, D]; timetaken=[1, 2, 3, 4] and deadline=[2,4,5,7].

def minLateness(Name, TimeTaken, Deadline):
    """
    Solve the lateness problem and find the minimum acheivable late days for the given assignments.
    :param Name: an array of assignments
    :param TimeTaken: an array of the days needed to complete corresponding assignments
    :param Deadline: an array of the deadline day for corresponding assignments
    :return:
    """
    # sort all three arrays on deadline ASC

    start_time = 0
    max_late = 0
    schedule = []
    finish_time = 0

    for i in range(len(Name)):
