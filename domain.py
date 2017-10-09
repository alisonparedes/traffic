def connect(east_west, north_south):
    intersections = []
    m = east_west
    n = north_south
    for i in range(n):
        for j in range(m):
            in_queues = []
            out_queues = []
            exceptions = dict()
            for q in range(4):
                queue = j*4+q+1+i*n*4
                in_queues.append(queue)
            north = (i-1)*m*4+j*4+4
            if north < 0:
                north = 0
            south = (i+1)*m*4+j*4+2
            if south > m*n*4:
                south = 0
            east = i*m*4+j*4+5
            if in_queues[3]%(m*4) == 0:
                east = 0
            west = i*m*4+j*4-1
            if in_queues[0]%(m*4) == 1:
                west = 0
            out_queues = list(set([north, south, east, west]))
            if len(out_queues) == 4:
                exceptions[(in_queues[0], west)] = True
                exceptions[(in_queues[1], north)] = True
                exceptions[(in_queues[2], east)] = True
                exceptions[(in_queues[3], south)] = True
            else:
                if in_queues[0] == 1:
                    exceptions[(in_queues[2], east)] = True
                    exceptions[(in_queues[3], south)] = True
                elif in_queues[3] == m*4:
                    exceptions[(in_queues[0], west)] = True
                    exceptions[(in_queues[3], south)] = True
                elif in_queues[0] == m*4*(n-1)+1:
                    exceptions[(in_queues[1], north)] = True
                    exceptions[(in_queues[2], east)] = True
                else: #in_queues[3] == m*n:
                    exceptions[(in_queues[0], west)] = True
                    exceptions[(in_queues[1], north)] = True
            intersections.append((in_queues, out_queues, exceptions))
    queues = n * m * 4
    sink = 1
    return queues + sink, intersections

if __name__ == "__main__":
    queues, domain = connect(10, 10)
    print queues
    for intersection in domain:
        print intersection