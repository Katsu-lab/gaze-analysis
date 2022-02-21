import numpy as np
import matplotlib.pyplot as plt

# x = np.arange(-5, 5, 0.1)
# y = np.sin(x)
# plt.plot(x,y)
# plt.show()

x = [10, 51, 44, 23, 55, 95]
y = [5, 125, 2, 55, 19, 55]
plt.xlim([0,3840])
plt.ylim([0,2160])
plt.scatter(x,y)
plt.show()