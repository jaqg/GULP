# Argon #

El Argon se encuentra en fase gas naturalmente a temperatura ambiente (22 grados Celsius), encontrando su punto triple a 83.80 K y 68.89 kPa. Es un gas noble, comunmente usado en iluminación o aplicaciones de almacenamiento [Seminario Dinámica Molecular - Vicente Timón].

![Ar](https://github.com/jaqg/GULP/blob/main/Proyectos/Ejercicios_Vicente/Ar/N%3D64/T%3D60K/TS%3D1fs/Ar_rho%3D0.0207125_N%3D64_cubic_60.png "Ar")

Llevamos a cabo cálculos de dinámica molecular, en las siguientes condiciones:

## Cálculos ##

### Sistema 1 con $\boldsymbol{N_1=64}$ átomos ###

- Tiempo (aproximado) de cómputo para $T=60\ \mathrm{K},\ \delta t = 1\ \mathrm{fs}$: **7.8 s**

    #### Para $\boldsymbol{T=60\ \mathrm{K}}$ ####

    - $\delta t = 0.1\ \mathrm{fs} \implies$ [Ar_rho=0.0207125_N=64_cubic_60_TS=01.gin](https://github.com/jaqg/GULP/blob/main/Proyectos/Ejercicios_Vicente/Ar/N%3D64/T%3D60K/TS%3D0.1fs/Ar_rho%3D0.0207125_N%3D64_cubic_60_TS%3D01.gin)
    - $\delta t = 1\ \mathrm{fs} \implies$ [Ar_rho=0.0207125_N=64_cubic_60.gin](https://github.com/jaqg/GULP/blob/main/Proyectos/Ejercicios_Vicente/Ar/N%3D64/T%3D60K/TS%3D1fs/Ar_rho%3D0.0207125_N%3D64_cubic_60.gin)
    - $\delta t = 10\ \mathrm{fs} \implies$ [Ar_rho=0.0207125_N=64_cubic_60_TS=10.gin](https://github.com/jaqg/GULP/blob/main/Proyectos/Ejercicios_Vicente/Ar/N%3D64/T%3D60K/TS%3D10fs/Ar_rho%3D0.0207125_N%3D64_cubic_60_TS%3D10.gin)

    #### Para $\boldsymbol{T=298\ \mathrm{K}}$ ####

    - $\delta t = 1\ \mathrm{fs} \implies$ [Ar_rho=0.0207125_N=64_cubic_298.gin](https://github.com/jaqg/GULP/blob/main/Proyectos/Ejercicios_Vicente/Ar/N%3D64/T%3D298K/TS%3D1fs/Ar_rho%3D0.0207125_N%3D64_cubic_298.gin)


    #### Para el **Punto Triple**: $\boldsymbol{T=83.80\ \mathrm{K}}$ y $\boldsymbol{P=68.89\ \mathrm{kPa}}$ ####

    - $\delta t = 1\ \mathrm{fs} \implies$ [Ar_rho=0.0207125_N=64_cubic_TP.gin](https://github.com/jaqg/GULP/blob/main/Proyectos/Ejercicios_Vicente/Ar/N%3D64/Punto_triple/TS%3D1fs/Ar_rho%3D0.0207125_N%3D64_cubic_TP.gin)

### Sistema 2 con $\boldsymbol{N_2=512}$ átomos ###

- Tiempo (aproximado) de cómputo para $T=60\ \mathrm{K},\ \delta t = 1\ \mathrm{fs}$: **211.5 s (3.5 min)**

    #### Para $\boldsymbol{T=60\ \mathrm{K}}$ ####

    - $\delta t = 1\ \mathrm{fs} \implies$ [Ar_rho=0.0207125_N=512_cubic_60.gin](https://github.com/jaqg/GULP/blob/main/Proyectos/Ejercicios_Vicente/Ar/N%3D512/T%3D60K/TS%3D1fs/Ar_rho%3D0.0207125_N%3D512_cubic_60.gin)

    #### Para $\boldsymbol{T=298\ \mathrm{K}}$ ####

    - $\delta t = 1\ \mathrm{fs} \implies$ [Ar_rho=0.0207125_N=64_cubic_298.gin](https://github.com/jaqg/GULP/blob/main/Proyectos/Ejercicios_Vicente/Ar/N%3D512/T%3D298K/TS%3D1fs/Ar_rho%3D0.0207125_N%3D512_cubic_298.gin)

    - $\delta t = 10\ \mathrm{fs} \implies$ [Ar_rho=0.0207125_N=64_cubic_298_TS=10.gin](https://github.com/jaqg/GULP/blob/main/Proyectos/Ejercicios_Vicente/Ar/N%3D512/T%3D298K/TS%3D10fs/Ar_rho%3D0.0207125_N%3D512_cubic_298_TS%3D10.gin)

## Cuestiones ##

- ¿Importa el tamaño del sistema?

    Sí, principalmente en el tiempo de cómputo. El tiempo de computación para el sistema 2 con $N_2=512$ átomos (8 veces más átomos que en el sistema 1, con $N_1=64$ átomos) es de $t_{c}^{(2)}=211.5\ \mathrm{s}$, mientras que para el sistema 1 es de $t_{c}^{(1)}=7.8\ \mathrm{s}$, de manera que $t_{c}^{(2)}/t_{c}^{(1)} = 27.12$. El tiempo de cómputo del sistema 2, con 8 veces el número de átomos del sistema 1, es $\approx 27$ veces el tiempo de cómputo del sistema 1.

- ¿Cambia la temperatura el comportamiento del sistema?

    Sí. Podemos apreciar perfectamente cómo, al aumentar la temperatura, aumenta la velocidad media de los átomos de Ar, habiendo un mayor número de átomos que entran y salen de la celda de simulación en el tiempo de duración de la misma.

- Si has probado diferentes valores de incremento de tiempo $\delta t$ (*timesteps*), ¿puedes emplear distintos valores minimizando la pérdida de precisión?

    Sí, he realizado los cálculos para $\delta t = 0.1,1,10\ \mathrm{fs}$. A la vista de los resultados, podemos incrementar el valor de $\delta t$ por encima de $0.1\ \mathrm{fs}$, ya que no perdemos mucha precisión con respecto a $1\ \mathrm{fs}$. Por encima de $1\ \mathrm{fs}$ sí empezamos a perder precisión, comenzando a ser apreciable a partir de $10\ \mathrm{fs}$. Por tanto, para este caso, considero que el valor indicado es de $\delta t = 1\ \mathrm{fs}$, puediendo incrementar este valor hasta $\delta t = 10\ \mathrm{fs}$ si se requiere unn tiempo de cómputo menor, aunque de por sí el cálculo debe tomar menos de 1 minuto para $\delta t = 1\ \mathrm{fs}$.
