import numpy as np 
from pandas import *
import pandas as pd
import matplotlib.pyplot as plt
D = pd.DataFrame(np.random.randn(6,5))
print(D)
#统计数据的个数，均值，最大值，最小值
print(D.describe())