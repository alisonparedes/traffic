from gurobipy import *

def maximize_flows(rates={}, queues={}):

    m = Model("transition")

    # Edges into network

    # Edges out of network
    '''
    L1202_3967_sink = m.addVar(vtype=GRB.CONTINUOUS, name="L1202_3967_sink")
    '''

    # All other edges
    '''
    L6013_1202__L1202_3967 = m.addVar(vtype=GRB.CONTINUOUS, name="L6013_1202__L1202_3967")
    L1349_1202__L1202_3967 = m.addVar(vtype=GRB.CONTINUOUS, name="L1349_1202__L1202_3967")
    '''
    L1202_1349__L1349_1867 = m.addVar(vtype=GRB.CONTINUOUS, name="L1202_1349__L1349_1867")
    L1202_1349__L1349_3621 = m.addVar(vtype=GRB.CONTINUOUS, name="L1202_1349__L1349_3621")
    L1202_3967__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L1202_3967__outside")
    L1202_6013__L6013_5840 = m.addVar(vtype=GRB.CONTINUOUS, name="L1202_6013__L6013_5840")
    L1202_6013__L6013_6014 = m.addVar(vtype=GRB.CONTINUOUS, name="L1202_6013__L6013_6014")
    L1216_1352__L1352_1867 = m.addVar(vtype=GRB.CONTINUOUS, name="L1216_1352__L1352_1867")
    L1216_1352__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L1216_1352__outside")
    L1233_1352__L1352_1353 = m.addVar(vtype=GRB.CONTINUOUS, name="L1233_1352__L1352_1353")
    L1233_1352__L1352_1867 = m.addVar(vtype=GRB.CONTINUOUS, name="L1233_1352__L1352_1867")
    L1233_1352__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L1233_1352__outside")
    L1349_1202__L1202_3967 = m.addVar(vtype=GRB.CONTINUOUS, name="L1349_1202__L1202_3967")
    L1349_1202__L1202_6013 = m.addVar(vtype=GRB.CONTINUOUS, name="L1349_1202__L1202_6013")
    L1349_1353__L1353_1352 = m.addVar(vtype=GRB.CONTINUOUS, name="L1349_1353__L1353_1352")
    L1349_1353__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L1349_1353__outside")
    L1349_1867__L1867_1352 = m.addVar(vtype=GRB.CONTINUOUS, name="L1349_1867__L1867_1352")
    L1349_1867__L1867_4574 = m.addVar(vtype=GRB.CONTINUOUS, name="L1349_1867__L1867_4574")
    L1349_3621__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L1349_3621__outside")
    L1352_1353__L1353_6014 = m.addVar(vtype=GRB.CONTINUOUS, name="L1352_1353__L1353_6014")
    L1352_1353__L1353_6014 = m.addVar(vtype=GRB.CONTINUOUS, name="L1352_1353__L1353_6014")
    L1352_1353__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L1352_1353__outside")
    L1352_1353__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L1352_1353__outside")
    L1352_1867__L1867_1349 = m.addVar(vtype=GRB.CONTINUOUS, name="L1352_1867__L1867_1349")
    L1352_1867__L1867_3621 = m.addVar(vtype=GRB.CONTINUOUS, name="L1352_1867__L1867_3621")
    L1352_1867__L1867_4574 = m.addVar(vtype=GRB.CONTINUOUS, name="L1352_1867__L1867_4574")
    L1353_1349__L1349_1202 = m.addVar(vtype=GRB.CONTINUOUS, name="L1353_1349__L1349_1202")
    L1353_1349__L1349_1867 = m.addVar(vtype=GRB.CONTINUOUS, name="L1353_1349__L1349_1867")
    L1353_1349__L1349_3621 = m.addVar(vtype=GRB.CONTINUOUS, name="L1353_1349__L1349_3621")
    L1353_1352__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L1353_1352__outside")
    L1353_1352__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L1353_1352__outside")
    L1353_6014__L6014_6013 = m.addVar(vtype=GRB.CONTINUOUS, name="L1353_6014__L6014_6013")
    L1353_6014__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L1353_6014__outside")
    L1867_1349__L1349_1202 = m.addVar(vtype=GRB.CONTINUOUS, name="L1867_1349__L1349_1202")
    L1867_1349__L1349_1353 = m.addVar(vtype=GRB.CONTINUOUS, name="L1867_1349__L1349_1353")
    L1867_1349__L1349_3621 = m.addVar(vtype=GRB.CONTINUOUS, name="L1867_1349__L1349_3621")
    L1867_1352__L1352_1353 = m.addVar(vtype=GRB.CONTINUOUS, name="L1867_1352__L1352_1353")
    L1867_1352__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L1867_1352__outside")
    L1867_1352__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L1867_1352__outside")
    L1867_3621__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L1867_3621__outside")
    L1867_4574__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L1867_4574__outside")
    L3621_1349__L1349_1202 = m.addVar(vtype=GRB.CONTINUOUS, name="L3621_1349__L1349_1202")
    L3621_1349__L1349_1353 = m.addVar(vtype=GRB.CONTINUOUS, name="L3621_1349__L1349_1353")
    L3621_1867__L1867_1349 = m.addVar(vtype=GRB.CONTINUOUS, name="L3621_1867__L1867_1349")
    L3621_1867__L1867_1352 = m.addVar(vtype=GRB.CONTINUOUS, name="L3621_1867__L1867_1352")
    L3621_1867__L1867_4574 = m.addVar(vtype=GRB.CONTINUOUS, name="L3621_1867__L1867_4574")
    L3966_1202__L1202_1349 = m.addVar(vtype=GRB.CONTINUOUS, name="L3966_1202__L1202_1349")
    L3966_1202__L1202_6013 = m.addVar(vtype=GRB.CONTINUOUS, name="L3966_1202__L1202_6013")
    L4574_1867__L1867_1349 = m.addVar(vtype=GRB.CONTINUOUS, name="L4574_1867__L1867_1349")
    L4574_1867__L1867_1352 = m.addVar(vtype=GRB.CONTINUOUS, name="L4574_1867__L1867_1352")
    L4574_1867__L1867_3621 = m.addVar(vtype=GRB.CONTINUOUS, name="L4574_1867__L1867_3621")
    L5840_6013__L6013_1202 = m.addVar(vtype=GRB.CONTINUOUS, name="L5840_6013__L6013_1202")
    L5840_6013__L6013_6014 = m.addVar(vtype=GRB.CONTINUOUS, name="L5840_6013__L6013_6014")
    L6013_1202__L1202_1349 = m.addVar(vtype=GRB.CONTINUOUS, name="L6013_1202__L1202_1349")
    L6013_1202__L1202_3967 = m.addVar(vtype=GRB.CONTINUOUS, name="L6013_1202__L1202_3967")
    #L6013_5840__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L6013_5840__outside")
    L6013_6014__L6014_1353 = m.addVar(vtype=GRB.CONTINUOUS, name="L6013_6014__L6014_1353")
    L6013_6014__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L6013_6014__outside")
    L6014_1353__L1353_1349 = m.addVar(vtype=GRB.CONTINUOUS, name="L6014_1353__L1353_1349")
    L6014_1353__L1353_1352 = m.addVar(vtype=GRB.CONTINUOUS, name="L6014_1353__L1353_1352")
    L6014_6013__L6013_1202 = m.addVar(vtype=GRB.CONTINUOUS, name="L6014_6013__L6013_1202")
    L6014_6013__L6013_5840 = m.addVar(vtype=GRB.CONTINUOUS, name="L6014_6013__L6013_5840")
    L6159_1353__L1353_1349 = m.addVar(vtype=GRB.CONTINUOUS, name="L6159_1353__L1353_1349")
    L6159_1353__L1353_1352 = m.addVar(vtype=GRB.CONTINUOUS, name="L6159_1353__L1353_1352")
    L6159_6014__L6014_1353 = m.addVar(vtype=GRB.CONTINUOUS, name="L6159_6014__L6014_1353")
    L6159_6014__L6014_6013 = m.addVar(vtype=GRB.CONTINUOUS, name="L6159_6014__L6014_6013")
    outside__L1216_1352 = m.addVar(vtype=GRB.CONTINUOUS, name="outside__L1216_1352")
    outside__L1233_1352 = m.addVar(vtype=GRB.CONTINUOUS, name="outside__L1233_1352")
    outside__L3621_1867 = m.addVar(vtype=GRB.CONTINUOUS, name="outside__L3621_1867")
    outside__L5840_6013 = m.addVar(vtype=GRB.CONTINUOUS, name="outside__L5840_6013")
    outside__L6159_1353 = m.addVar(vtype=GRB.CONTINUOUS, name="outside__L6159_1353")
    outside__L6159_6014 = m.addVar(vtype=GRB.CONTINUOUS, name="outside__L6159_6014")


    # Network B

    L1202b_1349b__L1349b_1867b = m.addVar(vtype=GRB.CONTINUOUS, name="L1202b_1349b__L1349b_1867b")
    L1202b_1349b__L1349b_3621b = m.addVar(vtype=GRB.CONTINUOUS, name="L1202b_1349b__L1349b_3621b")
    L1202b_3967b__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L1202b_3967b__outside")
    L1202b_6013b__L6013b_5840b = m.addVar(vtype=GRB.CONTINUOUS, name="L1202b_6013b__L6013b_5840b")
    L1202b_6013b__L6013b_6014b = m.addVar(vtype=GRB.CONTINUOUS, name="L1202b_6013b__L6013b_6014b")
    L1216b_1352b__L1352b_1867b = m.addVar(vtype=GRB.CONTINUOUS, name="L1216b_1352b__L1352b_1867b")
    L1216b_1352b__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L1216b_1352b__outside")
    L1233b_1352b__L1352b_1353b = m.addVar(vtype=GRB.CONTINUOUS, name="L1233b_1352b__L1352b_1353b")
    L1233b_1352b__L1352b_1867b = m.addVar(vtype=GRB.CONTINUOUS, name="L1233b_1352b__L1352b_1867b")
    L1233b_1352b__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L1233b_1352b__outside")
    L1349b_1202b__L1202b_3967b = m.addVar(vtype=GRB.CONTINUOUS, name="L1349b_1202b__L1202b_3967b")
    L1349b_1202b__L1202b_6013b = m.addVar(vtype=GRB.CONTINUOUS, name="L1349b_1202b__L1202b_6013b")
    L1349b_1353b__L1353b_1352b = m.addVar(vtype=GRB.CONTINUOUS, name="L1349b_1353b__L1353b_1352b")
    L1349b_1353b__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L1349b_1353b__outside")
    L1349b_1867b__L1867b_1352b = m.addVar(vtype=GRB.CONTINUOUS, name="L1349b_1867b__L1867b_1352b")
    L1349b_1867b__L1867b_4574b = m.addVar(vtype=GRB.CONTINUOUS, name="L1349b_1867b__L1867b_4574b")
    L1349b_3621b__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L1349b_3621b__outside")
    L1352b_1353b__L1353b_6014b = m.addVar(vtype=GRB.CONTINUOUS, name="L1352b_1353b__L1353b_6014b")
    L1352b_1353b__L1353b_6014b = m.addVar(vtype=GRB.CONTINUOUS, name="L1352b_1353b__L1353b_6014b")
    L1352b_1353b__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L1352b_1353b__outside")
    L1352b_1353b__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L1352b_1353b__outside")
    L1352b_1867b__L1867b_1349b = m.addVar(vtype=GRB.CONTINUOUS, name="L1352b_1867b__L1867b_1349b")
    L1352b_1867b__L1867b_3621b = m.addVar(vtype=GRB.CONTINUOUS, name="L1352b_1867b__L1867b_3621b")
    L1352b_1867b__L1867b_4574b = m.addVar(vtype=GRB.CONTINUOUS, name="L1352b_1867b__L1867b_4574b")
    L1353b_1349b__L1349b_1202b = m.addVar(vtype=GRB.CONTINUOUS, name="L1353b_1349b__L1349b_1202b")
    L1353b_1349b__L1349b_1867b = m.addVar(vtype=GRB.CONTINUOUS, name="L1353b_1349b__L1349b_1867b")
    L1353b_1349b__L1349b_3621b = m.addVar(vtype=GRB.CONTINUOUS, name="L1353b_1349b__L1349b_3621b")
    L1353b_1352b__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L1353b_1352b__outside")
    L1353b_1352b__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L1353b_1352b__outside")
    L1353b_6014b__L6014b_6013b = m.addVar(vtype=GRB.CONTINUOUS, name="L1353b_6014b__L6014b_6013b")
    L1353b_6014b__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L1353b_6014b__outside")
    L1867b_1349b__L1349b_1202b = m.addVar(vtype=GRB.CONTINUOUS, name="L1867b_1349b__L1349b_1202b")
    L1867b_1349b__L1349b_1353b = m.addVar(vtype=GRB.CONTINUOUS, name="L1867b_1349b__L1349b_1353b")
    L1867b_1349b__L1349b_3621b = m.addVar(vtype=GRB.CONTINUOUS, name="L1867b_1349b__L1349b_3621b")
    L1867b_1352b__L1352b_1353b = m.addVar(vtype=GRB.CONTINUOUS, name="L1867b_1352b__L1352b_1353b")
    L1867b_1352b__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L1867b_1352b__outside")
    L1867b_1352b__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L1867b_1352b__outside")
    L1867b_3621b__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L1867b_3621b__outside")
    L1867b_4574b__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L1867b_4574b__outside")
    L3621b_1349b__L1349b_1202b = m.addVar(vtype=GRB.CONTINUOUS, name="L3621b_1349b__L1349b_1202b")
    L3621b_1349b__L1349b_1353b = m.addVar(vtype=GRB.CONTINUOUS, name="L3621b_1349b__L1349b_1353b")
    L3621b_1867b__L1867b_1349b = m.addVar(vtype=GRB.CONTINUOUS, name="L3621b_1867b__L1867b_1349b")
    L3621b_1867b__L1867b_1352b = m.addVar(vtype=GRB.CONTINUOUS, name="L3621b_1867b__L1867b_1352b")
    L3621b_1867b__L1867b_4574b = m.addVar(vtype=GRB.CONTINUOUS, name="L3621b_1867b__L1867b_4574b")
    L3966b_1202b__L1202b_1349b = m.addVar(vtype=GRB.CONTINUOUS, name="L3966b_1202b__L1202b_1349b")
    L3966b_1202b__L1202b_6013b = m.addVar(vtype=GRB.CONTINUOUS, name="L3966b_1202b__L1202b_6013b")
    L4574b_1867b__L1867b_1349b = m.addVar(vtype=GRB.CONTINUOUS, name="L4574b_1867b__L1867b_1349b")
    L4574b_1867b__L1867b_1352b = m.addVar(vtype=GRB.CONTINUOUS, name="L4574b_1867b__L1867b_1352b")
    L4574b_1867b__L1867b_3621b = m.addVar(vtype=GRB.CONTINUOUS, name="L4574b_1867b__L1867b_3621b")
    L5840b_6013b__L6013b_1202b = m.addVar(vtype=GRB.CONTINUOUS, name="L5840b_6013b__L6013b_1202b")
    L5840b_6013b__L6013b_6014b = m.addVar(vtype=GRB.CONTINUOUS, name="L5840b_6013b__L6013b_6014b")
    L6013b_1202b__L1202b_1349b = m.addVar(vtype=GRB.CONTINUOUS, name="L6013b_1202b__L1202b_1349b")
    L6013b_1202b__L1202b_3967b = m.addVar(vtype=GRB.CONTINUOUS, name="L6013b_1202b__L1202b_3967b")
    L6013b_5840b__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L6013b_5840b__outside")
    L6013b_6014b__L6014b_1353b = m.addVar(vtype=GRB.CONTINUOUS, name="L6013b_6014b__L6014b_1353b")
    L6013b_6014b__outside = m.addVar(vtype=GRB.CONTINUOUS, name="L6013b_6014b__outside")
    L6014b_1353b__L1353b_1349b = m.addVar(vtype=GRB.CONTINUOUS, name="L6014b_1353b__L1353b_1349b")
    L6014b_1353b__L1353b_1352b = m.addVar(vtype=GRB.CONTINUOUS, name="L6014b_1353b__L1353b_1352b")
    L6014b_6013b__L6013b_1202b = m.addVar(vtype=GRB.CONTINUOUS, name="L6014b_6013b__L6013b_1202b")
    L6014b_6013b__L6013b_5840b = m.addVar(vtype=GRB.CONTINUOUS, name="L6014b_6013b__L6013b_5840b")
    L6159b_1353b__L1353b_1349b = m.addVar(vtype=GRB.CONTINUOUS, name="L6159b_1353b__L1353b_1349b")
    L6159b_1353b__L1353b_1352b = m.addVar(vtype=GRB.CONTINUOUS, name="L6159b_1353b__L1353b_1352b")
    L6159b_6014b__L6014b_1353b = m.addVar(vtype=GRB.CONTINUOUS, name="L6159b_6014b__L6014b_1353b")
    L6159b_6014b__L6014b_6013b = m.addVar(vtype=GRB.CONTINUOUS, name="L6159b_6014b__L6014b_6013b")
    outside__L1216b_1352b = m.addVar(vtype=GRB.CONTINUOUS, name="outside__L1216b_1352b")
    L5840_1233b__L1233b_1352b = m.addVar(vtype=GRB.CONTINUOUS, name="L5840_1233b__L1233b_1352b")
    outside__L3621b_1867b = m.addVar(vtype=GRB.CONTINUOUS, name="outside__L3621b_1867b")
    outside__L5840b_6013b = m.addVar(vtype=GRB.CONTINUOUS, name="outside__L5840b_6013b")
    outside__L6159b_1353b = m.addVar(vtype=GRB.CONTINUOUS, name="outside__L6159b_1353b")
    outside__L6159b_6014b = m.addVar(vtype=GRB.CONTINUOUS, name="outside__L6159b_6014b")

    # Connecting edges
    L6013_5840__L5840_1233b = m.addVar(vtype=GRB.CONTINUOUS, name="L6013_5840__L5840_1233b")
    L1233b_5840__L5840_6013 = m.addVar(vtype=GRB.CONTINUOUS, name="L1233b_5840__L5840_6013")
    L1352b_1233b__L1233b_5840 = m.addVar(vtype=GRB.CONTINUOUS, name="L1352b_1233b__L1233b_5840")

    '''
    m.setObjective(L1202_3967_sink
                   + L6013_1202_L1202_3967
                   + L1349_1202_L1202_3967
                   , GRB.MAXIMIZE)
    '''
    m.setObjective(L1202_1349__L1349_1867
        + L1202_1349__L1349_3621
        + L1202_3967__outside
        + L1202_6013__L6013_5840
        + L1202_6013__L6013_6014
        + L1216_1352__L1352_1867
        + L1216_1352__outside
        + L1233_1352__L1352_1353
        + L1233_1352__L1352_1867
        + L1233_1352__outside
        + L1349_1202__L1202_3967
        + L1349_1202__L1202_6013
        + L1349_1353__L1353_1352
        + L1349_1353__outside
        + L1349_1867__L1867_1352
        + L1349_1867__L1867_4574
        + L1349_3621__outside
        + L1352_1353__L1353_6014
        + L1352_1353__L1353_6014
        + L1352_1353__outside
        + L1352_1353__outside
        + L1352_1867__L1867_1349
        + L1352_1867__L1867_3621
        + L1352_1867__L1867_4574
        + L1353_1349__L1349_1202
        + L1353_1349__L1349_1867
        + L1353_1349__L1349_3621
        + L1353_1352__outside
        + L1353_1352__outside
        + L1353_6014__L6014_6013
        + L1353_6014__outside
        + L1867_1349__L1349_1202
        + L1867_1349__L1349_1353
        + L1867_1349__L1349_3621
        + L1867_1352__L1352_1353
        + L1867_1352__outside
        + L1867_1352__outside
        + L1867_3621__outside
        + L1867_4574__outside
        + L3621_1349__L1349_1202
        + L3621_1349__L1349_1353
        + L3621_1867__L1867_1349
        + L3621_1867__L1867_1352
        + L3621_1867__L1867_4574
        + L3966_1202__L1202_1349
        + L3966_1202__L1202_6013
        + L4574_1867__L1867_1349
        + L4574_1867__L1867_1352
        + L4574_1867__L1867_3621
        + L5840_6013__L6013_1202
        + L5840_6013__L6013_6014
        + L6013_1202__L1202_1349
        + L6013_1202__L1202_3967
        #+ L6013_5840__outside
        + L6013_6014__L6014_1353
        + L6013_6014__outside
        + L6014_1353__L1353_1349
        + L6014_1353__L1353_1352
        + L6014_6013__L6013_1202
        + L6014_6013__L6013_5840
        + L6159_1353__L1353_1349
        + L6159_1353__L1353_1352
        + L6159_6014__L6014_1353
        + L6159_6014__L6014_6013
        + outside__L1216_1352
        + outside__L1233_1352
        + outside__L3621_1867
        + outside__L5840_6013
        + outside__L6159_1353
        + outside__L6159_6014
        + L1202b_1349b__L1349b_1867b
        + L1202b_1349b__L1349b_3621b
        + L1202b_3967b__outside
        + L1202b_6013b__L6013b_5840b
        + L1202b_6013b__L6013b_6014b
        + L1216b_1352b__L1352b_1867b
        + L1216b_1352b__outside
        + L1233b_1352b__L1352b_1353b
        + L1233b_1352b__L1352b_1867b
        + L1233b_1352b__outside
        + L1349b_1202b__L1202b_3967b
        + L1349b_1202b__L1202b_6013b
        + L1349b_1353b__L1353b_1352b
        + L1349b_1353b__outside
        + L1349b_1867b__L1867b_1352b
        + L1349b_1867b__L1867b_4574b
        + L1349b_3621b__outside
        + L1352b_1353b__L1353b_6014b
        + L1352b_1353b__L1353b_6014b
        + L1352b_1353b__outside
        + L1352b_1353b__outside
        + L1352b_1867b__L1867b_1349b
        + L1352b_1867b__L1867b_3621b
        + L1352b_1867b__L1867b_4574b
        + L1353b_1349b__L1349b_1202b
        + L1353b_1349b__L1349b_1867b
        + L1353b_1349b__L1349b_3621b
        + L1353b_1352b__outside
        + L1353b_1352b__outside
        + L1353b_6014b__L6014b_6013b
        + L1353b_6014b__outside
        + L1867b_1349b__L1349b_1202b
        + L1867b_1349b__L1349b_1353b
        + L1867b_1349b__L1349b_3621b
        + L1867b_1352b__L1352b_1353b
        + L1867b_1352b__outside
        + L1867b_1352b__outside
        + L1867b_3621b__outside
        + L1867b_4574b__outside
        + L3621b_1349b__L1349b_1202b
        + L3621b_1349b__L1349b_1353b
        + L3621b_1867b__L1867b_1349b
        + L3621b_1867b__L1867b_1352b
        + L3621b_1867b__L1867b_4574b
        + L3966b_1202b__L1202b_1349b
        + L3966b_1202b__L1202b_6013b
        + L4574b_1867b__L1867b_1349b
        + L4574b_1867b__L1867b_1352b
        + L4574b_1867b__L1867b_3621b
        + L5840b_6013b__L6013b_1202b
        + L5840b_6013b__L6013b_6014b
        + L6013b_1202b__L1202b_1349b
        + L6013b_1202b__L1202b_3967b
        #+ L6013_5840__outside
        + L6013b_6014b__L6014b_1353b
        + L6013b_6014b__outside
        + L6014b_1353b__L1353b_1349b
        + L6014b_1353b__L1353b_1352b
        + L6014b_6013b__L6013b_1202b
        + L6014b_6013b__L6013b_5840b
        + L6159b_1353b__L1353b_1349b
        + L6159b_1353b__L1353b_1352b
        + L6159b_6014b__L6014b_1353b
        + L6159b_6014b__L6014b_6013b
        + outside__L1216b_1352b
        + L5840_1233b__L1233b_1352b
        + outside__L3621b_1867b
        + outside__L5840b_6013b
        + outside__L6159b_1353b
        + outside__L6159b_6014b

        #Connecting edges
        + L6013_5840__L5840_1233b
        + L1233b_5840__L5840_6013
        + L5840_1233b__L1233b_1352b
        + L1352b_1233b__L1233b_5840
        , GRB.MAXIMIZE)

    # Maximum capacities
    '''
    m.addConstr(L6013_1202_L1202_3967
                + L1349_1202_L1202_3967
                - L1202_3967_sink 
                <= 20, 
                "cap_L1202_3967")
    '''
    m.addConstr(L6013_1202__L1202_1349
                + L3966_1202__L1202_1349
                - L1202_1349__L1349_1867
                - L1202_1349__L1349_3621
                + queues["L1202_1349"]
                <= 88
                , "L1202_1349")
    m.addConstr(L1202_1349__L1349_1867
                + L1202_1349__L1349_3621
                <= queues["L1202_1349"])
    m.addConstr(L6013_1202__L1202_3967
                + L1349_1202__L1202_3967
                - L1202_3967__outside
                + queues["L1202_3967"]
                <= 138
                , "L1202_3967")
    m.addConstr(L1202_3967__outside
                <= queues["L1202_3967"])
    m.addConstr(L1349_1202__L1202_6013
                + L3966_1202__L1202_6013
                - L1202_6013__L6013_5840
                - L1202_6013__L6013_6014
                + queues["L1202_6013"]
                <= 61
                , "L1202_6013")
    m.addConstr(L1202_6013__L6013_5840
                + L1202_6013__L6013_6014
                <= queues["L1202_6013"])
    m.addConstr(outside__L1216_1352
                - L1216_1352__L1352_1867
                - L1216_1352__outside
                + queues["L1216_1352"]
                <= 13
                , "L1216_1352") # There may be a bug in the original model here.
    m.addConstr(L1216_1352__L1352_1867
                + L1216_1352__outside
                <= queues["L1216_1352"])
    m.addConstr(outside__L1233_1352
                - L1233_1352__L1352_1353
                - L1233_1352__L1352_1867
                - L1233_1352__outside
                + queues["L1233_1352"]
                <= 30
                , "L1233_1352") # Here too
    m.addConstr(L1233_1352__L1352_1353
                + L1233_1352__L1352_1867
                + L1233_1352__outside
                <= queues["L1233_1352"])
    m.addConstr(L1353_1349__L1349_1202
                + L3621_1349__L1349_1202
                + L1867_1349__L1349_1202
                - L1349_1202__L1202_3967
                - L1349_1202__L1202_6013
                + queues["L1349_1202"]
                <= 89
                , "L1349_1202")
    m.addConstr(L1349_1202__L1202_3967
                + L1349_1202__L1202_6013
                <= queues["L1349_1202"])
    m.addConstr(L3621_1349__L1349_1353
                + L1867_1349__L1349_1353
                - L1349_1353__L1353_1352
                - L1349_1353__outside
                + queues["L1349_1353"]
                <= 78
                , "L1349_1353")
    m.addConstr(L1349_1353__L1353_1352
                + L1349_1353__outside
                <= queues["L1349_1353"])
    m.addConstr(L1353_1349__L1349_1867
                + L1202_1349__L1349_1867
                - L1349_1867__L1867_1352
                - L1349_1867__L1867_4574
                + queues["L1349_1867"]
                <= 63
                , "L1349_1867")
    m.addConstr(L1349_1867__L1867_1352
                + L1349_1867__L1867_4574
                <= queues["L1349_1867"])
    m.addConstr(L1867_1349__L1349_3621
                + L1202_1349__L1349_3621
                + L1353_1349__L1349_3621
                - L1349_3621__outside
                + queues["L1349_3621"]
                <= 181
                , "L1349_3621")
    m.addConstr(L1349_3621__outside
                <= queues["L1349_3621"])
    m.addConstr(L1867_1352__L1352_1353
                + L1233_1352__L1352_1353
                - L1352_1353__L1353_6014
                - L1352_1353__outside
                + queues["L1352_1353"]
                <= 60
                , "L1352_1353")
    m.addConstr(L1352_1353__L1353_6014
                + L1352_1353__outside
                <= queues["L1352_1353"])
    m.addConstr(L1216_1352__L1352_1867
                + L1233_1352__L1352_1867
                - L1352_1867__L1867_1349
                - L1352_1867__L1867_3621
                - L1352_1867__L1867_4574
                + queues["L1352_1867"]
                <= 73
                , "L1352_1867")
    m.addConstr(L1352_1867__L1867_1349
                + L1352_1867__L1867_3621
                + L1352_1867__L1867_4574
                <= queues["L1352_1867"])
    m.addConstr(L6159_1353__L1353_1349
                + L6014_1353__L1353_1349
                - L1353_1349__L1349_1202
                - L1353_1349__L1349_1867
                - L1353_1349__L1349_3621
                + queues["L1353_1349"]
                <= 88
                , "L1353_1349")
    m.addConstr(L1353_1349__L1349_1202
                + L1353_1349__L1349_1867
                + L1353_1349__L1349_3621
                <= queues["L1353_1349"])
    m.addConstr(L1349_1353__L1353_1352
                + L6159_1353__L1353_1352
                + L6014_1353__L1353_1352
                - L1353_1352__outside
                + queues["L1353_1352"]
                <= 119
                , "L1353_1352")  # And this one
    m.addConstr(L1353_1352__outside
                <= queues["L1353_1352"])
    m.addConstr(L1352_1353__L1353_6014
                + L1352_1353__L1353_6014
                - L1353_6014__L6014_6013
                - L1353_6014__outside
                + queues["L1353_6014"]
                <= 24
                , "L1353_6014")
    m.addConstr(L1353_6014__L6014_6013
                + L1353_6014__outside
                <= queues["L1353_6014"])
    m.addConstr(L3621_1867__L1867_1349
                + L1352_1867__L1867_1349
                + L4574_1867__L1867_1349
                - L1867_1349__L1349_1202
                - L1867_1349__L1349_1353
                - L1867_1349__L1349_3621
                + queues["L1867_1349"]
                <= 104
                , "L1867_1349")
    m.addConstr(L1867_1349__L1349_1202
                + L1867_1349__L1349_1353
                + L1867_1349__L1349_3621
                <= queues["L1867_1349"])
    m.addConstr(L4574_1867__L1867_1352
                + L1349_1867__L1867_1352
                + L3621_1867__L1867_1352
                - L1867_1352__L1352_1353
                - L1867_1352__outside
                + queues["L1867_1352"]
                <= 128
                , "L1867_1352")
    m.addConstr(L1867_1352__L1352_1353
                + L1867_1352__outside
                <= queues["L1867_1352"])
    m.addConstr(L4574_1867__L1867_3621
                + L1352_1867__L1867_3621
                - L1867_3621__outside
                + queues["L1867_3621"]
                <= 19
                , "L1867_3621")
    m.addConstr(L1867_3621__outside
                <= queues["L1867_3621"])
    m.addConstr(L4574_1867__L1867_3621
                + L1352_1867__L1867_3621
                - L1867_3621__outside
                + queues["L1867_3621"]
                <= 62 # A bug? Weaker constraint than above
                , "L1867_3621")
    m.addConstr(L1867_3621__outside
                <= queues["L1867_3621"])
    m.addConstr(L1349_1867__L1867_4574
                + L1352_1867__L1867_4574
                + L3621_1867__L1867_4574
                - L1867_4574__outside
                + queues["L1867_4574"]
                <=82
                , "L1867_4574")
    m.addConstr(L1867_4574__outside
                <= queues["L1867_4574"])
    #m.addConstr(- L3621_1349__L1349_1202
    #            - L3621_1349__L1349_1353
    #            #+ queues["L3621_1349"]  # Problem initially exceeds capacity
    #            <= 75
    #            , "L3621_1349") # This constraint is always true
    m.addConstr(L3621_1349__L1349_1202
                + L3621_1349__L1349_1353
                <= queues["L3621_1349"])
    m.addConstr(outside__L3621_1867
                - L3621_1867__L1867_1349
                - L3621_1867__L1867_1352
                - L3621_1867__L1867_4574
                + queues["L3621_1867"]
                <=60
                , "L3621_1867")
    m.addConstr(L3621_1867__L1867_1349
                + L3621_1867__L1867_1352
                + L3621_1867__L1867_4574
                <= queues["L3621_1867"])
    #m.addConstr(- L3966_1202__L1202_1349
    #            - L3966_1202__L1202_6013
    #            #+ queues["L3966_1202"]  # Problem initially exceeds capacity
    #            <= 101 # Always true
    #            , "L3966_1202")
    m.addConstr(L3966_1202__L1202_1349
                + L3966_1202__L1202_6013
                <= queues["L3966_1202"])
    #m.addConstr(- L4574_1867__L1867_1349
    #            - L4574_1867__L1867_1352
    #            - L4574_1867__L1867_3621
    #            #+ queues["L4574_1867"]  # Problem initially exceeds capacity
    #            <= 179 # Always true
    #            , "L4574_1867")
    m.addConstr(L4574_1867__L1867_1349
                + L4574_1867__L1867_1352
                + L4574_1867__L1867_3621
                <= queues["L4574_1867"])
    m.addConstr(outside__L5840_6013
                - L5840_6013__L6013_1202
                - L5840_6013__L6013_6014
                + queues["L5840_6013"]
                <= 40
                , "L5840_6013")
    m.addConstr(L5840_6013__L6013_1202
                + L5840_6013__L6013_6014
                <= queues["L5840_6013"])
    m.addConstr(L5840_6013__L6013_1202
                + L6014_6013__L6013_1202
                - L6013_1202__L1202_1349
                - L6013_1202__L1202_3967
                + queues["L6013_1202"]
                <=35
                , "L6013_1202")
    m.addConstr(L6013_1202__L1202_1349
                + L6013_1202__L1202_3967
                <= queues["L6013_1202"])
    m.addConstr(L1202_6013__L6013_5840
                + L6014_6013__L6013_5840
                - L6013_5840__L5840_1233b
                + queues["L6013_5840"]
                <= 24
                , "L6013_5840")
    m.addConstr(L6013_5840__L5840_1233b
                <= queues["L6013_5840"])
    m.addConstr(L1202_6013__L6013_6014
                + L5840_6013__L6013_6014
                - L6013_6014__L6014_1353
                - L6013_6014__outside
                + queues["L6013_6014"]
                <= 94
                , "L6013_6014")
    m.addConstr(L6013_6014__L6014_1353
                + L6013_6014__outside
                <= queues["L6013_6014"])
    m.addConstr(L6013_6014__L6014_1353
                + L6159_6014__L6014_1353
                - L6014_1353__L1353_1349
                - L6014_1353__L1353_1352
                + queues["L6014_1353"]
                <= 23
                , "L6014_1353")
    m.addConstr(L6014_1353__L1353_1349
                + L6014_1353__L1353_1352
                <= queues["L6014_1353"])
    m.addConstr(L1353_6014__L6014_6013
                + L6159_6014__L6014_6013
                - L6014_6013__L6013_1202
                - L6014_6013__L6013_5840
                + queues["L6014_6013"]
                <= 94
                , "L6014_6013")
    m.addConstr(L6014_6013__L6013_1202
                + L6014_6013__L6013_5840
                <= queues["L6014_6013"])
    m.addConstr(outside__L6159_1353
                - L6159_1353__L1353_1349
                - L6159_1353__L1353_1352
                + queues["L6159_1353"]
                <= 24
                , "L6159_1353")
    m.addConstr(L6159_1353__L1353_1349
                + L6159_1353__L1353_1352
                <= queues["L6159_1353"])
    m.addConstr(outside__L6159_6014
                - L6159_6014__L6014_1353
                - L6159_6014__L6014_6013
                + queues["L6159_6014"]
                <= 218
                , "L6159_6014")
    m.addConstr(L6159_6014__L6014_1353
                + L6159_6014__L6014_6013
                <= queues["L6159_6014"])

    # Network B

    m.addConstr(L6013b_1202b__L1202b_1349b
                + L3966b_1202b__L1202b_1349b
                - L1202b_1349b__L1349b_1867b
                - L1202b_1349b__L1349b_3621b
                + queues["L1202b_1349b"]
                <= 88
                , "L1202b_1349b")
    m.addConstr(L1202b_1349b__L1349b_1867b
                + L1202b_1349b__L1349b_3621b
                <= queues["L1202b_1349b"])
    m.addConstr(L6013b_1202b__L1202b_3967b
                + L1349b_1202b__L1202b_3967b
                - L1202b_3967b__outside
                + queues["L1202b_3967b"]
                <= 138
                , "L1202b_3967b")
    m.addConstr(L1202b_3967b__outside
                <= queues["L1202b_3967b"])
    m.addConstr(L1349b_1202b__L1202b_6013b
                + L3966b_1202b__L1202b_6013b
                - L1202b_6013b__L6013b_5840b
                - L1202b_6013b__L6013b_6014b
                + queues["L1202b_6013b"]
                <= 61
                , "L1202b_6013b")
    m.addConstr(L1202b_6013b__L6013b_5840b
                + L1202b_6013b__L6013b_6014b
                <= queues["L1202b_6013b"])
    m.addConstr(outside__L1216b_1352b
                - L1216b_1352b__L1352b_1867b
                - L1216b_1352b__outside
                + queues["L1216b_1352b"]
                <= 13
                , "L1216b_1352b") # There may be a bug in the original model here.
    m.addConstr(L1216b_1352b__L1352b_1867b
                + L1216b_1352b__outside
                <= queues["L1216b_1352b"])
    m.addConstr(L5840_1233b__L1233b_1352b
                - L1233b_1352b__L1352b_1353b
                - L1233b_1352b__L1352b_1867b
                - L1233b_1352b__outside
                + queues["L1233b_1352b"]
                <= 30
                , "L1233b_1352b") # Here too
    m.addConstr(L1233b_1352b__L1352b_1353b
                + L1233b_1352b__L1352b_1867b
                + L1233b_1352b__outside
                <= queues["L1233b_1352b"])
    m.addConstr(L1353b_1349b__L1349b_1202b
                + L3621b_1349b__L1349b_1202b
                + L1867b_1349b__L1349b_1202b
                - L1349b_1202b__L1202b_3967b
                - L1349b_1202b__L1202b_6013b
                + queues["L1349b_1202b"]
                <= 89
                , "L1349b_1202b")
    m.addConstr(L1349b_1202b__L1202b_3967b
                + L1349b_1202b__L1202b_6013b
                <= queues["L1349b_1202b"])
    m.addConstr(L3621b_1349b__L1349b_1353b
                + L1867b_1349b__L1349b_1353b
                - L1349b_1353b__L1353b_1352b
                - L1349b_1353b__outside
                + queues["L1349b_1353b"]
                <= 78
                , "L1349b_1353b")
    m.addConstr(L1349b_1353b__L1353b_1352b
                + L1349b_1353b__outside
                <= queues["L1349b_1353b"])
    m.addConstr(L1353b_1349b__L1349b_1867b
                + L1202b_1349b__L1349b_1867b
                - L1349b_1867b__L1867b_1352b
                - L1349b_1867b__L1867b_4574b
                + queues["L1349b_1867b"]
                <= 63
                , "L1349b_1867b")
    m.addConstr(L1349b_1867b__L1867b_1352b
                + L1349b_1867b__L1867b_4574b
                <= queues["L1349b_1867b"])
    m.addConstr(L1867b_1349b__L1349b_3621b
                + L1202b_1349b__L1349b_3621b
                + L1353b_1349b__L1349b_3621b
                - L1349b_3621b__outside
                + queues["L1349b_3621b"]
                <= 181
                , "L1349b_3621b")
    m.addConstr(L1349b_3621b__outside
                <= queues["L1349b_3621b"])
    m.addConstr(L1867b_1352b__L1352b_1353b
                + L1233b_1352b__L1352b_1353b
                - L1352b_1353b__L1353b_6014b
                - L1352b_1353b__outside
                + queues["L1352b_1353b"]
                <= 60
                , "L1352b_1353b")
    m.addConstr(L1352b_1353b__L1353b_6014b
                + L1352b_1353b__outside
                <= queues["L1352b_1353b"])
    m.addConstr(L1216b_1352b__L1352b_1867b
                + L1233b_1352b__L1352b_1867b
                - L1352b_1867b__L1867b_1349b
                - L1352b_1867b__L1867b_3621b
                - L1352b_1867b__L1867b_4574b
                + queues["L1352b_1867b"]
                <= 73
                , "L1352b_1867b")
    m.addConstr(L1352b_1867b__L1867b_1349b
                + L1352b_1867b__L1867b_3621b
                + L1352b_1867b__L1867b_4574b
                <= queues["L1352b_1867b"])
    m.addConstr(L6159b_1353b__L1353b_1349b
                + L6014b_1353b__L1353b_1349b
                - L1353b_1349b__L1349b_1202b
                - L1353b_1349b__L1349b_1867b
                - L1353b_1349b__L1349b_3621b
                + queues["L1353b_1349b"]
                <= 88
                , "L1353b_1349b")
    m.addConstr(L1353b_1349b__L1349b_1202b
                + L1353b_1349b__L1349b_1867b
                + L1353b_1349b__L1349b_3621b
                <= queues["L1353b_1349b"])
    m.addConstr(L1349b_1353b__L1353b_1352b
                + L6159b_1353b__L1353b_1352b
                + L6014b_1353b__L1353b_1352b
                - L1353b_1352b__outside
                + queues["L1353b_1352b"]
                <= 119
                , "L1353b_1352b")  # And this one
    m.addConstr(L1353b_1352b__outside
                <= queues["L1353b_1352b"])
    m.addConstr(L1352b_1353b__L1353b_6014b
                + L1352b_1353b__L1353b_6014b
                - L1353b_6014b__L6014b_6013b
                - L1353b_6014b__outside
                + queues["L1353b_6014b"]
                <= 24
                , "L1353b_6014b")
    m.addConstr(L1353b_6014b__L6014b_6013b
                + L1353b_6014b__outside
                <= queues["L1353b_6014b"])
    m.addConstr(L3621b_1867b__L1867b_1349b
                + L1352b_1867b__L1867b_1349b
                + L4574b_1867b__L1867b_1349b
                - L1867b_1349b__L1349b_1202b
                - L1867b_1349b__L1349b_1202b
                - L1867b_1349b__L1349b_1202b
                + queues["L1867b_1349b"]
                <= 104
                , "L1867b_1349b")
    m.addConstr(L1867b_1349b__L1349b_1202b
                + L1867b_1349b__L1349b_1353b
                + L1867b_1349b__L1349b_3621b
                <= queues["L1867b_1349b"])
    m.addConstr(L4574b_1867b__L1867b_1352b
                + L1349b_1867b__L1867b_1352b
                + L3621b_1867b__L1867b_1352b
                - L1867b_1352b__L1352b_1353b
                - L1867b_1352b__outside
                + queues["L1867b_1352b"]
                <= 128
                , "L1867b_1352b")
    m.addConstr(L1867b_1352b__L1352b_1353b
                + L1867b_1352b__outside
                <= queues["L1867b_1352b"])
    m.addConstr(L4574b_1867b__L1867b_3621b
                + L1352b_1867b__L1867b_3621b
                - L1867b_3621b__outside
                + queues["L1867b_3621b"]
                <= 19
                , "L1867b_3621b")
    m.addConstr(L1867b_3621b__outside
                <= queues["L1867b_3621b"])
    m.addConstr(L4574b_1867b__L1867b_3621b
                + L1352b_1867b__L1867b_3621b
                - L1867b_3621b__outside
                + queues["L1867b_3621b"]
                <= 62 # A bug? Weaker constraint than above
                , "L1867b_3621b")
    m.addConstr(L1867b_3621b__outside
                <= queues["L1867b_3621b"])
    m.addConstr(L1349b_1867b__L1867b_4574b
                + L1352b_1867b__L1867b_4574b
                + L3621b_1867b__L1867b_4574b
                - L1867b_4574b__outside
                + queues["L1867b_4574b"]
                <=82
                , "L1867b_4574b")
    m.addConstr(L1867b_4574b__outside
                <= queues["L1867b_4574b"])
    m.addConstr(- L3621b_1349b__L1349b_1202b
                - L3621b_1349b__L1349b_1353b
                + queues["L3621b_1349b"]
                <= 75
                , "L3621b_1349b")
    m.addConstr(L3621b_1349b__L1349b_1202b
                + L3621b_1349b__L1349b_1353b
                <= queues["L3621b_1349b"])
    m.addConstr(outside__L3621b_1867b
                - L3621b_1867b__L1867b_1349b
                - L3621b_1867b__L1867b_1352b
                - L3621b_1867b__L1867b_4574b
                + queues["L3621b_1867b"]
                <=60
                , "L3621b_1867b")
    m.addConstr(L3621b_1867b__L1867b_1349b
                + L3621b_1867b__L1867b_1352b
                + L3621b_1867b__L1867b_4574b
                <= queues["L3621b_1867b"])
    m.addConstr(- L3966b_1202b__L1202b_1349b
                - L3966b_1202b__L1202b_6013b
                + queues["L3966b_1202b"]
                <= 101
                , "L3966b_1202b")
    m.addConstr(L3966b_1202b__L1202b_1349b
                + L3966b_1202b__L1202b_6013b
                <= queues["L3966b_1202b"])
    m.addConstr(- L4574b_1867b__L1867b_1349b
                - L4574b_1867b__L1867b_1352b
                - L4574b_1867b__L1867b_3621b
                + queues["L4574b_1867b"]
                <= 179
                , "L4574b_1867b")
    m.addConstr(L4574b_1867b__L1867b_1349b
                + L4574b_1867b__L1867b_1352b
                + L4574b_1867b__L1867b_3621b
                <= queues["L4574b_1867b"])
    m.addConstr(outside__L5840b_6013b
                - L5840b_6013b__L6013b_1202b
                - L5840b_6013b__L6013b_6014b
                + queues["L5840b_6013b"]
                <= 40
                , "L5840b_6013b")
    m.addConstr(L5840b_6013b__L6013b_1202b
                + L5840b_6013b__L6013b_6014b
                <= queues["L5840b_6013b"])
    m.addConstr(L5840b_6013b__L6013b_1202b
                + L6014b_6013b__L6013b_1202b
                - L6013b_1202b__L1202b_1349b
                - L6013b_1202b__L1202b_3967b
                + queues["L6013b_1202b"]
                <=35
                , "L6013b_1202b")
    m.addConstr(L6013b_1202b__L1202b_1349b
                + L6013b_1202b__L1202b_3967b
                <= queues["L6013b_1202b"])
    m.addConstr(L1202b_6013b__L6013b_5840b
                + L6014b_6013b__L6013b_5840b
                - L6013b_5840b__outside
                + queues["L6013b_5840b"]
                <= 24
                , "L6013b_5840b")
    m.addConstr(L6013b_5840b__outside
                <= queues["L6013b_5840b"])
    m.addConstr(L1202b_6013b__L6013b_6014b
                + L5840b_6013b__L6013b_6014b
                - L6013b_6014b__L6014b_1353b
                - L6013b_6014b__outside
                + queues["L6013b_6014b"]
                <= 94
                , "L6013b_6014b")
    m.addConstr(L6013b_6014b__L6014b_1353b
                + L6013b_6014b__outside
                <= queues["L6013b_6014b"])
    m.addConstr(L6013b_6014b__L6014b_1353b
                + L6159b_6014b__L6014b_1353b
                - L6014b_1353b__L1353b_1349b
                - L6014b_1353b__L1353b_1352b
                + queues["L6014b_1353b"]
                <= 23
                , "L6014b_1353b")
    m.addConstr(L6014b_1353b__L1353b_1349b
                + L6014b_1353b__L1353b_1352b
                <= queues["L6014b_1353b"])
    m.addConstr(L1353b_6014b__L6014b_6013b
                + L6159b_6014b__L6014b_6013b
                - L6014b_6013b__L6013b_1202b
                - L6014b_6013b__L6013b_5840b
                + queues["L6014b_6013b"]
                <= 94
                , "L6014b_6013b")
    m.addConstr(L6014b_6013b__L6013b_1202b
                + L6014b_6013b__L6013b_5840b
                <= queues["L6014b_6013b"])
    m.addConstr(outside__L6159b_1353b
                - L6159b_1353b__L1353b_1349b
                - L6159b_1353b__L1353b_1352b
                + queues["L6159b_1353b"]
                <= 24
                , "L6159b_1353b")
    m.addConstr(L6159b_1353b__L1353b_1349b
                + L6159b_1353b__L1353b_1352b
                <= queues["L6159b_1353b"])
    m.addConstr(outside__L6159b_6014b
                - L6159b_6014b__L6014b_1353b
                - L6159b_6014b__L6014b_6013b
                + queues["L6159b_6014b"]
                <= 218
                , "L6159b_6014b")
    m.addConstr(L6159b_6014b__L6014b_1353b
                + L6159b_6014b__L6014b_6013b
                <= queues["L6159b_6014b"])

    # Connecting queues
    m.addConstr(L6013_5840__L5840_1233b
                - L5840_1233b__L1233b_1352b
                + queues["L5840_1233b"]
                <= 80
                , "L5840_1233b")
    m.addConstr(L5840_1233b__L1233b_1352b
                <= queues["L5840_1233b"])

    m.addConstr(L1352b_1233b__L1233b_5840
                - L1233b_5840__L5840_6013
                + queues["L1233b_5840"]
                <= 80
                , "L1233b_5840")
    m.addConstr(L1233b_5840__L5840_6013
                <= queues["L1233b_5840"])

    # Maximum flow
    '''
    m.addConstr(L1202_3967_sink <= 0.49333 * t * flows["L1202_3967_sink"])
    m.addConstr(L6013_1202_L1202_3967 <= 0.41067 * t * flows["L6013_1202_L1202_3967"])
    m.addConstr(L1349_1202_L1202_3967 <= 0.825 * t * flows["L1349_1202_L1202_3967"])
    '''
    m.addConstr(L1202_1349__L1349_1867 <= rates["L1202_1349__L1349_1867"])
    m.addConstr(L1202_1349__L1349_3621 <= rates["L1202_1349__L1349_3621"])
    m.addConstr(L1202_3967__outside <= rates["L1202_3967__outside"])
    m.addConstr(L1202_6013__L6013_5840 <= rates["L1202_6013__L6013_5840"])
    m.addConstr(L1202_6013__L6013_6014 <= rates["L1202_6013__L6013_6014"])
    m.addConstr(L1216_1352__L1352_1867 <= rates["L1216_1352__L1352_1867"])
    m.addConstr(L1216_1352__outside <= rates["L1216_1352__outside"])
    m.addConstr(L1233_1352__L1352_1353 <= rates["L1233_1352__L1352_1353"])
    m.addConstr(L1233_1352__L1352_1867 <= rates["L1233_1352__L1352_1867"])
    m.addConstr(L1233_1352__outside <= rates["L1233_1352__outside"])
    m.addConstr(L1349_1202__L1202_3967 <= rates["L1349_1202__L1202_3967"])
    m.addConstr(L1349_1202__L1202_6013 <= rates["L1349_1202__L1202_6013"])
    m.addConstr(L1349_1353__L1353_1352 <= rates["L1349_1353__L1353_1352"])
    m.addConstr(L1349_1353__outside <= rates["L1349_1353__outside"])
    m.addConstr(L1349_1867__L1867_1352 <= rates["L1349_1867__L1867_1352"])
    m.addConstr(L1349_1867__L1867_4574 <= rates["L1349_1867__L1867_4574"])
    m.addConstr(L1349_3621__outside <= rates["L1349_3621__outside"])
    m.addConstr(L1352_1353__L1353_6014 <= rates["L1352_1353__L1353_6014"])
    m.addConstr(L1352_1353__L1353_6014 <= rates["L1352_1353__L1353_6014"])
    m.addConstr(L1352_1353__outside <= rates["L1352_1353__outside"])
    m.addConstr(L1352_1353__outside <= rates["L1352_1353__outside"])
    m.addConstr(L1352_1867__L1867_1349 <= rates["L1352_1867__L1867_1349"])
    m.addConstr(L1352_1867__L1867_3621 <= rates["L1352_1867__L1867_3621"])
    m.addConstr(L1352_1867__L1867_4574 <= rates["L1352_1867__L1867_4574"])
    m.addConstr(L1353_1349__L1349_1202 <= rates["L1353_1349__L1349_1202"])
    m.addConstr(L1353_1349__L1349_1867 <= rates["L1353_1349__L1349_1867"])
    m.addConstr(L1353_1349__L1349_3621 <= rates["L1353_1349__L1349_3621"])
    m.addConstr(L1353_1352__outside <= rates["L1353_1352__outside"])
    m.addConstr(L1353_1352__outside <= rates["L1353_1352__outside"])
    m.addConstr(L1353_6014__L6014_6013 <= rates["L1353_6014__L6014_6013"])
    m.addConstr(L1353_6014__outside <= rates["L1353_6014__outside"])
    m.addConstr(L1867_1349__L1349_1202 <= rates["L1867_1349__L1349_1202"])
    m.addConstr(L1867_1349__L1349_1353 <= rates["L1867_1349__L1349_1353"])
    m.addConstr(L1867_1349__L1349_3621 <= rates["L1867_1349__L1349_3621"])
    m.addConstr(L1867_1352__L1352_1353 <= rates["L1867_1352__L1352_1353"])
    m.addConstr(L1867_1352__outside <= rates["L1867_1352__outside"])
    m.addConstr(L1867_1352__outside <= rates["L1867_1352__outside"])
    m.addConstr(L1867_3621__outside <= rates["L1867_3621__outside"])
    m.addConstr(L1867_4574__outside <= rates["L1867_4574__outside"])
    m.addConstr(L3621_1349__L1349_1202 <= rates["L3621_1349__L1349_1202"])
    m.addConstr(L3621_1349__L1349_1353 <= rates["L3621_1349__L1349_1353"])
    m.addConstr(L3621_1867__L1867_1349 <= rates["L3621_1867__L1867_1349"])
    m.addConstr(L3621_1867__L1867_1352 <= rates["L3621_1867__L1867_1352"])
    m.addConstr(L3621_1867__L1867_4574 <= rates["L3621_1867__L1867_4574"])
    m.addConstr(L3966_1202__L1202_1349 <= rates["L3966_1202__L1202_1349"])
    m.addConstr(L3966_1202__L1202_6013 <= rates["L3966_1202__L1202_6013"])
    m.addConstr(L4574_1867__L1867_1349 <= rates["L4574_1867__L1867_1349"])
    m.addConstr(L4574_1867__L1867_1352 <= rates["L4574_1867__L1867_1352"])
    m.addConstr(L4574_1867__L1867_3621 <= rates["L4574_1867__L1867_3621"])
    m.addConstr(L5840_6013__L6013_1202 <= rates["L5840_6013__L6013_1202"])
    m.addConstr(L5840_6013__L6013_6014 <= rates["L5840_6013__L6013_6014"])
    m.addConstr(L6013_1202__L1202_1349 <= rates["L6013_1202__L1202_1349"])
    m.addConstr(L6013_1202__L1202_3967 <= rates["L6013_1202__L1202_3967"])
    m.addConstr(L6013_5840__L5840_1233b <= rates["L6013_5840__L5840_1233b"])  # Connects to network B
    m.addConstr(L6013_6014__L6014_1353 <= rates["L6013_6014__L6014_1353"])
    m.addConstr(L6013_6014__outside <= rates["L6013_6014__outside"])
    m.addConstr(L6014_1353__L1353_1349 <= rates["L6014_1353__L1353_1349"])
    m.addConstr(L6014_1353__L1353_1352 <= rates["L6014_1353__L1353_1352"])
    m.addConstr(L6014_6013__L6013_1202 <= rates["L6014_6013__L6013_1202"])
    m.addConstr(L6014_6013__L6013_5840 <= rates["L6014_6013__L6013_5840"])
    m.addConstr(L6159_1353__L1353_1349 <= rates["L6159_1353__L1353_1349"])
    m.addConstr(L6159_1353__L1353_1352 <= rates["L6159_1353__L1353_1352"])
    m.addConstr(L6159_6014__L6014_1353 <= rates["L6159_6014__L6014_1353"])
    m.addConstr(L6159_6014__L6014_6013 <= rates["L6159_6014__L6014_6013"])
    m.addConstr(outside__L1216_1352 <= rates["outside__L1216_1352"])
    m.addConstr(outside__L1233_1352 <= rates["outside__L1233_1352"])
    m.addConstr(outside__L3621_1867 <= rates["outside__L3621_1867"])
    m.addConstr(outside__L5840_6013 <= rates["outside__L5840_6013"])
    m.addConstr(outside__L6159_1353 <= rates["outside__L6159_1353"])
    m.addConstr(outside__L6159_6014 <= rates["outside__L6159_6014"])

    # Network B
    m.addConstr(L1202b_1349b__L1349b_1867b <= rates["L1202b_1349b__L1349b_1867b"])
    m.addConstr(L1202b_1349b__L1349b_3621b <= rates["L1202b_1349b__L1349b_3621b"])
    m.addConstr(L1202b_3967b__outside <= rates["L1202b_3967b__outside"])
    m.addConstr(L1202b_6013b__L6013b_5840b <= rates["L1202b_6013b__L6013b_5840b"])
    m.addConstr(L1202b_6013b__L6013b_6014b <= rates["L1202b_6013b__L6013b_6014b"])
    m.addConstr(L1216b_1352b__L1352b_1867b <= rates["L1216b_1352b__L1352b_1867b"])
    m.addConstr(L1216b_1352b__outside <= rates["L1216b_1352b__outside"])
    m.addConstr(L1233b_1352b__L1352b_1353b <= rates["L1233b_1352b__L1352b_1353b"])
    m.addConstr(L1233b_1352b__L1352b_1867b <= rates["L1233b_1352b__L1352b_1867b"])
    m.addConstr(L1233b_1352b__outside <= rates["L1233b_1352b__outside"])
    m.addConstr(L1349b_1202b__L1202b_3967b <= rates["L1349b_1202b__L1202b_3967b"])
    m.addConstr(L1349b_1202b__L1202b_6013b <= rates["L1349b_1202b__L1202b_6013b"])
    m.addConstr(L1349b_1353b__L1353b_1352b <= rates["L1349b_1353b__L1353b_1352b"])
    m.addConstr(L1349b_1353b__outside <= rates["L1349b_1353b__outside"])
    m.addConstr(L1349b_1867b__L1867b_1352b <= rates["L1349b_1867b__L1867b_1352b"])
    m.addConstr(L1349b_1867b__L1867b_4574b <= rates["L1349b_1867b__L1867b_4574b"])
    m.addConstr(L1349b_3621b__outside <= rates["L1349b_3621b__outside"])
    m.addConstr(L1352b_1353b__L1353b_6014b <= rates["L1352b_1353b__L1353b_6014b"])
    m.addConstr(L1352b_1353b__L1353b_6014b <= rates["L1352b_1353b__L1353b_6014b"])
    m.addConstr(L1352b_1353b__outside <= rates["L1352b_1353b__outside"])
    m.addConstr(L1352b_1353b__outside <= rates["L1352b_1353b__outside"])
    m.addConstr(L1352b_1867b__L1867b_1349b <= rates["L1352b_1867b__L1867b_1349b"])
    m.addConstr(L1352b_1867b__L1867b_3621b <= rates["L1352b_1867b__L1867b_3621b"])
    m.addConstr(L1352b_1867b__L1867b_4574b <= rates["L1352b_1867b__L1867b_4574b"])
    m.addConstr(L1353b_1349b__L1349b_1202b <= rates["L1353b_1349b__L1349b_1202b"])
    m.addConstr(L1353b_1349b__L1349b_1867b <= rates["L1353b_1349b__L1349b_1867b"])
    m.addConstr(L1353b_1349b__L1349b_3621b <= rates["L1353b_1349b__L1349b_3621b"])
    m.addConstr(L1353b_1352b__outside <= rates["L1353b_1352b__outside"])
    m.addConstr(L1353b_1352b__outside <= rates["L1353b_1352b__outside"])
    m.addConstr(L1353b_6014b__L6014b_6013b <= rates["L1353b_6014b__L6014b_6013b"])
    m.addConstr(L1353b_6014b__outside <= rates["L1353b_6014b__outside"])
    m.addConstr(L1867b_1349b__L1349b_1202b <= rates["L1867b_1349b__L1349b_1202b"])
    m.addConstr(L1867b_1349b__L1349b_1353b <= rates["L1867b_1349b__L1349b_1353b"])
    m.addConstr(L1867b_1349b__L1349b_3621b <= rates["L1867b_1349b__L1349b_3621b"])
    m.addConstr(L1867b_1352b__L1352b_1353b <= rates["L1867b_1352b__L1352b_1353b"])
    m.addConstr(L1867b_1352b__outside <= rates["L1867b_1352b__outside"])
    m.addConstr(L1867b_1352b__outside <= rates["L1867b_1352b__outside"])
    m.addConstr(L1867b_3621b__outside <= rates["L1867b_3621b__outside"])
    m.addConstr(L1867b_4574b__outside <= rates["L1867b_4574b__outside"])
    m.addConstr(L3621b_1349b__L1349b_1202b <= rates["L3621b_1349b__L1349b_1202b"])
    m.addConstr(L3621b_1349b__L1349b_1353b <= rates["L3621b_1349b__L1349b_1353b"])
    m.addConstr(L3621b_1867b__L1867b_1349b <= rates["L3621b_1867b__L1867b_1349b"])
    m.addConstr(L3621b_1867b__L1867b_1352b <= rates["L3621b_1867b__L1867b_1352b"])
    m.addConstr(L3621b_1867b__L1867b_4574b <= rates["L3621b_1867b__L1867b_4574b"])
    m.addConstr(L3966b_1202b__L1202b_1349b <= rates["L3966b_1202b__L1202b_1349b"])
    m.addConstr(L3966b_1202b__L1202b_6013b <= rates["L3966b_1202b__L1202b_6013b"])
    m.addConstr(L4574b_1867b__L1867b_1349b <= rates["L4574b_1867b__L1867b_1349b"])
    m.addConstr(L4574b_1867b__L1867b_1352b <= rates["L4574b_1867b__L1867b_1352b"])
    m.addConstr(L4574b_1867b__L1867b_3621b <= rates["L4574b_1867b__L1867b_3621b"])
    m.addConstr(L5840b_6013b__L6013b_1202b <= rates["L5840b_6013b__L6013b_1202b"])
    m.addConstr(L5840b_6013b__L6013b_6014b <= rates["L5840b_6013b__L6013b_6014b"])
    m.addConstr(L6013b_1202b__L1202b_1349b <= rates["L6013b_1202b__L1202b_1349b"])
    m.addConstr(L6013b_1202b__L1202b_3967b <= rates["L6013b_1202b__L1202b_3967b"])
    m.addConstr(L6013b_5840b__outside <= rates["L6013b_5840b__outside"])
    m.addConstr(L6013b_6014b__L6014b_1353b <= rates["L6013b_6014b__L6014b_1353b"])
    m.addConstr(L6013b_6014b__outside <= rates["L6013b_6014b__outside"])
    m.addConstr(L6014b_1353b__L1353b_1349b <= rates["L6014b_1353b__L1353b_1349b"])
    m.addConstr(L6014b_1353b__L1353b_1352b <= rates["L6014b_1353b__L1353b_1352b"])
    m.addConstr(L6014b_6013b__L6013b_1202b <= rates["L6014b_6013b__L6013b_1202b"])
    m.addConstr(L6014b_6013b__L6013b_5840b <= rates["L6014b_6013b__L6013b_5840b"])
    m.addConstr(L6159b_1353b__L1353b_1349b <= rates["L6159b_1353b__L1353b_1349b"])
    m.addConstr(L6159b_1353b__L1353b_1352b <= rates["L6159b_1353b__L1353b_1352b"])
    m.addConstr(L6159b_6014b__L6014b_1353b <= rates["L6159b_6014b__L6014b_1353b"])
    m.addConstr(L6159b_6014b__L6014b_6013b <= rates["L6159b_6014b__L6014b_6013b"])
    m.addConstr(outside__L1216b_1352b <= rates["outside__L1216b_1352b"])
    m.addConstr(L5840_1233b__L1233b_1352b <= rates["L5840_1233b__L1233b_1352b"])  # Connects to Network A
    m.addConstr(outside__L3621b_1867b <= rates["outside__L3621b_1867b"])
    m.addConstr(outside__L5840b_6013b <= rates["outside__L5840b_6013b"])
    m.addConstr(outside__L6159b_1353b <= rates["outside__L6159b_1353b"])
    m.addConstr(outside__L6159b_6014b <= rates["outside__L6159b_6014b"])

    # Connecting edges
    m.addConstr(L6013_5840__L5840_1233b <= rates["L6013_5840__L5840_1233b"])


    # Non-negative
    '''
    m.addConstr(L1202_3967_sink >= 0)
    m.addConstr(L6013_1202_L1202_3967 >= 0)
    m.addConstr(L1349_1202_L1202_3967 >= 0)
    '''
    m.addConstr(L1202_1349__L1349_1867 >= 0)
    m.addConstr(L1202_1349__L1349_3621 >= 0)
    m.addConstr(L1202_3967__outside >= 0)
    m.addConstr(L1202_6013__L6013_5840 >= 0)
    m.addConstr(L1202_6013__L6013_6014 >= 0)
    m.addConstr(L1216_1352__L1352_1867 >= 0)
    m.addConstr(L1216_1352__outside >= 0)
    m.addConstr(L1233_1352__L1352_1353 >= 0)
    m.addConstr(L1233_1352__L1352_1867 >= 0)
    m.addConstr(L1233_1352__outside >= 0)
    m.addConstr(L1349_1202__L1202_3967 >= 0)
    m.addConstr(L1349_1202__L1202_6013 >= 0)
    m.addConstr(L1349_1353__L1353_1352 >= 0)
    m.addConstr(L1349_1353__outside >= 0)
    m.addConstr(L1349_1867__L1867_1352 >= 0)
    m.addConstr(L1349_1867__L1867_4574 >= 0)
    m.addConstr(L1349_3621__outside >= 0)
    m.addConstr(L1352_1353__L1353_6014 >= 0)
    m.addConstr(L1352_1353__L1353_6014 >= 0)
    m.addConstr(L1352_1353__outside >= 0)
    m.addConstr(L1352_1353__outside >= 0)
    m.addConstr(L1352_1867__L1867_1349 >= 0)
    m.addConstr(L1352_1867__L1867_3621 >= 0)
    m.addConstr(L1352_1867__L1867_4574 >= 0)
    m.addConstr(L1353_1349__L1349_1202 >= 0)
    m.addConstr(L1353_1349__L1349_1867 >= 0)
    m.addConstr(L1353_1349__L1349_3621 >= 0)
    m.addConstr(L1353_1352__outside >= 0)
    m.addConstr(L1353_1352__outside >= 0)
    m.addConstr(L1353_6014__L6014_6013 >= 0)
    m.addConstr(L1353_6014__outside >= 0)
    m.addConstr(L1867_1349__L1349_1202 >= 0)
    m.addConstr(L1867_1349__L1349_1353 >= 0)
    m.addConstr(L1867_1349__L1349_3621 >= 0)
    m.addConstr(L1867_1352__L1352_1353 >= 0)
    m.addConstr(L1867_1352__outside >= 0)
    m.addConstr(L1867_1352__outside >= 0)
    m.addConstr(L1867_3621__outside >= 0)
    m.addConstr(L1867_4574__outside >= 0)
    m.addConstr(L3621_1349__L1349_1202 >= 0)
    m.addConstr(L3621_1349__L1349_1353 >= 0)
    m.addConstr(L3621_1867__L1867_1349 >= 0)
    m.addConstr(L3621_1867__L1867_1352 >= 0)
    m.addConstr(L3621_1867__L1867_4574 >= 0)
    m.addConstr(L3966_1202__L1202_1349 >= 0)
    m.addConstr(L3966_1202__L1202_6013 >= 0)
    m.addConstr(L4574_1867__L1867_1349 >= 0)
    m.addConstr(L4574_1867__L1867_1352 >= 0)
    m.addConstr(L4574_1867__L1867_3621 >= 0)
    m.addConstr(L5840_6013__L6013_1202 >= 0)
    m.addConstr(L5840_6013__L6013_6014 >= 0)
    m.addConstr(L6013_1202__L1202_1349 >= 0)
    m.addConstr(L6013_1202__L1202_3967 >= 0)
    m.addConstr(L6013_5840__L5840_1233b >= 0)  # Connects to network B
    m.addConstr(L6013_6014__L6014_1353 >= 0)
    m.addConstr(L6013_6014__outside >= 0)
    m.addConstr(L6014_1353__L1353_1349 >= 0)
    m.addConstr(L6014_1353__L1353_1352 >= 0)
    m.addConstr(L6014_6013__L6013_1202 >= 0)
    m.addConstr(L6014_6013__L6013_5840 >= 0)
    m.addConstr(L6159_1353__L1353_1349 >= 0)
    m.addConstr(L6159_1353__L1353_1352 >= 0)
    m.addConstr(L6159_6014__L6014_1353 >= 0)
    m.addConstr(L6159_6014__L6014_6013 >= 0)
    m.addConstr(outside__L1216_1352 >= 0)
    m.addConstr(outside__L1233_1352 >= 0)
    m.addConstr(outside__L3621_1867 >= 0)
    m.addConstr(outside__L5840_6013 >= 0)
    m.addConstr(outside__L6159_1353 >= 0)
    m.addConstr(outside__L6159_6014 >= 0)

    # Network B

    m.addConstr(L1202b_1349b__L1349b_1867b >= 0)
    m.addConstr(L1202b_1349b__L1349b_3621b >= 0)
    m.addConstr(L1202b_3967b__outside >= 0)
    m.addConstr(L1202b_6013b__L6013b_5840b >= 0)
    m.addConstr(L1202b_6013b__L6013b_6014b >= 0)
    m.addConstr(L1216b_1352b__L1352b_1867b >= 0)
    m.addConstr(L1216b_1352b__outside >= 0)
    m.addConstr(L1233b_1352b__L1352b_1353b >= 0)
    m.addConstr(L1233b_1352b__L1352b_1867b >= 0)
    m.addConstr(L1233b_1352b__outside >= 0)
    m.addConstr(L1349b_1202b__L1202b_3967b >= 0)
    m.addConstr(L1349b_1202b__L1202b_6013b >= 0)
    m.addConstr(L1349b_1353b__L1353b_1352b >= 0)
    m.addConstr(L1349b_1353b__outside >= 0)
    m.addConstr(L1349b_1867b__L1867b_1352b >= 0)
    m.addConstr(L1349b_1867b__L1867b_4574b >= 0)
    m.addConstr(L1349b_3621b__outside >= 0)
    m.addConstr(L1352b_1353b__L1353b_6014b >= 0)
    m.addConstr(L1352b_1353b__L1353b_6014b >= 0)
    m.addConstr(L1352b_1353b__outside >= 0)
    m.addConstr(L1352b_1353b__outside >= 0)
    m.addConstr(L1352b_1867b__L1867b_1349b >= 0)
    m.addConstr(L1352b_1867b__L1867b_3621b >= 0)
    m.addConstr(L1352b_1867b__L1867b_4574b >= 0)
    m.addConstr(L1353b_1349b__L1349b_1202b >= 0)
    m.addConstr(L1353b_1349b__L1349b_1867b >= 0)
    m.addConstr(L1353b_1349b__L1349b_3621b >= 0)
    m.addConstr(L1353b_1352b__outside >= 0)
    m.addConstr(L1353b_1352b__outside >= 0)
    m.addConstr(L1353b_6014b__L6014b_6013b >= 0)
    m.addConstr(L1353b_6014b__outside >= 0)
    m.addConstr(L1867b_1349b__L1349b_1202b >= 0)
    m.addConstr(L1867b_1349b__L1349b_1353b >= 0)
    m.addConstr(L1867b_1349b__L1349b_3621b >= 0)
    m.addConstr(L1867b_1352b__L1352b_1353b >= 0)
    m.addConstr(L1867b_1352b__outside >= 0)
    m.addConstr(L1867b_1352b__outside >= 0)
    m.addConstr(L1867b_3621b__outside >= 0)
    m.addConstr(L1867b_4574b__outside >= 0)
    m.addConstr(L3621b_1349b__L1349b_1202b >= 0)
    m.addConstr(L3621b_1349b__L1349b_1353b >= 0)
    m.addConstr(L3621b_1867b__L1867b_1349b >= 0)
    m.addConstr(L3621b_1867b__L1867b_1352b >= 0)
    m.addConstr(L3621b_1867b__L1867b_4574b >= 0)
    m.addConstr(L3966b_1202b__L1202b_1349b >= 0)
    m.addConstr(L3966b_1202b__L1202b_6013b >= 0)
    m.addConstr(L4574b_1867b__L1867b_1349b >= 0)
    m.addConstr(L4574b_1867b__L1867b_1352b >= 0)
    m.addConstr(L4574b_1867b__L1867b_3621b >= 0)
    m.addConstr(L5840b_6013b__L6013b_1202b >= 0)
    m.addConstr(L5840b_6013b__L6013b_6014b >= 0)
    m.addConstr(L6013b_1202b__L1202b_1349b >= 0)
    m.addConstr(L6013b_1202b__L1202b_3967b >= 0)
    m.addConstr(L6013b_5840b__outside >= 0)
    m.addConstr(L6013b_6014b__L6014b_1353b >= 0)
    m.addConstr(L6013b_6014b__outside >= 0)
    m.addConstr(L6014b_1353b__L1353b_1349b >= 0)
    m.addConstr(L6014b_1353b__L1353b_1352b >= 0)
    m.addConstr(L6014b_6013b__L6013b_1202b >= 0)
    m.addConstr(L6014b_6013b__L6013b_5840b >= 0)
    m.addConstr(L6159b_1353b__L1353b_1349b >= 0)
    m.addConstr(L6159b_1353b__L1353b_1352b >= 0)
    m.addConstr(L6159b_6014b__L6014b_1353b >= 0)
    m.addConstr(L6159b_6014b__L6014b_6013b >= 0)
    m.addConstr(outside__L1216b_1352b >= 0)
    m.addConstr(L5840_1233b__L1233b_1352b >= 0)  # Connect back to network A
    m.addConstr(outside__L3621b_1867b >= 0)
    m.addConstr(outside__L5840b_6013b >= 0)
    m.addConstr(outside__L6159b_1353b >= 0)
    m.addConstr(outside__L6159b_6014b >= 0)

    # Connecting edges
    m.addConstr(L6013_5840__L5840_1233b >= 0)


    ''''
    fij = m.addVar(vtype=GRB.CONTINUOUS, name="fij")
    fkj = m.addVar(vtype=GRB.CONTINUOUS, name="fkj")
    
    # Set objective
    m.setObjective(fij + fkj, GRB.MAXIMIZE)
    
    # Add constraint: x + 2 y + 3 z <= 4
    m.addConstr(fij + fkj <= 1, "c0")
    m.addConstr(fij >= 0, "c1")
    m.addConstr(fkj >= 0, "c2")
    m.addConstr(fij <= 1)
    m.addConstr(fkj <= 10)
    '''

    #m.Params.outputFlag = 0  # Suppress logging
    m.optimize()

    max_flow = {}
    for v in m.getVars():
        max_flow[v.varName] = v.x

    return max_flow

if __name__ == "__main__":
    import state

    current_queues, current_intersections, goal = state.init_problem()
    print(current_intersections)
    print(state.get_rates(current_intersections))
    for intersection, phase in current_intersections.iteritems():
        phase_name = phase[0]
        print(state.get_intergreen(phase_name))
