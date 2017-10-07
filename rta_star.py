import numpy
import itertools
import copy
import heapq


def f(new_q=[], visited=dict(), goal=[]):
    hashable_q = tuple(new_q)
    h = visited.get(hashable_q)
    if not h:
        h = numpy.linalg.norm(new_q - goal)
    f = h
    return f


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


def execute(current_state, phases):
    next_state = copy.copy(current_state)
    for phase in phases:
        simulate(next_state, current_state, phase)
    return next_state


def simulate(successor_state, q, best):
    in_queue = best[1][0]
    out_queue = best[1][1]
    change = q[in_queue]
    successor_state[in_queue] -= change
    successor_state[out_queue] += change


def visited_h(alternative_assignments, q, goal, successor_state):
    next_best_h_min = []
    for assignment in alternative_assignments:
        next_best = copy.copy(q)
        for intersection in assignment:
            simulate(next_best, q, intersection)
        next_best_h = numpy.linalg.norm(next_best - goal)
        if numpy.linalg.norm(next_best - successor_state) > 0:
            heapq.heappush(next_best_h_min, next_best_h + 1)
    return heapq.heappop(next_best_h_min)


def min_f(domain, q):
    successor_state = copy.copy(q)
    alternatives = []
    for intersection in domain:
        best, next_best = min_phase(q, intersection)
        simulate(successor_state, q, best)
        alternatives.append((best, next_best))
    alternative_assignments = itertools.product(*alternatives)
    return best, alternative_assignments, successor_state

if __name__ == "__main__":



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

    for _ in range(10):
        best, alternatives, successor_state = min_f(domain, q)
        new_h = visited_h(alternatives, q, goal, successor_state)
        cost = 1
        visited[tuple(q)] = new_h + cost
        q = execute(q, best)

