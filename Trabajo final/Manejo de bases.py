# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 17:53:56 2025

@author: Luis José López
"""
import os
import pandas as pd
os.chdir(r"C:\Users\Luis José López\Documents\7-Maestría\PUC\Semestre 4\Machine-Learning\Trabajo final")
print(os.getcwd())

""" 2024 """
df = pd.read_csv(r"C:\Users\Luis José López\Documents\7-Maestría\PUC\Semestre 4\Machine-Learning\Trabajo final\Rendimiento 2024.csv" , sep=';')

df = df[~df['COD_ENSE'].isin([110, 165, 167, 211, 212, 213, 214, 215, 216, 217, 218, 219, 299])]

df['COD_ENSE'].value_counts()

df = df[df['COD_GRADO'].isin([3, 4])]

df['COD_GRADO'].value_counts()

df.to_csv('2024.csv', index=False)
