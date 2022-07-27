# GULP Input Files Cheatsheet  (.gin) #

## Estructura del fichero ##

### Keyword line ###

Ejemplo:
```
optimise conp properties phonon
```
o, de manera abreviada, como suele aparecer en los ficheros (empleando
sólo las primeras cuatro letras)
```
opti conp prop phon
```
donde:
- `opti` (optimise): optimización de geometría
- `conp`: *constant pressure*
    - Las variables que comienzan con *con-* son referidas a
        *constant-*, por ejemplo, *conp* (constant pressure), *conv* (constant volume), etc.
- `prop` (properties): calcula las propiedades de red (*lattice properties*) en la geometría optimizada
- `phon` (phonon): calcula los fonones en la geometría optimizada
- **Nota:** el orden de las palabras en la *keyword line* no afecta al
    cálculo.






Mg core 0.0 0.0 0.0 2.00000 1.0 0.0 0 0 0

Estructura:
Átomo (símbolo del elemento): Mg

### Options ###

Las siguientes líneas contienen las **opciones** o más información.

Por ejemplo, la presión a aplicar sobre la estructura:
```
# La presión es:
pressure 10.0 kbar
```
- Las opciones se aplican sobre la última estructura que ha sido creada
- Algunas opciones deben ser especificadas como subsecciones de una opción
    particular. Por ejemplo: `elastic, sdlc, hfdlc, piezo, energy` y
    `gradients` son subsecciones del comando `observables`
- **Nota:** Los comentarios comienzan con `#`

### Átomos ###

- Los átomos son etiquetados con el símbolo del elemento químico que representan.
- Opcionalmente, se puede especificar el tipo de especie:
    - `core` (default): representa la parte principal de un átomo incluyendo
        toda su masa
    - `shel`: representa la componente sin masa (*mass-less*) en un
        modelo *shell*
    - `bcor`: a core, but with a spherical breathing radius
    - `bshe`: a shell, but with a spherical breathing radius
- Se pueden numerar átomos, por ejemplo como `Si1, Si2, ...`, pudiendo
    aplicar un potencial sobre cada uno de ellos. Por ejemplo,
    aplicando un potencial de Buckingham sobre el átomo `Si1` como
    ```
    buck
    Si1 core O core 1283.0 0.299 10.66 0.0 12.0
    ```
    mientras que, además, podemos aplicar el potencial a todos los átomos de
    un mismo elemento, aunque tengan etiquetas distintas. Por ejemplo,
    podemos aplicar un potencial de Buckingham sobre todos los átomos de
    silicio (`Si1, Si2, ...`) escribiendo el símbolo del elemento (`Si`)
    ```
    buck
    Si core O core 1283.0 0.299 10.66 0.0 12.0
    ```

### Estructura ###

Tenemos que especificar:
- La celda unidad
- Las coordenadas fraccionarias y los tipos de átomos que la componen
- El grupo espacial de simetría

#### Celdilla unidad ####

Por ejemplo:
```
cell
4.212 4.212 4.212 90.0 90.0 90.0
```

donde estamos especificando los parámetros de la celdilla unidad: $a = b
= c = 4.212\ \mathrm{\AA}$ y $\alpha = \beta = \gamma = 90^{\circ}$.
Si no especificamos las palabras clave `conp` o `conv`, debemos de
indicar 6 banderas para indicar cómo debe ser optimizada la celdilla
unidad, donde
- `1`: indica que un grado de libertad debería estar permitido que
    varíe
- `0`: implica que debería mantenerse fijo

Estas banderas se refieren a los componentes de la presión en el orden $xx$,
$yy$, $zz$, $yz$, $xz$ y $xy$, respectivamente. Por ejemplo, sobre el
ejemplo anterior
```
cell
4.212 4.212 4.212 90.0 90.0 90.0 1 1 1 0 0 0
```
sólo las componentes de la diagonal pueden variar.

#### Coordenadas de los átomos ####

Escribimos el símbolo del átomo, el tipo de especie y las coordenadas
fraccionarias. Por ejemplo:
```
fractional
Mg core 0.0 0.0 0.0
O core 0.5 0.5 0.5
O shel 0.5 0.5 0.5
```
donde hemos incluido un modelo *shell* para el oxígeno.
- **Nota:** en caso de que la coordenada sea fraccionaria, como $a=1/3$,
    deberemos especificar 6 decimales, es decir, $a=0.333333$

Además, podemos especificar parámetros opcionales que siguen la coordenada
$z$. Por ejemplo:
```
fractional
Mg core 0.0 0.0 0.0 2.00000 1.0 0.0 0 0 0
```
donde
- `0.0 0.0 0.0`: Fractional coordinates
- `2.00000`: Charge
- `1.0`: Site occupancy (default 1.0)
- `0.0`: Ion radius for a breathing shell model (default 0.0)
- `0 0 0`: 3 flags to identify geometric variables
    - `1`$\implies$ vary
    - `0`$\implies$fix

#### Grupo espacial de simetría ####

Se puede especificar con el número de grupo
```
space
225
```
o con el símbolo estándar de Hermann-Mauguin (**recomendado**)
```
space
F M 3 M
```
- **Nota:** el *help file* contiene la lista completa de los símbolos de
    cada grupo espacial

Podemos crear varias estructuras y etiquetarlas con el comando
`name`, cuyo argumento es una sola palabra, precediendo la declaración de
la estrucura:
```
name corundum
cell
4.7602 4.7602 12.9933 90.0 90.0 120.0
frac
Al core 0.00000 0.0 0.35216
O core 0.30624 0.0 0.00000
space
167
name quartz
cell
4.91485 4.91485 5.40629 90.0 90.0 120.0
frac
Si core 0.4682 0.0000 0.333333
O core 0.4131 0.2661 0.213100
```
Para usar la misma estructura a dos condiciones distintas, usamos el
comando `ditto`. Por ejemplo, para realizar los cálculos sobre el
corundo a 1 GPa y 2 GPa escribimos:
```
name corundum
cell
4.7602 4.7602 12.9933 90.0 90.0 120.0
frac
Al core 0.00000 0.0 0.35216
O core 0.30624 0.0 0.00000
space
167
pressure 1 GPa
ditto structure
pressure 2 GPa
```

### Species/libraries ###

Podemos especificar la carga de cada átomo individual con la opción
`species`. Por ejemplo, para una zeolita:
```
species
Si core 4.00000
O core 0.86902
O shel -2.86902
```

Podemos usar el comando `library` para especificar una de las librerias que
contienen los potenciales. Encontramos dos:
- `catlow.lib`: para los sistemas del tipo zeolita o
    aluminofosfatos
- `bush.lib`: para óxidos metálicos del trabajo de Bush et al

Ejemplo:
```
species
Si core Si
O core O_O2-
O shel O_O2-
library catlow.lib
```
- **Nota:** especificamos los símbolos de un elemento no estándar con
    `_`. Por ejemplo, especificamos el oxígeno del grupo hidroxilo
    como `O_Oh`.

### Input of potentials ###

El formato de entrada de cada potencial puede encontrarse en el *on-line
help*.

Por ejemplo, para aplicar un optencial de Buckingham entre cores de
magnesio y shells de oxígeno con parámetros $\mathrm{A} = 1280.0\
\mathrm{eV}$, $\rho = 0.300\
\mathrm{\AA}$, $\mathrm{C} = 0.300\
\mathrm{eV\AA^6}$ en el rango de $0$ a $12\ \mathrm{\AA}$:
```
buck
Mg core O shel 1280.0 0.3 4.5 0.0 12.0
```

Podemos hacer que varíe (`1`) o que no lo haga (`0`) cada parámetro del
potencial, especificándolo tras estos. Por ejemplo, para que varíe el
parámetro $\mathrm{A}$:
```
buck
Mg core O shel 1280.0 0.3 4.5 0.0 12.0 1 0 0
```

El número de parámetros de entrada puede variar dependiendo de las
opciones aplicadas sobre el tipo de potencial. Por ejemplo, si queremos
que el potencial anterior actúe sobre los átomos que están enlazados:
```
buck bond
Mg core O shel 1280.0 0.3 4.5
```
Para algunos tipos de potencial (como algunos *three-body* y todos los
*four-body*) es importante el orden de los átomos, que deberemos de
comprobar.
- **Nota:** para continuar en otra línea, debemos incluir el carácter `&`.

#### Input of PDF settings ####
Incluimos los parámetros de entrada en el cálculo de Pairs Distribution Functions (PDF) en un entorno `pdf`:
```
pdf
    rmax [real]
    rbins [int]
    units freq [rad/Thz/cm/wav/meV]
    wmin [real] (or wxmax [real])
end
```
donde deben ser especificados
- `rmax`: el radio máximo en $\mathrm{\AA}$ (default $5\ \mathrm{\AA}$)
- `rbins`: el número de *bins* usados para el output
y podemos, opcionalmente, incluir
- `units freq`: cambiar las unidades de la frecuencia de THz (default) a
    otra unidad
- `wmin` (or `wmax`): al usar la *frequency cut-off facility*

### Defects ###

Primero que todo, deberemos incluir la opción `defect` en la *keyword line*
si pensamos incluir un defecto en nuestra celda unidad de estudio.

Determinamos el *defect centre* con la opción `centre` (o, también,
`center`). Podemos determinar la localización del defecto según:
- Atom symbol
```
centre Mg2 core
```
- Atom number: número del átomo en la unidad asimétrica como input
```
centre 3
```
- Fractional coordinates: la posición viene dada en unidades fraccionarias

```
centre frac 0.25 0.25 0.25
```
- Cartesian coordinates
```
centre cart 1.5 2.4 0.8
```
- Molecule number: defecto en el medio de la molécula indicada
```
centre mol 2
```

Especificamos la región 1 y la región 2a radii con el comando `size`:
```
size 4.0 10.0
```
donde:
- `4.0`: region 1 radius ($\mathrm{\AA}$)
- `10.0`: region 2a radius ($\mathrm{\AA}$)

Ahora, podemos crear el defecto que nos interese. Hay 3 opciones:
- `vacancy`: removes an ion from the structure to infinity
- `interstitial`: inserts an ion into the structure from infinity
- `impurity`: replaces one ion with a different one

Debemos especificar el tipo de especie que es insertada. Por ejemplo,
podemos reemplazar `O2` con `S` con el comando `impurity`, según
```
impurity S O2
```
donde primero incluimos la especie a insertar, y a continuación,
la especie a sustituir.

También podemos introducir un defecto intersticial. Por ejemplo,
podemos protonar un oxígeno para generar un grupo hidroxilo en el `O2`
escribiendo
```
interstitial H bond O2
```
lo que colocará el `H` en la estructura a una distancia igual al radio
covalente del `O2`.

Con esto, podemos crear una impureza de litio en el óxido de magnesio para
generar un defecto cargado negativamente. La parte del input referente a la
estructura es
```
opti conp defect
cell
4.212 4.212 4.212 90.0 90.0 90.0
frac
Mg core 0.0 0.0 0.0
Mg core 0.0 0.5 0.5
Mg1 core 0.5 0.0 0.5
Mg core 0.5 0.5 0.0
O core 0.5 0.5 0.5
O core 0.5 0.0 0.0
O core 0.0 0.5 0.0
O core 0.0 0.0 0.5
species
Mg core 2.0
O core -2.0
Li core 1.0
```
Podemos crear el defecto escribiendo, por ejemplo:
```
centre Mg1
size 6.0 12.0
vacancy Mg1
interstitial Li 0.5 0.0 0.5
```

### Restarting jobs ###

Automaticamente se escribe un archivo `dump`, en caso de que se tenga que
reiniciar el cálculo, similar al archivo input. Podemos cambiar la
frecuencia con la que este archivo `dump` es generado con
```
dump every 4 gulp.res
```
donde dicho archivo se generaría cada 4 ciclos (default 1).

### Keywords ###

Podemos consultar las *keywords* en la página 149 (en adelante) del
manual.

## Output ##

Hay una guía sobre el fichero de salida a partir de la página 163 del
manual.
