import unittest
import rta_star
import numpy

class MyTestCase(unittest.TestCase):

    def test_h(self):
        current_state = numpy.arange(8)
        goal = numpy.asarray([0] * 8)
        visited = dict()
        h = rta_star.h(current_state, visited)
        self.assertEqual(h, numpy.linalg.norm(current_state - goal), h)

    def test_h_visited(self):
        current_state = numpy.arange(8)
        goal = numpy.asarray([0] * 8)
        visited = dict()
        improved_h = 100
        visited[tuple(current_state)] = improved_h
        h = rta_star.h(current_state, visited)
        self.assertEqual(h, improved_h, h)

    def test_min_local_f(self):
        current_state = numpy.arange(3) + 1
        phases = ((0, 1), (0, 2))
        visited = dict()
        best, next_best = rta_star.min_local_f(current_state, phases, visited)
        self.assertEqual(best[0] < next_best[0], True, (current_state, best, next_best))

    def test_min_local_visited(self):
        current_state = numpy.arange(3) + 1
        phases = ((0, 1), (0, 2))
        visited = dict()
        assignments = ((0, (0, 1)), )
        visited_state = rta_star.simulate(current_state, assignments)
        visited[tuple(visited_state)] = 100
        best, next_best = rta_star.min_local_f(current_state, phases, visited)
        self.assertEqual(best[1], (0, 2), (current_state, best, next_best))

    def test_visited_h(self):
        current_state = numpy.arange(3) + 1
        visited = dict()
        best = [(1.0, (1, 0, 1, 1))]
        alternatives = [(2.0, (2, 0, 1, 2))]
        next_best_h = rta_star.visited_h(alternatives, current_state, visited, 1, best)
        #goal = numpy.asarray([0] * len(current_state))
        #self.assertEqual(next_best_h > h, True, (next_best_h, h))

    def test_min_f(self):
        domains = (((0, 1), (0, 2)), )
        current_state = numpy.arange(3) + 1
        visited = dict()
        best, next_best_h = rta_star.min_f(domains, current_state, visited)
        self.assertEqual(best[0] < next_best_h, True, (best, next_best_h))

    def test_min_heap(self):
        heap = []
        import heapq
        heapq.heappush(heap, (1, (1, 1)))
        heapq.heappush(heap, (2, (1, 1)))
        popped = heapq.heappop(heap)
        self.assertEqual(popped, False, popped)

if __name__ == '__main__':
    unittest.main()
