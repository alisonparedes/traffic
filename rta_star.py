import numpy
import itertools

def f(new_q=[], visited=dict(), goal=[]):
    hashable_q = tuple(new_q)
    h = visited.get(hashable_q)
    if not h:
        h = numpy.linalg.norm(new_q - goal)
    f = h
    return f

def transition(phase_assignments=[(1.0, (0, 4)), (1.0, (5, 2))], current_state=numpy.asarray([1, 2, 3, 4, 5, 6, 7, 8])):
    return 1


def min_phase(current_state=numpy.asarray([1, 2, 3, 4, 5, 6, 7, 8]), phases=itertools.product([0, 1, 2, 3], [4, 5, 6, 7])):
    goal = numpy.asarray([0] * len(current_state))
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
    return heapq.heappop(min_h), heapq.heappop(min_h)


if __name__ == "__main__":

    import copy
    import math
    import heapq

    visited = dict()
    q = numpy.asarray([0] * 8)
    q[0] = 10
    q[1] = 10
    q[2] = 10
    goal = numpy.asarray([0] * len(q))

    '''A problem instance to play with during development'''
    domain = []
    in_queues_1 = [0, 1, 2, 3]
    out_queues_1 = [4, 5, 6, 7]
    phases_1 = itertools.product(in_queues_1, out_queues_1)
    domain.append(phases_1)

    # in_queues_2 = [5, 8, 9, 10]
    # out_queues_2 = [11, 12, 13, 2]
    # phases_2 = itertools.product(in_queues_2, out_queues_2)
    # domain.append(phases_2)

    # in_queues_3 = [12, 14, 15, 16]
    # out_queues_3 = [8, 17, 18, 19]
    # phases_3 = itertools.product(in_queues_1, out_queues_3)
    # domain.append(phases_3)

    # in_queues_4 = [20, 19, 22, 21]
    # out_queues_4 = [15, 24, 25, 13]
    # phases_4 = itertools.product(in_queues_2, out_queues_4)
    # domain.append(phases_4)

    # in_queues_5 = [26, 13, 28, 27]
    # out_queues_5 = [9, 20, 30, 6]
    # phases_5 = itertools.product(in_queues_1, out_queues_5)
    # domain.append(phases_5)

    # in_queues_6 = [31, 6, 32, 33]
    # out_queues_6 = [2, 26, 34, 35]
    # phases_6 = itertools.product(in_queues_2, out_queues_6)
    # domain.append(phases_6)

    # in_queues_7 = [36, 34, 38, 37]
    # out_queues_7 = [41, 32, 39, 40]
    # phases_7 = itertools.product(in_queues_2, out_queues_7)
    # domain.append(phases_7)
    ''''''

    import time
    start_time = time.time()


    successor_state = copy.copy(q)
    alternatives = []
    for intersection in domain:
        best, next_best = min_phase(q, intersection)
        in_queue = best[1][0]
        out_queue = best[1][1]
        change = q[in_queue]
        successor_state[in_queue] -= change
        successor_state[out_queue] += change
        alternatives.append((best, next_best))

    h = numpy.linalg.norm(successor_state - goal)
    print(h)


    next_best_h_min = []

    alternative_assignments = itertools.product(*alternatives)
    for assignment in alternative_assignments:
        next_best = copy.copy(q)

        for intersection in assignment:
            in_queue = intersection[1][0]
            out_queue = intersection[1][1]
            change = q[in_queue]
            next_best[in_queue] -= change
            next_best[out_queue] += change

        next_best_h = numpy.linalg.norm(next_best - goal)

        if numpy.linalg.norm(next_best - successor_state) > 0:
            heapq.heappush(next_best_h_min, next_best_h + 1)
    print(heapq.heappop(next_best_h_min))

    print(time.time() - start_time)

    current_state = q
    arg_min = None
    min_f = float("inf")
    next_min_f = min_f




    # f = f(new_q, visited, goal)
    #
    # if f < min_f:
    #     arg_min = assignment
    #     next_min_f = min_f
    #     min_f = f
    #
    # visited[tuple(current_state)] =  next_min_f
    # print arg_min