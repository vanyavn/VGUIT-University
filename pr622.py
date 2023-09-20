import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-5,5,100)
y = lambda x: np.sqrt(abs(x))
plt.plot(x,y(x))
plt.show()