#! /bin/bash
# |-------------------------------------------------|
# | Autor: José Antonio Quiñonero Gris              |
# | Fecha de creacion: Wednesday 17:38:53 27-07-2022 |
# |_________________________________________________|
# Script name: exec
# Description: ejecutable para cálculo de GULP

file_name='MgO'

rm -f $file_name.got
gulp < $file_name.gin > $file_name.got
echo "Cálculo GULP terminado con éxito"
