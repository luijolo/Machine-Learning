# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 17:53:56 2025

@author: Luis José López
"""
%reset -f
%clear 
import os
import pandas as pd
os.chdir(r"C:\Users\Luis José López\Documents\7-Maestría\PUC\Semestre 4\Machine-Learning\Trabajo final")
print(os.getcwd())

""" ############################# 2024 ############################# """
df = pd.read_csv(r"C:\Users\Luis José López\Documents\7-Maestría\PUC\Semestre 4\Machine-Learning\Trabajo final\Rendimiento 2024.csv" , sep=';')

df = df[~df['COD_ENSE'].isin([110, 165, 167, 211, 212, 213, 214, 215, 216, 217, 218, 219, 299])]

df['COD_ENSE'].value_counts()

df = df[df['COD_GRADO'].isin([3, 4])]

df['COD_GRADO'].value_counts()

df.to_csv('2024.csv', index=False)

#merge con preferentes y docentes

""" ############################# 2023 ############################# """
df = pd.read_csv(r"C:\Users\Luis José López\Documents\7-Maestría\PUC\Semestre 4\Machine-Learning\Trabajo final\Rendimiento_2023.csv" , sep=';')

df = df[~df['COD_ENSE'].isin([110, 165, 167, 211, 212, 213, 214, 215, 216, 217, 218, 219, 299])]

df['COD_ENSE'].value_counts()

df = df[df['COD_GRADO'].isin([3, 4])]

df['COD_GRADO'].value_counts()

df.to_csv('2023.csv', index=False)

#merge con preferentes y docentes

""" ############################# 2022 ############################# """
df = pd.read_csv(r"C:\Users\Luis José López\Documents\7-Maestría\PUC\Semestre 4\Machine-Learning\Trabajo final\Rendimiento_2022.csv" , sep=';')

df = df[~df['COD_ENSE'].isin([110, 165, 167, 211, 212, 213, 214, 215, 216, 217, 218, 219, 299])]

df['COD_ENSE'].value_counts()

df = df[df['COD_GRADO'].isin([3, 4])]

df['COD_GRADO'].value_counts()

df.to_csv('2022.csv', index=False)

#merge con preferentes y docentes

""" ############################# 2021 ############################# """
df = pd.read_csv(r"C:\Users\Luis José López\Documents\7-Maestría\PUC\Semestre 4\Machine-Learning\Trabajo final\Rendimiento_2021.csv" , sep=';')

df = df[~df['COD_ENSE'].isin([110, 165, 167, 211, 212, 213, 214, 215, 216, 217, 218, 219, 299])]

df['COD_ENSE'].value_counts()

df = df[df['COD_GRADO'].isin([3, 4])]

df['COD_GRADO'].value_counts()

df.to_csv('2021.csv', index=False)

#merge con preferentes y docentes

""" ############################# 2020 ############################# """
df = pd.read_csv(r"C:\Users\Luis José López\Documents\7-Maestría\PUC\Semestre 4\Machine-Learning\Trabajo final\Rendimiento_2020.csv" , sep=';')

df = df[~df['COD_ENSE'].isin([110, 165, 167, 211, 212, 213, 214, 215, 216, 217, 218, 219, 299])]

df['COD_ENSE'].value_counts()

df = df[df['COD_GRADO'].isin([3, 4])]

df['COD_GRADO'].value_counts()

df.to_csv('2020.csv', index=False)

#merge con preferentes y docentes

""" ######################### Unir bases ########################## """
df1 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2020.csv')
df2 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2021.csv')
df3 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2022.csv')
df4 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2023.csv') 
df5 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2024.csv')

df = pd.concat([df1, df2, df3, df4, df5], ignore_index=True) 

df.to_csv('datafinal.csv', index=False)

df = pd.read_csv('datafinal.csv')