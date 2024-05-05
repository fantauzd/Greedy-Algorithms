# You are given a list of activities {a1, a2,...an} with their start times [s1, s2,...sn]
# and end times [e1,e2,....en].
#
# Example: activities: {Play Golf, Paint, Cook, Sleep, Jog, Write Code, Eat}
#
# start times: [1, 3, 1, 3, 4, 6, 8]
#
# end times: [3, 4, 4, 6, 6, 9, 9]
#
# You are equally interested in all of them. Your goal is to maximize
# the number of activities that you can perform. You cannot choose overlapping activities,
# for example, 'cook' and 'paint'. You can choose activities that immediately start
# after the previous one ends, for example, 'Play Golf' and 'Paint'.

def activity_selection(activities, starts, ends):
    """
    Solves activity selection problem where end times are in sorted order (ASC)
    and activities and times correspond by index.
    :param activities: a list of activities
    :param starts: a list of start times
    :param ends: a list of end times
    :return: a list with the maximum salection of activites
    """
    result = []
    blocked_time = 0
    for i in range(len(activities)):
