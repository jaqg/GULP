#! /bin/bash
# |-------------------------------------------------|
# | Autor: José Antonio Quiñonero Gris              |
# | Fecha de creacion: Sunday 22:13:48 24-07-2022   |
# |_________________________________________________|
# Script name: exec
# Description: ejecutable para cálculo de GULP

file_name='Si'

rm -f $file_name.got
gulp < $file_name.gin > $file_name.got
echo "Cálculo GULP terminado con éxito"
