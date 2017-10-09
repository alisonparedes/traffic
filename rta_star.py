import numpy
import itertools
import copy
import heapq
import logging
import time


def h(current_state, visited):
    goal = numpy.asarray([0] * (len(current_state) - 1))
    hashable_q = tuple(current_state)
    h = visited.get(hashable_q)
    logging.debug("checking visited ... {0}".format(h))
    if not h:
        h = numpy.linalg.norm(current_state[1:] - goal)
    logging.debug("h is ... {0}".format(h))
    return h


def min_local_f(current_state, domain, visited, intervals):
    phases = []
    with_intervals = itertools.product(domain, intervals)
    for phase in with_intervals:
        in_queue = phase[0][0]
        out_queue = phase[0][1]
        rate = phase[0][2]
        interval = phase[1]
        phases.append((in_queue, out_queue, rate, interval))
    min_f = []
    for phase in phases:
        logging.debug("considering phase ... {0}".format(phase))
        successor_state = copy.copy(current_state)
        in_queue = phase[0]
        out_queue = phase[1]
        rate = phase[2]
        interval = phase[3]
        change = min(interval * rate, current_state[in_queue])
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


def simulate(current_state, assignments, interval):
    successor_state = copy.copy(current_state)
    for phase in assignments:
        in_queue = phase[1][0]
        out_queue = phase[1][1]
        rate = phase[1][2]
        change = min(current_state[in_queue], interval * rate)
        successor_state[in_queue] -= change
        successor_state[out_queue] += change
    return successor_state


def visited_h(alternative_assignments, current_state, successor_state, visited):
    min_h = []
    for phases in alternative_assignments:
        alternative_state = simulate(current_state, phases, interval)
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
    intervals = list(set(current_state))
    max_interval = 0
    for domain in domains:
        best, next_best = min_local_f(current_state, domain, visited, intervals)
        interval = best[1][3]
        if interval > max_interval:
            max_interval = interval
        assignment.append(best)
        #alternatives.append((best, next_best))
    successor_state = simulate(current_state, assignment, max_interval)
    logging.debug("best assignment is ... {0}".format(assignment))
    logging.debug("successor state will be ... {0}".format(successor_state))
    #alternative_assignments = []
    #for omg in itertools.product(*alternatives):
    #    alternative_assignments.append(omg)
    cost = 1
    next_best_h = cost + best[0]#visited_h(alternative_assignments, current_state, successor_state, visited)
    return assignment, next_best_h, max_interval

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
        start_time = time.clock()
        best, new_h, interval = min_f(domain, current_state, visited)
        print(time.clock()-start_time)
        visited[tuple(current_state)] = new_h
        logging.debug("seting h for current state ... {0}".format(current_state))
        logging.debug("set h to ... {0}".format(new_h))
        current_state = simulate(current_state, best, interval)
    print(current_state)


def quick_domain(in_queues, out_queues, exceptions):
    rates = (1, )
    phases = []
    for phase in itertools.product(in_queues, out_queues, rates):
        in_queue = phase[0]
        out_queue = phase[1]
        rate = phase[2]
        if exceptions.get((in_queue, out_queue)):
            rate = 0
        phases.append((in_queue, out_queue, rate))
    return phases

if __name__ == "__main__":

    '''
    current_state = numpy.arange(28)
    goal = numpy.asarray([0] * (len(current_state) - 1))
    domains = []
    domains.append(quick_domain([1, 2, 3, 4], [0, 5, 25], {(3, 5): True, (4, 25): True}))
    domains.append(quick_domain([5, 6, 7, 8], [0, 3, 9, 21], {(6, 0): True, (5, 3): True, (7, 9): True, (8, 21): True}))
    domains.append(quick_domain([9, 10, 11, 12],  [0, 7, 13], {(9, 7): True, (12, 13): True}))
    domains.append(quick_domain([13, 14, 15], [0, 12, 17], {(13, 12): True, (14, 0): True, (15, 17): True}))
    domains.append(quick_domain([16, 17, 18, 19], [0, 15, 22], {(17, 15): True, (16, 22): True}))
    domains.append(quick_domain([20, 21, 22, 23], [0, 8, 16, 26], {(21, 8): True, (22, 16): True, (23, 0): True, (20, 26): True}))
    domains.append(quick_domain([24, 25, 26, 27], [0, 20, 4], {(25, 4): True, (26, 20): True}))
    '''
    import domain
    queues, intersections = domain.connect(4, 4)
    current_state = numpy.arange(queues) % 10
    goal = numpy.asarray([0] * (len(current_state) - 1))
    domains = []
    for intersection in intersections:
        in_queues = intersection[0]
        out_queues = intersection[1]
        exceptions = intersection[2]
        domains.append(quick_domain(in_queues, out_queues, exceptions))
    rta_star(current_state, domains)
