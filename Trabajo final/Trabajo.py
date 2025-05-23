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
import seaborn as sns
import matplotlib.pyplot as plt

os.chdir(r"C:\Users\Luis José López\Documents\7-Maestría\PUC\Semestre 4\Machine-Learning\Trabajo final")
print(os.getcwd())

""" 
Nota:
    
Los CSV Rendimiento 2024, Rendimiento 2023, Rendimiento 2022, 
Rendimiento 2021, Rendimiento 2020, Preferencia 2024, Preferencia 2023, 
Preferencia 2022, Preferencia 2021, Preferencia 2020, Docentes 2024, 
Docentes 2023, Docentes 2022, Docentes 2021 y Docentes 2020 son los archivos 
originales publicados por MINEDUC (sacados de las carpetas zip) desde su 
página web (https://datosabiertos.mineduc.cl/) para los años correspondientes.
"""

""" ######################### Limpieza y carga ########################## """
""" 2024 """
%clear
%reset -f
!cls 
import pandas as pd
import os
os.chdir(r"C:\Users\Luis José López\Documents\7-Maestría\PUC\Semestre 4\Machine-Learning\Trabajo final")
df = pd.read_csv(r"C:\Users\Luis José López\Documents\7-Maestría\PUC\Semestre 4\Machine-Learning\Trabajo final\Rendimiento 2024.csv" , sep=';')

df5 = df5[~df5['COD_ENSE'].isin([110, 165, 167, 211, 212, 213, 214, 215, 216, 217, 218, 219, 299])]

df5['COD_ENSE'].value_counts()

df5 = df5[df5['COD_GRADO'].isin([3, 4])]

df5['COD_GRADO'].value_counts()

df5.to_csv('2024.csv', index=False)

#merge con preferentes y docentes

""" 2023 """
%clear
%reset -f
!cls 
import pandas as pd
import os
os.chdir(r"C:\Users\Luis José López\Documents\7-Maestría\PUC\Semestre 4\Machine-Learning\Trabajo final")
df4 = pd.read_csv(r"C:\Users\Luis José López\Documents\7-Maestría\PUC\Semestre 4\Machine-Learning\Trabajo final\Rendimiento_2023.csv" , sep=';')

df4 = df4[~df4['COD_ENSE'].isin([110, 165, 167, 211, 212, 213, 214, 215, 216, 217, 218, 219, 299])]

df4['COD_ENSE'].value_counts()

df4 = df4[df4['COD_GRADO'].isin([3, 4])]

df4['COD_GRADO'].value_counts()

df4.to_csv('2023.csv', index=False)

#merge con preferentes y docentes

""" 2022 """
%clear
%reset -f
!cls 
import pandas as pd
import os
os.chdir(r"C:\Users\Luis José López\Documents\7-Maestría\PUC\Semestre 4\Machine-Learning\Trabajo final")
df3 = pd.read_csv(r"C:\Users\Luis José López\Documents\7-Maestría\PUC\Semestre 4\Machine-Learning\Trabajo final\Rendimiento_2022.csv" , sep=';')

df3 = df3[~df3['COD_ENSE'].isin([110, 165, 167, 211, 212, 213, 214, 215, 216, 217, 218, 219, 299])]

df3['COD_ENSE'].value_counts()

df3 = df3[df3['COD_GRADO'].isin([3, 4])]

df3['COD_GRADO'].value_counts()

df3.to_csv('2022.csv', index=False)

#merge con preferentes y docentes

""" 2021 """
%clear
%reset -f
!cls 
import pandas as pd
import os
os.chdir(r"C:\Users\Luis José López\Documents\7-Maestría\PUC\Semestre 4\Machine-Learning\Trabajo final")
df2 = pd.read_csv(r"C:\Users\Luis José López\Documents\7-Maestría\PUC\Semestre 4\Machine-Learning\Trabajo final\Rendimiento_2021.csv" , sep=';')

df2 = df2[~df2['COD_ENSE'].isin([110, 165, 167, 211, 212, 213, 214, 215, 216, 217, 218, 219, 299])]

df2['COD_ENSE'].value_counts()

df2 = df2[df2['COD_GRADO'].isin([3, 4])]

df2['COD_GRADO'].value_counts()

df2.to_csv('2021.csv', index=False)

#merge con preferentes y docentes

""" 2020 """
%clear
%reset -f
!cls 
import pandas as pd
import os
os.chdir(r"C:\Users\Luis José López\Documents\7-Maestría\PUC\Semestre 4\Machine-Learning\Trabajo final")
df1 = pd.read_csv(r"C:\Users\Luis José López\Documents\7-Maestría\PUC\Semestre 4\Machine-Learning\Trabajo final\Rendimiento_2020.csv" , sep=';')

df1 = df1[~df1['COD_ENSE'].isin([110, 165, 167, 211, 212, 213, 214, 215, 216, 217, 218, 219, 299])]

df1['COD_ENSE'].value_counts()

df1 = df1[df1['COD_GRADO'].isin([3, 4])]

df1['COD_GRADO'].value_counts()

df1.to_csv('2020.csv', index=False)

""" 2019 """
%clear
%reset -f
!cls 
import pandas as pd
import os
os.chdir(r"C:\Users\Luis José López\Documents\7-Maestría\PUC\Semestre 4\Machine-Learning\Trabajo final")
df1 = pd.read_csv(r"C:\Users\Luis José López\Documents\7-Maestría\PUC\Semestre 4\Machine-Learning\Trabajo final\Rendimiento_2019.csv" , sep=';')

df1 = df1[~df1['COD_ENSE'].isin([110, 165, 167, 211, 212, 213, 214, 215, 216, 217, 218, 219, 299])]

df1['COD_ENSE'].value_counts()

df1 = df1[df1['COD_GRADO'].isin([3, 4])]

df1['COD_GRADO'].value_counts()

df1.to_csv('2019.csv', index=False)

""" 2018 """
%clear
%reset -f
!cls 
import pandas as pd
import os
os.chdir(r"C:\Users\Luis José López\Documents\7-Maestría\PUC\Semestre 4\Machine-Learning\Trabajo final")
df1 = pd.read_csv(r"C:\Users\Luis José López\Documents\7-Maestría\PUC\Semestre 4\Machine-Learning\Trabajo final\Rendimiento_2018.csv" , sep=';')

df1 = df1[~df1['COD_ENSE'].isin([110, 165, 167, 211, 212, 213, 214, 215, 216, 217, 218, 219, 299])]

df1['COD_ENSE'].value_counts()

df1 = df1[df1['COD_GRADO'].isin([3, 4])]

df1['COD_GRADO'].value_counts()

df1.to_csv('2018.csv', index=False)

""" 2017 """
%clear
%reset -f
!cls 
import pandas as pd
import os
os.chdir(r"C:\Users\Luis José López\Documents\7-Maestría\PUC\Semestre 4\Machine-Learning\Trabajo final")
df1 = pd.read_csv(r"C:\Users\Luis José López\Documents\7-Maestría\PUC\Semestre 4\Machine-Learning\Trabajo final\Rendimiento_2017.csv" , sep=';')

df1 = df1[~df1['cod_ense'].isin([110, 165, 167, 211, 212, 213, 214, 215, 216, 217, 218, 219, 299])]

df1['cod_ense'].value_counts()

df1 = df1[df1['cod_ense'].isin([3, 4])]

df1['cod_ense'].value_counts()

df1.to_csv('2017.csv', index=False)

#merge con preferentes y docentes

""" ######################### Unir bases ########################## """
df1 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2020.csv')
df2 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2021.csv')
df3 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2022.csv')
df4 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2023.csv') 
df5 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2024.csv')
df6 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2019.csv')
df7 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2018.csv')
df8 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2017.csv')

df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8], ignore_index=True) 

del df1 
del df2 
del df3
del df4
del df5
del df6 
del df7
del df8

""" ################ Análisis exploratorio de datos ####################### """
df.head()

#Box plot para ver desertores, aprobados y reprobados
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

#Evaluamos si categoría en blanco es desertor o no

#Reeemplazar variables string por númericas

#Verificar y elminar outliers

#Estandarizar/Normalizar variables

#Balancear set de entrenamiento 


""" ##################### Modelo 1 ####################### """

""" ##################### Modelo 2 ####################### """

""" ##################### Modelo 3 ####################### """

""" ################# Muestra aleatoria ################## """

