import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ts = pd.Series(np.random.randn(365), index=pd.date_range('01/01/2017',periods=365))
ts = ts.cumsum()
ts.plot()
plt.show()