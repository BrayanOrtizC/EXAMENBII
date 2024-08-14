import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize


f = lambda x: x**5 - 6 * x**4 + 2 * x**3 + 20 * x**2 - 27 * x + 10
g = lambda x: 0 * x

x = np.arange(-1,3,0.1)
#x = np.arange(-3,6,0.1) ver todos los puntos



plt.subplot(1,1,1)
plt.plot(x, f(x), 'o')
plt.plot(x, g(x))
plt.show()

