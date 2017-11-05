from gurobipy import *

def maximize_flows(rates={}, queues={}):

    m = Model("transition")

    # Edges into network

    # Edges out of network
    '''
    L1202_3967_sink = m.addVar(vtype=GRB.INTEGER, name="L1202_3967_sink")
    '''

    # All other edges
    '''
    L6013_1202__L1202_3967 = m.addVar(vtype=GRB.INTEGER, name="L6013_1202__L1202_3967")
    L1349_1202__L1202_3967 = m.addVar(vtype=GRB.INTEGER, name="L1349_1202__L1202_3967")
    '''
    L1202_1349__L1349_1867 = m.addVar(vtype=GRB.INTEGER, name="L1202_1349__L1349_1867")
    L1202_1349__L1349_3621 = m.addVar(vtype=GRB.INTEGER, name="L1202_1349__L1349_3621")
    L1202_3967__outside = m.addVar(vtype=GRB.INTEGER, name="L1202_3967__outside")
    L1202_6013__L6013_5840 = m.addVar(vtype=GRB.INTEGER, name="L1202_6013__L6013_5840")
    L1202_6013__L6013_6014 = m.addVar(vtype=GRB.INTEGER, name="L1202_6013__L6013_6014")
    L1216_1352__L1352_1867 = m.addVar(vtype=GRB.INTEGER, name="L1216_1352__L1352_1867")
    L1216_1352__outside = m.addVar(vtype=GRB.INTEGER, name="L1216_1352__outside")
    L1233_1352__L1352_1353 = m.addVar(vtype=GRB.INTEGER, name="L1233_1352__L1352_1353")
    L1233_1352__L1352_1867 = m.addVar(vtype=GRB.INTEGER, name="L1233_1352__L1352_1867")
    L1233_1352__outside = m.addVar(vtype=GRB.INTEGER, name="L1233_1352__outside")
    L1349_1202__L1202_3967 = m.addVar(vtype=GRB.INTEGER, name="L1349_1202__L1202_3967")
    L1349_1202__L1202_6013 = m.addVar(vtype=GRB.INTEGER, name="L1349_1202__L1202_6013")
    L1349_1353__L1353_1352 = m.addVar(vtype=GRB.INTEGER, name="L1349_1353__L1353_1352")
    L1349_1353__outside = m.addVar(vtype=GRB.INTEGER, name="L1349_1353__outside")
    L1349_1867__L1867_1352 = m.addVar(vtype=GRB.INTEGER, name="L1349_1867__L1867_1352")
    L1349_1867__L1867_4574 = m.addVar(vtype=GRB.INTEGER, name="L1349_1867__L1867_4574")
    L1349_3621__outside = m.addVar(vtype=GRB.INTEGER, name="L1349_3621__outside")
    L1352_1353__L1353_6014 = m.addVar(vtype=GRB.INTEGER, name="L1352_1353__L1353_6014")
    L1352_1353__L1353_6014 = m.addVar(vtype=GRB.INTEGER, name="L1352_1353__L1353_6014")
    L1352_1353__outside = m.addVar(vtype=GRB.INTEGER, name="L1352_1353__outside")
    L1352_1353__outside = m.addVar(vtype=GRB.INTEGER, name="L1352_1353__outside")
    L1352_1867__L1867_1349 = m.addVar(vtype=GRB.INTEGER, name="L1352_1867__L1867_1349")
    L1352_1867__L1867_3621 = m.addVar(vtype=GRB.INTEGER, name="L1352_1867__L1867_3621")
    L1352_1867__L1867_4574 = m.addVar(vtype=GRB.INTEGER, name="L1352_1867__L1867_4574")
    L1353_1349__L1349_1202 = m.addVar(vtype=GRB.INTEGER, name="L1353_1349__L1349_1202")
    L1353_1349__L1349_1867 = m.addVar(vtype=GRB.INTEGER, name="L1353_1349__L1349_1867")
    L1353_1349__L1349_3621 = m.addVar(vtype=GRB.INTEGER, name="L1353_1349__L1349_3621")
    L1353_1352__outside = m.addVar(vtype=GRB.INTEGER, name="L1353_1352__outside")
    L1353_1352__outside = m.addVar(vtype=GRB.INTEGER, name="L1353_1352__outside")
    L1353_6014__L6014_6013 = m.addVar(vtype=GRB.INTEGER, name="L1353_6014__L6014_6013")
    L1353_6014__outside = m.addVar(vtype=GRB.INTEGER, name="L1353_6014__outside")
    L1867_1349__L1349_1202 = m.addVar(vtype=GRB.INTEGER, name="L1867_1349__L1349_1202")
    L1867_1349__L1349_1353 = m.addVar(vtype=GRB.INTEGER, name="L1867_1349__L1349_1353")
    L1867_1349__L1349_3621 = m.addVar(vtype=GRB.INTEGER, name="L1867_1349__L1349_3621")
    L1867_1352__L1352_1353 = m.addVar(vtype=GRB.INTEGER, name="L1867_1352__L1352_1353")
    L1867_1352__outside = m.addVar(vtype=GRB.INTEGER, name="L1867_1352__outside")
    L1867_1352__outside = m.addVar(vtype=GRB.INTEGER, name="L1867_1352__outside")
    L1867_3621__outside = m.addVar(vtype=GRB.INTEGER, name="L1867_3621__outside")
    L1867_4574__outside = m.addVar(vtype=GRB.INTEGER, name="L1867_4574__outside")
    L3621_1349__L1349_1202 = m.addVar(vtype=GRB.INTEGER, name="L3621_1349__L1349_1202")
    L3621_1349__L1349_1353 = m.addVar(vtype=GRB.INTEGER, name="L3621_1349__L1349_1353")
    L3621_1867__L1867_1349 = m.addVar(vtype=GRB.INTEGER, name="L3621_1867__L1867_1349")
    L3621_1867__L1867_1352 = m.addVar(vtype=GRB.INTEGER, name="L3621_1867__L1867_1352")
    L3621_1867__L1867_4574 = m.addVar(vtype=GRB.INTEGER, name="L3621_1867__L1867_4574")
    L3966_1202__L1202_1349 = m.addVar(vtype=GRB.INTEGER, name="L3966_1202__L1202_1349")
    L3966_1202__L1202_6013 = m.addVar(vtype=GRB.INTEGER, name="L3966_1202__L1202_6013")
    L4574_1867__L1867_1349 = m.addVar(vtype=GRB.INTEGER, name="L4574_1867__L1867_1349")
    L4574_1867__L1867_1352 = m.addVar(vtype=GRB.INTEGER, name="L4574_1867__L1867_1352")
    L4574_1867__L1867_3621 = m.addVar(vtype=GRB.INTEGER, name="L4574_1867__L1867_3621")
    L5840_6013__L6013_1202 = m.addVar(vtype=GRB.INTEGER, name="L5840_6013__L6013_1202")
    L5840_6013__L6013_6014 = m.addVar(vtype=GRB.INTEGER, name="L5840_6013__L6013_6014")
    L6013_1202__L1202_1349 = m.addVar(vtype=GRB.INTEGER, name="L6013_1202__L1202_1349")
    L6013_1202__L1202_3967 = m.addVar(vtype=GRB.INTEGER, name="L6013_1202__L1202_3967")
    L6013_5840__outside = m.addVar(vtype=GRB.INTEGER, name="L6013_5840__outside")
    L6013_6014__L6014_1353 = m.addVar(vtype=GRB.INTEGER, name="L6013_6014__L6014_1353")
    L6013_6014__outside = m.addVar(vtype=GRB.INTEGER, name="L6013_6014__outside")
    L6014_1353__L1353_1349 = m.addVar(vtype=GRB.INTEGER, name="L6014_1353__L1353_1349")
    L6014_1353__L1353_1352 = m.addVar(vtype=GRB.INTEGER, name="L6014_1353__L1353_1352")
    L6014_6013__L6013_1202 = m.addVar(vtype=GRB.INTEGER, name="L6014_6013__L6013_1202")
    L6014_6013__L6013_5840 = m.addVar(vtype=GRB.INTEGER, name="L6014_6013__L6013_5840")
    L6159_1353__L1353_1349 = m.addVar(vtype=GRB.INTEGER, name="L6159_1353__L1353_1349")
    L6159_1353__L1353_1352 = m.addVar(vtype=GRB.INTEGER, name="L6159_1353__L1353_1352")
    L6159_6014__L6014_1353 = m.addVar(vtype=GRB.INTEGER, name="L6159_6014__L6014_1353")
    L6159_6014__L6014_6013 = m.addVar(vtype=GRB.INTEGER, name="L6159_6014__L6014_6013")
    outside__L1216_1352 = m.addVar(vtype=GRB.INTEGER, name="outside__L1216_1352")
    outside__L1233_1352 = m.addVar(vtype=GRB.INTEGER, name="outside__L1233_1352")
    outside__L3621_1867 = m.addVar(vtype=GRB.INTEGER, name="outside__L3621_1867")
    outside__L5840_6013 = m.addVar(vtype=GRB.INTEGER, name="outside__L5840_6013")
    outside__L6159_1353 = m.addVar(vtype=GRB.INTEGER, name="outside__L6159_1353")
    outside__L6159_6014 = m.addVar(vtype=GRB.INTEGER, name="outside__L6159_6014")

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
                   + L6013_5840__outside
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
                - L6013_5840__outside
                + queues["L6013_5840"]
                <= 24
                , "L6013_5840")
    m.addConstr(L6013_5840__outside
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
    m.addConstr(L6013_5840__outside <= rates["L6013_5840__outside"])
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
    m.addConstr(L6013_5840__outside >= 0)
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


    ''''
    fij = m.addVar(vtype=GRB.INTEGER, name="fij")
    fkj = m.addVar(vtype=GRB.INTEGER, name="fkj")
    
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
    import sys
    print(sys.path)

    t = 10  # seconds
    '''
    flows = {}
    flows[("L1202_3967", "sink")] = 1
    flows[("L6013_1202", "L1202_3967")] = 1
    flows[("L1349_1202", "L1202_3967")] = 1
    '''
    rates = {}
    rates["L1202_1349__L1349_1867"] = 0.73030 * t
    rates["L1202_1349__L1349_3621"] = 0.08 * t
    rates["L1202_3967__outside"] = 0.49333 * t
    rates["L1202_6013__L6013_5840"] = 0.19774 * t
    rates["L1202_6013__L6013_6014"] = 0.14972 * t
    rates["L1216_1352__L1352_1867"] = 0.15385 * t
    rates["L1216_1352__outside"] = 0.10256 * t
    rates["L1233_1352__L1352_1353"] = 0.27778 * t
    rates["L1233_1352__L1352_1867"] = 0.19192 * t
    rates["L1233_1352__outside"] = 0.06061 * t
    rates["L1349_1202__L1202_3967"] = 0.825 * t
    rates["L1349_1202__L1202_6013"] = 0.11138 * t
    rates["L1349_1353__L1353_1352"] = 0.0075 * t
    rates["L1349_1353__outside"] = 0.045 * t
    rates["L1349_1867__L1867_1352"] = 0.07547 * t
    rates["L1349_1867__L1867_4574"] = 0.76730 * t
    rates["L1349_3621__outside"] = 0.075 * t
    rates["L1352_1353__L1353_6014"] = 0.48837 * t
    rates["L1352_1353__L1353_6014"] = 0.72414 * t
    rates["L1352_1353__outside"] = 0.19535 * t
    rates["L1352_1353__outside"] = 0.28966 * t
    rates["L1352_1867__L1867_1349"] = 0.33333 * t
    rates["L1352_1867__L1867_3621"] = 0.21875 * t
    rates["L1352_1867__L1867_4574"] = 0.11458 * t
    rates["L1353_1349__L1349_1202"] = 0.01961 * t
    rates["L1353_1349__L1349_1867"] = 0.35 * t
    rates["L1353_1349__L1349_3621"] = 0.16667 * t
    rates["L1353_1352__outside"] = 0.00505 * t
    rates["L1353_1352__outside"] = 0.05556 * t
    rates["L1353_6014__L6014_6013"] = 0.10714 * t
    rates["L1353_6014__outside"] = 0.01714 * t
    rates["L1867_1349__L1349_1202"] = 0.79845 * t
    rates["L1867_1349__L1349_1353"] = 0.03876 * t
    rates["L1867_1349__L1349_3621"] = 0.00388 * t
    rates["L1867_1352__L1352_1353"] = 0.08333 * t
    rates["L1867_1352__outside"] = 0.14744 * t
    rates["L1867_1352__outside"] = 0.25641 * t
    rates["L1867_3621__outside"] = 0.04833 * t
    rates["L1867_4574__outside"] = 0.46833 * t
    rates["L3621_1349__L1349_1202"] = 0.33333 * t
    rates["L3621_1349__L1349_1353"] = 0.03333 * t
    rates["L3621_1867__L1867_1349"] = 0.125 * t
    rates["L3621_1867__L1867_1352"] = 0.25 * t
    rates["L3621_1867__L1867_4574"] = 0.21875 * t
    rates["L3966_1202__L1202_1349"] = 0.64522 * t
    rates["L3966_1202__L1202_6013"] = 0.71739 * t
    rates["L4574_1867__L1867_1349"] = 0.73077 * t
    rates["L4574_1867__L1867_1352"] = 0.03419 * t
    rates["L4574_1867__L1867_3621"] = 0.04273 * t
    rates["L5840_6013__L6013_1202"] = 0.16667 * t
    rates["L5840_6013__L6013_6014"] = 0.06349 * t
    rates["L6013_1202__L1202_1349"] = 0.165 * t
    rates["L6013_1202__L1202_3967"] = 0.41067 * t
    rates["L6013_5840__outside"] = 0.13833 * t
    rates["L6013_6014__L6014_1353"] = 0.05625 * t
    rates["L6013_6014__outside"] = 0.31875 * t
    rates["L6014_1353__L1353_1349"] = 0.24643 * t
    rates["L6014_1353__L1353_1352"] = 0.075 * t
    rates["L6014_6013__L6013_1202"] = 0.51010 * t
    rates["L6014_6013__L6013_5840"] = 0.02020 * t
    rates["L6159_1353__L1353_1349"] = 0.0525 * t
    rates["L6159_1353__L1353_1352"] = 0.03 * t
    rates["L6159_6014__L6014_1353"] = 0.4 * t
    rates["L6159_6014__L6014_6013"] = 0.37105 * t
    rates["outside__L1216_1352"] = 0.075 * t
    rates["outside__L1233_1352"] = 0.17667 * t
    rates["outside__L3621_1867"] = 0.085 * t
    rates["outside__L5840_6013"] = 0.08333 * t
    rates["outside__L6159_1353"] = 0.01667 * t
    rates["outside__L6159_6014"] = 0.15167 * t

#for _ in range(1000):
#    max_flow = maximize_flows(rates)

#max_flow = maximize_flows(rates)