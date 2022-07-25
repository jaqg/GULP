#! /bin/bash
# |-------------------------------------------------|
# | Autor: José Antonio Quiñonero Gris              |
# | Fecha de creacion: Monday 19:07:25 25-07-2022 |
# |_________________________________________________|
# Script name: exec
# Description: ejecutable para cálculo de GULP

file_name='Al'

rm -f $file_name.got
gulp < $file_name.gin > $file_name.got
echo "Cálculo GULP terminado con éxito"
