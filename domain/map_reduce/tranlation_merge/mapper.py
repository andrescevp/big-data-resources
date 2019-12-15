#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # Limpiamos espacions, buscamos el tabulador y separamos en 2 elementos (tupla)
    terms = line.strip().split('\t')
    # Volcamos la salida por consola
    print('\t'.join(terms))
