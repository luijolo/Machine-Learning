"""
Created on Mon Apr 14 19:05:30 2025

@author: Luis José López
"""
""" Inicio """
%clear
%reset -f
!cls 

import os
import pandas as pd
os.chdir(r"C:\Users\Luis José López\Documents\7-Maestría\PUC\Semestre 4\Machine-Learning\Trabajo final")
print(os.getcwd())

""" Inicio """
df1 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2020.csv')
df2 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2021.csv')
df3 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2022.csv')
df4 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2023.csv') 
df5 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2024.csv')

df = pd.concat([df1, df2, df3, df4, df5], ignore_index=True) 

del df1 
del df2 
del df3
del df4
del df5

""" Análisis exploratorio de datos """
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df.head()

ax = sns.countplot(x='SIT_FIN_R', data=df, palette='hls')
for p in ax.patches:
    count = int(p.get_height())
    ax.annotate(count,                       
        (p.get_x() + p.get_width() / 2., p.get_height()),  
        ha='center', va='bottom',       
        fontsize=10, color='black',     
        xytext=(0, 3), textcoords='offset points'  
    )

plt.show()

""" Modelo 1  """

""" Modelo 2  """

""" Visualizaciones  """