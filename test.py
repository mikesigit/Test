import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ts = pd.Series(np.random.randn(365), index=pd.date_range('01/01/2017',periods=365))
# ts = ts.cumsum()
# ts.plot()
# plt.show()

# df = pd.DataFrame(np.random.randn(8,6), index=pd.date_range('01/01/2018',periods=8),columns=list('ABCDEF'))
# print(df)

df = pd.read_excel(r"C:\Users\MIKE\Desktop\Data.xlsx", sheet_name="NetworkBridge")

print(type(df))
print(df)



