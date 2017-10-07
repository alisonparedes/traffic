import numpy
import itertools
import copy
import heapq
import logging


def h(current_state, visited):
    goal = numpy.asarray([0] * (len(current_state) - 1))
    hashable_q = tuple(current_state)
    h = visited.get(hashable_q)
    logging.debug("checking visited ... {0}".format(h))
    if not h:
        h = numpy.linalg.norm(current_state[1:] - goal)
    logging.debug("h is ... {0}".format(h))
    return h


def min_local_f(current_state, domain, visited):
    min_f = []

    for phase in domain:
        logging.debug("considering phase ... {0}".format(phase))
        successor_state = copy.copy(current_state)
        in_queue = phase[0]
        out_queue = phase[1]
        change = current_state[in_queue]

        successor_state[in_queue] -= change
        successor_state[out_queue] += change
        logging.debug("successor would be ... {0}".format(successor_state))

        improved_h = h(successor_state, visited)
        cost = 1
        f = cost + improved_h
        heapq.heappush(min_f, (f, phase))

    best_phase = heapq.heappop(min_f)
    next_best_phase = heapq.heappop(min_f)
    logging.debug("best local phase is ... {0}".format(best_phase))

    return best_phase, next_best_phase



def execute(current_state, phases):
    logging.debug("EXECUTING ACTION ... {0}".format(phases))
    next_state = simulate(current_state, phases)
    logging.debug('CURRENT STATE SHOULD BE ... {0}'.format(next_state))
    return next_state


def simulate(current_state, assignments):
    """

    :param current_state:
    :param assignments: Is a list of phase changes for each intersection and for fun the f of the phase change when simulated locally
    :return:
    """

    successor_state = copy.copy(current_state)

    for phase in assignments:

        in_queue = phase[1][0]
        out_queue = phase[1][1]
        change = current_state[in_queue]

        successor_state[in_queue] -= change
        successor_state[out_queue] += change

    return successor_state


def visited_h(alternative_assignments, current_state, successor_state, visited):
    min_h = []
    for phases in alternative_assignments:
        alternative_state = simulate(current_state, phases)
        visited_h = h(alternative_state, visited)
        heapq.heappush(min_h, visited_h)
        logging.debug("considering alternative ... {0}".format(alternative_state))
        logging.debug("alternative h is ... {0}".format(visited_h))
    min_alternative = heapq.heappop(min_h)
    logging.debug("best alternative h is ... {0}".format(min_alternative))
    return min_alternative


def min_f(domains, current_state, visited):
    assignment = []
    alternatives = []
    for domain in domains:
        best, next_best = min_local_f(current_state, domain, visited)
        assignment.append(best)
        alternatives.append((best, next_best))
    successor_state = simulate(current_state, assignment)
    logging.debug("best assignment is ... {0}".format(assignment))
    logging.debug("successor state will be ... {0}".format(successor_state))
    alternative_assignments = []
    for omg in itertools.product(*alternatives):
        alternative_assignments.append(omg)
    cost = 1
    next_best_h = cost + visited_h(alternative_assignments, current_state, successor_state, visited)
    return assignment, next_best_h

def sum_queues(initial_state):
    queues_sum = 0
    for queue in initial_state[1:]:
        queues_sum += queue
    return queues_sum

def rta_star(initial_state, domain):
    visited = dict()
    goal = sum_queues(initial_state)
    current_state = initial_state
    while current_state[0] < goal:
        logging.debug("CURRENT STATE ... {0}".format(current_state))
        print(current_state)
        best, new_h = min_f(domain, current_state, visited)
        visited[tuple(current_state)] = new_h
        logging.debug("seting h for current state ... {0}".format(current_state))
        logging.debug("set h to ... {0}".format(new_h))
        current_state = execute(current_state, best)
    print(current_state)


if __name__ == "__main__":




    current_state = numpy.asarray([0] * 14)
    current_state[1] = 10
    current_state[2] = 10
    goal = numpy.asarray([0] * (len(current_state) - 1))

    '''A problem instance to play with during development'''
    domain = []
    in_queues_1 = [1, 2, 3, 4]
    out_queues_1 = [5, 0]
    phases_1 = []
    for phase in itertools.product(in_queues_1, out_queues_1):
        phases_1.append(phase)
    domain.append(phases_1)

    in_queues_2 = [5, 8, 9, 10]
    out_queues_2 = [0, 2]
    phases_2 = []
    for phase in itertools.product(in_queues_2, out_queues_2):
        phases_2.append(phase)
    domain.append(phases_2)

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
    time.clock()
    rta_star(current_state, domain)
    end_time = time.time()
    print(time.clock())