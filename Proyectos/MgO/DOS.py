# _____________________________________________________________________________
# *****************************************************************************
# Autor: José Antonio Quiñonero gris
# Fecha de creación: Monday 19:36:20 25-07-2022
# *****************************************************************************
# -----------------------------------------------------------------------------

# descripcion del programa

# Librerias
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

# plt.style.use('band_structure')
plt.style.use('density_of_states')

# *****************************************************************************
# INICIO
# *****************************************************************************
sustancia = r'$\mathrm{MgO}$'
funcional = ''
nombre_grafica = os.path.basename(__file__).replace(".py", ".pdf")

#
# --- GRAFICA ---
#
xmin = 0
xmax = 0.007
ymin = 0
ymax = 700
#
fig, ax = plt.subplots()
fig.subplots_adjust(left=.15, bottom=.16, right=.99, top=.97)
#
# --- BUSH ---
#
fichero_datos = './Bush_1994/DOS.dens'
y, x = np.loadtxt(fichero_datos, unpack=True, skiprows=2)
ax.plot(x,y, label=r'Bush 1994')
#
ax.set(title=r'Density of States'+' '+sustancia+' '+funcional,
       ylabel=r'Frequency, $\nu\ (\mathrm{cm^{-1}})$',
       xlabel=r'PDOS (electrons/eV)')
ax.set_xlim(xmin,xmax)
ax.set_ylim(ymin,ymax)
ax.legend()
#
plt.savefig(nombre_grafica, transparent='True', bbox_inches='tight')
# plt.show()
