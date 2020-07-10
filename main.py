import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")
subdata = data.loc[4:28]
df = nx.from_pandas_edgelist(data, source='Origin', target='Dest', edge_attr=True)
# subgraph = df.subgraph(df.edges[0:15])
print(df.edges)
plt.figure(figsize=(12,8))
nx.draw_networkx(df, with_labels=True)
plt.show()