def one_way():
    '''q1 contains 1 vehicle, q2 contains 2 vehciles'''
    q = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    '''move vehicles in q1 to q2 at a rate of 0.5 vehicles per second'''
    t = 2
    i_1 = ((1, 2, 0.5), (3, 4, 0.5))
    i_2 = ((5, 6, 0.5), (7, 8, 0.5))
    intersections = (i_1, i_2)
    import copy
    import math
    import numpy
    goal = [0] * 20
    for _ in range(0, 100):
        new_q = copy.copy(q)
        for phase in intersections:
            for flow in phase:
                rate = flow[2]
                from_q = flow[0]
                to_q = flow[1]
                change = math.floor(rate * t)
                new_q[from_q] = q[from_q] - change
                new_q[to_q] = q[to_q] + change
        h = numpy.linalg.norm(q - goal)


if __name__ == "__main__":


    '''A different approach'''
    in_queues = [0, 1, 2, 3]
    out_queues = [4, 5, 6, 7]
    import itertools
    import copy
    import numpy
    phases = itertools.product(in_queues, out_queues)
    current_state = numpy.asarray([1, 2, 3, 4, 5, 6, 7, 8])
    goal = numpy.asarray([0] * 8)
    import heapq
    min_h = []
    for phase in phases:
        successor_state = copy.copy(current_state)
        in_queue = phase[0]
        out_queue = phase[1]
        change = current_state[in_queue]
        successor_state[in_queue] -= change
        successor_state[out_queue] += change
        h = numpy.linalg.norm(successor_state - goal)
        heapq.heappush(min_h, (h, phase))
    return heapq.heappop(min_h)




