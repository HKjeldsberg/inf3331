import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,1,1001)
y1 = np.sin(2*np.pi*x)
y2 = y1 + 0.09*np.sin(30/5.*2*np.pi*x)
plt.plot(x,y1,x,y2)
plt.grid()
plt.show()
