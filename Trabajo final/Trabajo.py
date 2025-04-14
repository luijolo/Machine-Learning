# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 19:05:30 2025

@author: Luis José López
"""
""" Iniciar seteando directorio y uniendo bases """
%clear

import os
import pandas as pd
os.chdir(r"C:\Users\Luis José López\Documents\7-Maestría\PUC\Semestre 4\Machine-Learning\Trabajo final")
print(os.getcwd())

df1 = pd.read_csv('2021.csv')
df2 = pd.read_csv('2021.csv')
df3 = pd.read_csv('2022.csv')
df4 = pd.read_csv('2023.csv') 
df5 = pd.read_csv('2024.csv')

df = pd.concat([df1, df2, df3, df4, df5], ignore_index=True)

""" Análisis exploratorio de datos """

""" Modelo 1  """

""" Modelo 2  """

""" Visualizaciones  """