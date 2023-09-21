import pandas as pd
import numpy as np
frame = pd.DataFrame(np.arange(16).reshape((4,4)), index=['red', 'blue', 'yellow', 'white'], columns = ['ball', 'pen', 'pencil', 'paper'])
ser = pd.Series(np.arange(4), index=['ball','pen','pencil','paper'])
print('Операции между Dataframe и Series\n\n', frame - ser)
ser['mug'] = 9
print(ser, '\n\n', frame - ser, '\n')