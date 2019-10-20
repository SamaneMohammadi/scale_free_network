import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

def function(N,gama):
    K_MAX = int(1* N**(1/(gama-1)))
    x = np.arange(1, K_MAX+1, dtype='float')
    pmf = 1/x**gama
    pmf /= pmf.sum()
    d = stats.rv_discrete(values=(range(1, K_MAX+1), pmf))

    sample = d.rvs(size=N)
    y= sorted(list(sample))
    x= [y.count(t) for t in y]

    plt.hist(y, bins=np.arange(K_MAX), linewidth=2, histtype="step",color='red')
    plt.show()

function(10000,3)