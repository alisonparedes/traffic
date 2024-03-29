import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

beam_d2 = pd.read_csv("data\\beam_d2.csv")
sns.pairplot(beam_d2)

bfs_d1 = pd.read_csv("data\\bfs_d1.csv")
sns.pairplot(bfs_d1)

beam_d2["bfs_d1"] = bfs_d1["ex_time"]
beam_d2["bfs_d1"]

both = (sns.jointplot(x="ex_time",
               y="bfs_d1",
               data=beam_d2,
               xlim=(1000, 2400),
               ylim=(1000, 2400))).set_axis_labels("beam_d2", "bfs_d1")

x0, x1 = both.ax_joint.get_xlim()
y0, y1 = both.ax_joint.get_ylim()

both.ax_joint.plot([x0, x1], [y0, y1], 'b-')