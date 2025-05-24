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
Rendimiento 2021, Rendimiento 2020, Rendimiento 2019, Rendimiento 2018, 
Rendimiento 2017, PPB 2024, PPB 2023, PPB 2022, PPB 2021, PPB 2020, PPB 2019,
PPB 2018, PPB 2017 son los archivos originales publicados por MINEDUC 
(sacados de las carpetas zip) desde su página web 
(https://datosabiertos.mineduc.cl/) para los años correspondientes.
"""

""" ######################### Limpieza y carga ########################## """
""" 2024 """
df5 = pd.read_csv(r"C:\Users\Luis José López\Documents\7-Maestría\PUC\Semestre 4\Machine-Learning\Trabajo final\Rendimiento 2024.csv" , sep=';')

df5 = df5[~df5['COD_ENSE'].isin([110, 165, 167, 211, 212, 213, 214, 215, 216, 217, 218, 219, 299])]

df5['COD_ENSE'].value_counts()

df5 = df5[df5['COD_GRADO'].isin([3, 4])]

df5['COD_GRADO'].value_counts()

df5.to_csv('2024.csv', index=False)

#Preferenciales
df2 = pd.read_csv(r"C:\Users\Luis José López\Documents\7-Maestría\PUC\Semestre 4\Machine-Learning\Trabajo final\PPB_2024.csv" , sep=';')

df2 = df2[df2['COD_ENSE'] != ' ']
df2['COD_ENSE'] = df2['COD_ENSE'].astype(int)
df2 = df2[df2['COD_ENSE'].isin([310, 410, 510, 610, 710, 810, 910])]
df2['COD_ENSE'].value_counts()

df2 = df2[df2['COD_GRADO'] != ' ']
df2['COD_GRADO'] = df2['COD_GRADO'].astype(int)
df2 = df2[df2['COD_GRADO'].isin([3, 4])]
df2['COD_GRADO'].value_counts()

df2.to_csv('2024_SEP.csv', index=False)

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

#Preferenciales
df2 = pd.read_csv(r"C:\Users\Luis José López\Documents\7-Maestría\PUC\Semestre 4\Machine-Learning\Trabajo final\PPB_2023.csv" , sep=';')

df2 = df2[df2['COD_ENSE'] != ' ']
df2['COD_ENSE'] = df2['COD_ENSE'].astype(int)
df2 = df2[df2['COD_ENSE'].isin([310, 410, 510, 610, 710, 810, 910])]
df2['COD_ENSE'].value_counts()

df2 = df2[df2['COD_GRADO'] != ' ']
df2['COD_GRADO'] = df2['COD_GRADO'].astype(int)
df2 = df2[df2['COD_GRADO'].isin([3, 4])]
df2['COD_GRADO'].value_counts()

df2.to_csv('2023_SEP.csv', index=False)

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

#Preferenciales
df2 = pd.read_csv(r"C:\Users\Luis José López\Documents\7-Maestría\PUC\Semestre 4\Machine-Learning\Trabajo final\PPB_2022.csv" , sep=';')

df2 = df2[df2['COD_ENSE'] != ' ']
df2['COD_ENSE'] = df2['COD_ENSE'].astype(int)
df2 = df2[df2['COD_ENSE'].isin([310, 410, 510, 610, 710, 810, 910])]
df2['COD_ENSE'].value_counts()

df2 = df2[df2['COD_GRADO'] != ' ']
df2['COD_GRADO'] = df2['COD_GRADO'].astype(int)
df2 = df2[df2['COD_GRADO'].isin([3, 4])]
df2['COD_GRADO'].value_counts()

df2.to_csv('2022_SEP.csv', index=False)

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

#Preferenciales
df2 = pd.read_csv(r"C:\Users\Luis José López\Documents\7-Maestría\PUC\Semestre 4\Machine-Learning\Trabajo final\PPB_2021.csv" , sep=';')

df2 = df2[df2['COD_ENSE'] != ' ']
df2['COD_ENSE'] = df2['COD_ENSE'].astype(int)
df2 = df2[df2['COD_ENSE'].isin([310, 410, 510, 610, 710, 810, 910])]
df2['COD_ENSE'].value_counts()

df2 = df2[df2['COD_GRADO'] != ' ']
df2['COD_GRADO'] = df2['COD_GRADO'].astype(int)
df2 = df2[df2['COD_GRADO'].isin([3, 4])]
df2['COD_GRADO'].value_counts()

df2.to_csv('2021_SEP.csv', index=False)

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

#Preferenciales
df2 = pd.read_csv(r"C:\Users\Luis José López\Documents\7-Maestría\PUC\Semestre 4\Machine-Learning\Trabajo final\PPB_2020.csv" , sep=';')

df2 = df2[df2['COD_ENSE'] != ' ']
df2['COD_ENSE'] = df2['COD_ENSE'].astype(int)
df2 = df2[df2['COD_ENSE'].isin([310, 410, 510, 610, 710, 810, 910])]
df2['COD_ENSE'].value_counts()

df2 = df2[df2['COD_GRADO'] != ' ']
df2['COD_GRADO'] = df2['COD_GRADO'].astype(int)
df2 = df2[df2['COD_GRADO'].isin([3, 4])]
df2['COD_GRADO'].value_counts()

df2.to_csv('2020_SEP.csv', index=False)

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

#Preferenciales
df2 = pd.read_csv(r"C:\Users\Luis José López\Documents\7-Maestría\PUC\Semestre 4\Machine-Learning\Trabajo final\PPB_2019.csv" , sep=';')

df2 = df2[df2['COD_ENSE'] != ' ']
df2['COD_ENSE'] = df2['COD_ENSE'].astype(int)
df2 = df2[df2['COD_ENSE'].isin([310, 410, 510, 610, 710, 810, 910])]
df2['COD_ENSE'].value_counts()

df2 = df2[df2['COD_GRADO'] != ' ']
df2['COD_GRADO'] = df2['COD_GRADO'].astype(int)
df2 = df2[df2['COD_GRADO'].isin([3, 4])]
df2['COD_GRADO'].value_counts()

df2.to_csv('2019_SEP.csv', index=False)

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

#Preferenciales
df2 = pd.read_csv(r"C:\Users\Luis José López\Documents\7-Maestría\PUC\Semestre 4\Machine-Learning\Trabajo final\PPB_2018.csv" , sep=';')

df2 = df2[df2['COD_ENSE'] != ' ']
df2['COD_ENSE'] = df2['COD_ENSE'].astype(int)
df2 = df2[df2['COD_ENSE'].isin([310, 410, 510, 610, 710, 810, 910])]
df2['COD_ENSE'].value_counts()

df2 = df2[df2['COD_GRADO'] != ' ']
df2['COD_GRADO'] = df2['COD_GRADO'].astype(int)
df2 = df2[df2['COD_GRADO'].isin([3, 4])]
df2['COD_GRADO'].value_counts()

df2.to_csv('2018_SEP.csv', index=False)

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

df1['cod_ense'] = df1['cod_ense'].astype(int)
df1 = df1[df1['cod_grado'].isin([3, 4])]

df1['cod_grado'].value_counts()

df1.to_csv('2017.csv', index=False)

#Preferenciales
df2 = pd.read_csv(r"C:\Users\Luis José López\Documents\7-Maestría\PUC\Semestre 4\Machine-Learning\Trabajo final\PPB_2017.csv" , sep=';')

df2 = df2[df2['COD_ENSE'] != ' ']
df2['COD_ENSE'] = df2['COD_ENSE'].astype(int)
df2 = df2[df2['COD_ENSE'].isin([310, 410, 510, 610, 710, 810, 910])]
df2['COD_ENSE'].value_counts()

df2 = df2[df2['COD_GRADO'] != ' ']
df2['COD_GRADO'] = df2['COD_GRADO'].astype(int)
df2 = df2[df2['COD_GRADO'].isin([3, 4])]
df2['COD_GRADO'].value_counts()

df2.to_csv('2017_SEP.csv', index=False)

""" ######################### Cargar bases ########################## """
%clear
%reset -f
!cls 
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
os.chdir(r"C:\Users\Luis José López\Documents\7-Maestría\PUC\Semestre 4\Machine-Learning\Trabajo final")

df1 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2020.csv')
df2 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2021.csv')
df3 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2022.csv')
df4 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2023.csv') 
df5 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2024.csv')
df6 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2019.csv')
df7 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2018.csv')
df8 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2017.csv')

df8.columns = df8.columns.str.upper()

df_p1 = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8], ignore_index=True) 

del df1, df2 , df3, df4, df5, df6, df7, df8

df1 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2020_SEP.csv')
df2 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2021_SEP.csv')
df3 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2022_SEP.csv')
df4 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2023_SEP.csv') 
df5 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2024_SEP.csv')
df6 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2019_SEP.csv')
df7 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2018_SEP.csv')
df8 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2017_SEP.csv')

df8.columns = df8.columns.str.upper()

df_p2= pd.concat([df1, df2, df3, df4, df5, df6, df7, df8], ignore_index=True) 

del df1, df2 , df3, df4, df5, df6, df7, df8

df = pd.merge(df_p1, df_p2, on=['MRUN', 'AGNO'], how='left')

del df_p1 df_p2

""" ################ Pre procesamiento ####################### """
#Descripción de cada columna (tipo de dato y missings)
df_p1.info()
df.head()

"""

"""

#Evaluar missing y outliers


#1. Total de missings

#2. Missing en particulares pagados
count = df_p1[(df_p1['ASISTENCIA'] == 'Y') & (df_p1['COD_DEPE'] == 4)].shape[0]
missing_asistencia = df_p1[(df_p1['ASISTENCIA'] == 50) & (df_p1['COD_DEPE'] == 4)]

#Crear variable target


df = df[df['SIT_FIN_R'] != ' '] #Se dropea porque son valores vacíos


#Dropear particulares pagados ['COD_DEPE'] == 4


""" ################ Análisis exploratorio de datos ####################### """
#Distribución de variables continuas
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

#Conteo de cada estado de var categoricas


#Correlaciones y distribuciones por clase


""" ################ Feature Engineering ####################### """
#Imputar outliers


#Estandarizar/Normalizar variables


#Reeemplazar variables string por númericas (one hot encoding)


#Balancear set de entrenamiento 


""" ##################### Modelo 1 ####################### """

""" ##################### Modelo 2 ####################### """

""" ##################### Modelo 3 ####################### """

""" ################# Muestra aleatoria ################## """

