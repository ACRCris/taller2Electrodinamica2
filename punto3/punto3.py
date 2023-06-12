import numpy as np
import matplotlib.pyplot as plt


# Wikipedia's values for water and vacuum
mur = 0.99992 # relative mu = mu/mu'
n1 = 1.0      # refraction index for vacum
n2 = 1.3330   # refraction index for water


r_perp = lambda i: (2*n1*np.cos(i))/(n1*np.cos(i) + mur*np.sqrt(n2**2 - (n1*np.sin(i))**2))
t_perp = lambda i: (n1*np.cos(i) - mur*np.sqrt(n2**2 - (n1*np.sin(i))**2))/( n1*np.cos(i) + mur*np.sqrt(n2**2 - (n1*np.sin(i))**2))
r_parallel = lambda i: (2*n1*n2*np.cos(i))/( mur*n2**2*np.cos(i) + n1*np.sqrt(n2**2 - (n1*np.sin(i))**2))
t_parallel = lambda i:( mur*n2**2*np.cos(i) - n1*np.sqrt(n2**2 - (n1*np.sin(i))**2))/(mur*n2**2*np.cos(i) + n1*np.sqrt(n2**2 - (n1*np.sin(i))**2)) 

theta = np.linspace(0, np.pi/2, 100)

fig, ax = plt.subplots(2,2, figsize=(14,5))
ax[0][0].plot(theta, r_parallel(theta), label="paralela")
ax[1][0].plot(theta, r_perp(theta), label="perpendicular")
ax[0][1].plot(theta, t_parallel(theta), label="paralela")
ax[1][1].plot(theta, t_perp(theta), label="perpendicular")


ax[0][0].set_ylabel(r"$r$")
ax[0][1].set_ylabel(r"$t$")
ax[1][0].set_ylabel(r"$r$")
ax[1][1].set_ylabel(r"$t$")

ax[0][0].set_title(r"Coeficiente de reflexión $E_r\; / E_0$")
ax[0][1].set_title(r"Coeficiente de transmisión $E_t \; / E_0$")

for i in range (2):
    for j in range (2):
        ax[i][j].legend(title="Polarización:")
        ax[i][j].grid()
        ax[i][j].set_xlabel(r"Ángulo de incidencia, $i$ (rad)")

plt.savefig("Graficas1.png")

fig, ax2 = plt.subplots(1,2, figsize=(12.5,4))


ax2[0].plot(theta, r_parallel(theta), label="paralela")
ax2[0].plot(theta, r_perp(theta), label="perpendicular")
ax2[1].plot(theta, t_parallel(theta), label="paralela")
ax2[1].plot(theta, t_perp(theta), label="perpendicular")


ax2[0].set_ylabel(r"$r$")
ax2[1].set_ylabel(r"$t$")

ax2[0].set_title(r"Coeficiente de reflexión $E_r\; / E_0$")
ax2[1].set_title(r"Coeficiente de transmisión $E_t \; / E_0$")

for i in range (2):
        ax2[i].legend(title="Polarización:")
        ax2[i].grid()
        ax2[i].set_xlabel(r"Ángulo de incidencia, $i$ (rad)")

plt.savefig("Graficas2.png")
plt.show()