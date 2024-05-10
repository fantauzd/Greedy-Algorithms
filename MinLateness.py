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

from operator import itemgetter

def minLateness(assignments):
    """
    Solve the lateness problem and find the minimum acheivable late days for the given assignments.
    Assignment = [("A" , 2 , 2 ),( "B" , 3 , 4 ), ( "D" , 5 , 7 ), ( "C" , 1 , 6 )]
    where the three values in each set are
    :param Name:  assignment name
    :param TimeTaken: the days needed to complete corresponding assignments
    :param Deadline: the deadline day for corresponding assignments
    :return:
    """
    # sort all three arrays on deadline ASC
    sorted_assignemnts = sorted([assignments], key = itemgetter(2))

    start_time = 0
    max_late = 0
    schedule = []

    for assignment in assignments:
        finish_time = start_time + assignment[1]
        if finish_time > assignment[2]:
            max_late = max(max_late, finish_time - assignment[2])
        start_time = finish_time
        schedule.append(assignment[0])

    return max_late, schedule

if __name__ == "__main__":
    assinnments = [("A", 2, 2), ("B", 3, 4), ("C", 1, 6), ("D", 5, 7)]  # [(S.no, timetaken, deadline)]
    print(min_Lateness(assinnments))
