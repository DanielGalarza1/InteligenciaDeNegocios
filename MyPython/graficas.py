import numpy as np
import matplotlib.pyplot as plt 

n = 12
y = np.zeros(n)
x1 = np.linspace(0,10,n,endpoint=True)
x2 = np.linspace(0,10,n,endpoint=False)
plt.plot(x1, y, 'o')
plt.plot(x2, y+0.2, 'o')
plt.ylim([-0.3,0.5])
plt.show()

# Graficar una funcion como el seno, coseno, tangente
x = np.linspace(-3,3,500)
y = np.sin(x)
plt.plot(x,y)
plt.show()