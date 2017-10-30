from copy import copy
import numpy


def simulate(queues, max_flows):
    new_queues = copy(queues)
    for flow, rate in max_flows.iteritems():
        in_queue, out_queue = flows[flow]
        change = min(queues[in_queue], rate)  # TODO: I want to think there is a better way to simulate this
        new_queues[in_queue] = queues[in_queue] - change
        new_queues[out_queue] = queues[out_queue] + change
    return new_queues


def applicable_actions(intersections, min_time, max_time):
    applicable = {}
    for intersection, state in intersections.iteritems():  #TODO: How does intergreen affect rates and applicable acitons?
        phase = state[0]
        phase_time = state[1]
        #intergreen_ind = state[2]
        #int_time = state[3]
        if not applicable.get(intersection):
            applicable[intersection] = []
        if phase_time > min_time[phase]:
            applicable[intersection].append(cycles[phase])
        if phase_time < max_time[phase]:
            applicable[intersection].append(phase)
    return applicable


def heuristic(goal, queues):
    current_state = []
    goal_state = []
    for queue, capacity in goal.iteritems():
        load = queues[queue]
        if load < capacity:
            load = capacity
        current_state.append(load)
        goal_state.append(capacity)
    h = numpy.linalg.norm(numpy.asarray(current_state) - numpy.asarray(goal_state))
    return h


def is_goal(goal, queues):
    for queue, capacity in goal.iteritems():
        load = queues[queue]
        if load > capacity:
            return False
    return True



def set_rates(intersections, flows, interval, phases):
    rates = {}
    for flow in flows.iterkeys():
        rates[flow] = 0.0
    for phase, _ in intersections.itervalues():
        for flow, rate in phases[phase]:
            rates[flow] = rate * interval
    for flow, rate in phases["fake"]:  # Because some flows are always on
        rates[flow] = rate * interval
    return rates

if __name__ == "__main__":
    pass






