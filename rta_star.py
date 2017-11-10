import numpy
import itertools
import copy
import heapq
import logging
import time
import os
import state
import transition
import random


def get_intersection(best):
    f = best[0]
    intersection, phase = best[1]
    return intersection


def get_phase(best):
    f = best[0]
    intersection, phase = best[1]
    return phase


def random_next(current_queues, current_intersections, interval=10):
    next_intersections = copy.copy(current_intersections)
    next_best_h = float("inf")
    actions = state.applicable_actions(current_intersections)
    for intersection, domain in actions.iteritems():
        apply = random.randint(0, len(domain)-1)
        current_phase = current_intersections[intersection][0]
        current_time = current_intersections[intersection][1]
        new_time = current_time + interval
        if domain[apply] != current_phase:
            new_time = interval
        next_intersections[intersection] = (domain[apply], new_time)
    return next_intersections, next_best_h


def breadth_first_d1(current_queues, current_intersections, interval=10):
    next_intersections = copy.copy(current_intersections)
    next_best_h = float("inf")
    best_h = float("inf")
    #print(next_best_h)
    actions = state.applicable_actions(current_intersections)
    next_states = itertools.product(*actions.itervalues())
    for try_state in next_states:
        try_intersections = copy.copy(current_intersections)
        for phase in try_state:
            intersection = phase[0:5]
            current_phase = current_intersections[intersection][0]
            current_time = current_intersections[intersection][1]
            new_time = current_time + interval
            if phase != current_phase:
                new_time = interval
            try_intersections[phase[0:5]] = (phase, new_time)
        active_flows = state.get_rates(try_intersections, current_intersections, interval)
        max_flows = transition.maximize_flows(active_flows, current_queues)
        successor_queues = state.simulate(current_queues, max_flows)
        try_h = state.heuristic(successor_queues, goal)
        if try_h < best_h:
            next_best_h = best_h
            best_h = try_h
            next_intersections = try_intersections
            #print(next_best_h)
    return next_intersections, next_best_h


def leader_first(current_queues, current_intersections, interval=10):
    successor_intersections = copy.copy(current_intersections)
    successor_queues = current_queues
    for intersection in current_intersections.iterkeys():
        #print(intersection)
        actions = state.applicable_actions(successor_intersections)
        current_phase = successor_intersections[intersection][0]
        current_time = successor_intersections[intersection][1]
        next_best_h = float("inf")
        next_intersections = None
        next_queues = None
        for phase in actions[intersection]:
            #print(phase)
            new_time = current_time + interval
            if phase != current_phase:
                new_time = interval
            try_intersections = copy.copy(successor_intersections)
            try_intersections[intersection] = (phase, new_time)
            active_flows = state.get_rates(try_intersections, successor_intersections, interval)
            max_flows = transition.maximize_flows(active_flows, successor_queues)
            try_queues = state.simulate(successor_queues, max_flows)
            try_h = visited.get(classify_state(try_intersections), state.heuristic(try_queues, goal))
            #try_h = state.heuristic(try_queues, goal)
            #print(try_h)
            if try_h < next_best_h:
                next_best_h = try_h
                next_intersections = try_intersections
                next_queues = try_queues
        successor_queues = next_queues
        successor_intersections = next_intersections
    return successor_intersections, next_best_h


def classify_state(intersections):
    return tuple(x for x, y in intersections.itervalues())


def rta_star(initial_queues, initial_intersections):
    current_queues = initial_queues
    current_intersections = initial_intersections
    execution_time = 0
    #max_search_time = 0
    interval = 10
    search = leader_first
    #search = random_next
    #search = breadth_first_d1
    #print(current_queues)
    #print(goal)
    while not state.is_goal(goal, current_queues):
        start_time = time.clock()
        next_intersections, new_h = search(current_queues, current_intersections)
        end_time = time.clock()-start_time
        hashable = classify_state(current_intersections)
        #if end_time > max_search_time:
        #    max_search_time = end_time
        #print(next_intersections)
        rates = state.get_rates(next_intersections, current_intersections, interval)
        #print(current_queues)
        max_flows = transition.maximize_flows(rates, current_queues)
        #print(max_flows)
        next_queues = state.simulate(current_queues, max_flows)
        #print(next_intersections)
        #state.print_change(current_queues, next_queues)
        visited[hashable] = new_h + 1
        current_queues = next_queues
        current_intersections = next_intersections
        #print(state.heuristic(next_queues, goal))
        #print(visited)
        execution_time += interval
        #print(next_intersections)
        #print(current_queues)
        #print("max search time per iteration so far (seconds): {0}".format(max_search_time))
    #print(current_state)
    print("execution time (seconds): {0}".format(execution_time))
    #print("max search time per iteration (seconds): {0}".format(max_search_time))


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
    domains = []
    domains.append((quick_domain([1, 2, 3, 4], [5, 24, 28, 29], {(3, 5): True, (4, 24): True, (1, 28): True, (2, 29): True}), [1, 2, 3, 4]))
    domains.append((quick_domain([5, 6, 7, 8], [3, 9, 20, 30], {(6, 30): True, (5, 3): True, (7, 9): True, (8, 20): True}), [5, 6, 7, 8]))
    domains.append((quick_domain([9, 10, 11, 12],  [7, 13, 31], {(9, 7): True, (12, 13): True, (10, 31): True}), [9, 10, 11, 12]))
    domains.append((quick_domain([13, 14, 15], [12, 17, 32], {(13, 12): True, (14, 32): True, (15, 17): True}), [13, 14, 15]))
    domains.append((quick_domain([16, 17, 18], [15, 21, 27], {(17, 15): True, (16, 21): True}), [16, 17, 18]))
    domains.append((quick_domain([19, 20, 21, 22], [8, 16, 25, 33], {(20, 8): True, (21, 16): True, (22, 33): True, (19, 25): True}), [19, 20, 21, 22]))
    domains.append((quick_domain([23, 24, 25, 26], [19, 4, 34, 35], {(24, 4): True, (25, 19): True, (26, 34): True, (23, 35): True}), [23, 24, 25, 26]))
    domains.append((quick_domain([27], [0], dict()), [27]))
    domains.append((quick_domain([28], [0], dict()), [28]))
    domains.append((quick_domain([29], [0], dict()), [29]))
    domains.append((quick_domain([30, 31], [0], dict()), [30, 31]))
    domains.append((quick_domain([32], [0], dict()), [32]))
    domains.append((quick_domain([33, 34], [0], dict()), [33, 34]))
    domains.append((quick_domain([35], [0], dict()), [35]))
    sink = 1
    queues = 35 + sink
    #print(domains)
    '''
    queues, intersections, goal = state.init_problem()
    #print(current_state)
    #print(actions)
    #print(goal)
    visited = dict()
    rta_star(queues, intersections)

