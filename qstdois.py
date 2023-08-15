import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 100)
y = np.linspace(1, 100)

fig, (ax1, ax2, ax3, ax4, ax5, ax6) = plt.subplots(1,6, figsize = (15,2.7))

ax1.plot(x, y) 
ax1.set_title("Função linear")
ax2.plot(x, y**2)
ax2.set_title("Função quadrática")
ax3.plot(x, y**3)
ax3.set_title("Função cúbica")
ax4.plot(x, np.log(y))
ax4.set_title("Função logarítimica")
ax5.plot(x,np.cos(x))
ax5.set_title("Função cosseno")
ax6.plot(x,np.sin(x))
ax6.set_title("Função Seno")

plt.show()