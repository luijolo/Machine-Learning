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

    df1['MRUN'] = df1['MRUN'].astype(str).str.strip()
    duplicated_mruns = df1['MRUN'].value_counts()
    duplicated_mruns = duplicated_mruns[duplicated_mruns > 1].index
    df1 = df1[~df1['MRUN'].isin(duplicated_mruns)]
    
    df2['MRUN'] = df2['MRUN'].astype(str).str.strip()
    duplicated_mruns = df2['MRUN'].value_counts()
    duplicated_mruns = duplicated_mruns[duplicated_mruns > 1].index
    df2 = df2[~df2['MRUN'].isin(duplicated_mruns)]
    
    df3['MRUN'] = df3['MRUN'].astype(str).str.strip()
    duplicated_mruns = df3['MRUN'].value_counts()
    duplicated_mruns = duplicated_mruns[duplicated_mruns > 1].index
    df3 = df3[~df3['MRUN'].isin(duplicated_mruns)]
    
    df4['MRUN'] = df4['MRUN'].astype(str).str.strip()
    duplicated_mruns = df4['MRUN'].value_counts()
    duplicated_mruns = duplicated_mruns[duplicated_mruns > 1].index
    df4 = df4[~df4['MRUN'].isin(duplicated_mruns)]
    
    df5['MRUN'] = df5['MRUN'].astype(str).str.strip()
    duplicated_mruns = df5['MRUN'].value_counts()
    duplicated_mruns = duplicated_mruns[duplicated_mruns > 1].index
    df5 = df5[~df5['MRUN'].isin(duplicated_mruns)]
    
    df6['MRUN'] = df6['MRUN'].astype(str).str.strip()
    duplicated_mruns = df6['MRUN'].value_counts()
    duplicated_mruns = duplicated_mruns[duplicated_mruns > 1].index
    df6 = df6[~df6['MRUN'].isin(duplicated_mruns)]
    
    df7['MRUN'] = df7['MRUN'].astype(str).str.strip()
    duplicated_mruns = df7['MRUN'].value_counts()
    duplicated_mruns = duplicated_mruns[duplicated_mruns > 1].index
    df7 = df7[~df7['MRUN'].isin(duplicated_mruns)]
    
    df8['MRUN'] = df8['MRUN'].astype(str).str.strip()
    duplicated_mruns = df8['MRUN'].value_counts()
    duplicated_mruns = duplicated_mruns[duplicated_mruns > 1].index
    df8 = df8[~df8['MRUN'].isin(duplicated_mruns)]

df_p1 = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8], ignore_index=True) 

df_p1['AGNO'] = df_p1['AGNO'].astype(int)
df_p1['MRUN'] = df_p1['MRUN'].astype(int)

del df1, df2 , df3, df4, df5, df6, df7, df8, duplicated_mruns

df1 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2020_SEP.csv')
df2 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2021_SEP.csv')
df3 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2022_SEP.csv')
df4 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2023_SEP.csv') 
df5 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2024_SEP.csv')
df6 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2019_SEP.csv')
df7 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2018_SEP.csv')
df8 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2017_SEP.csv')

df8.columns = df8.columns.str.upper()

    df1['MRUN'] = df1['MRUN'].astype(str).str.strip()
    duplicated_mruns = df1['MRUN'].value_counts()
    duplicated_mruns = duplicated_mruns[duplicated_mruns > 1].index
    df1 = df1[~df1['MRUN'].isin(duplicated_mruns)]
    
    df2['MRUN'] = df2['MRUN'].astype(str).str.strip()
    duplicated_mruns = df2['MRUN'].value_counts()
    duplicated_mruns = duplicated_mruns[duplicated_mruns > 1].index
    df2 = df2[~df2['MRUN'].isin(duplicated_mruns)]
    
    df3['MRUN'] = df3['MRUN'].astype(str).str.strip()
    duplicated_mruns = df3['MRUN'].value_counts()
    duplicated_mruns = duplicated_mruns[duplicated_mruns > 1].index
    df3 = df3[~df3['MRUN'].isin(duplicated_mruns)]
    
    df4['MRUN'] = df4['MRUN'].astype(str).str.strip()
    duplicated_mruns = df4['MRUN'].value_counts()
    duplicated_mruns = duplicated_mruns[duplicated_mruns > 1].index
    df4 = df4[~df4['MRUN'].isin(duplicated_mruns)]
    
    df5['MRUN'] = df5['MRUN'].astype(str).str.strip()
    duplicated_mruns = df5['MRUN'].value_counts()
    duplicated_mruns = duplicated_mruns[duplicated_mruns > 1].index
    df5 = df5[~df5['MRUN'].isin(duplicated_mruns)]
    
    df6['MRUN'] = df6['MRUN'].astype(str).str.strip()
    duplicated_mruns = df6['MRUN'].value_counts()
    duplicated_mruns = duplicated_mruns[duplicated_mruns > 1].index
    df6 = df6[~df6['MRUN'].isin(duplicated_mruns)]
    
    df7['MRUN'] = df7['MRUN'].astype(str).str.strip()
    duplicated_mruns = df7['MRUN'].value_counts()
    duplicated_mruns = duplicated_mruns[duplicated_mruns > 1].index
    df7 = df7[~df7['MRUN'].isin(duplicated_mruns)]
    
    df8['MRUN'] = df8['MRUN'].astype(str).str.strip()
    duplicated_mruns = df8['MRUN'].value_counts()
    duplicated_mruns = duplicated_mruns[duplicated_mruns > 1].index
    df8 = df8[~df8['MRUN'].isin(duplicated_mruns)]

df_p2= pd.concat([df1, df2, df3, df4, df5, df6, df7, df8], ignore_index=True) 

df_p2['AGNO'] = df_p2['AGNO'].astype(int)
df_p2['MRUN'] = df_p2['MRUN'].astype(int)

df_p2 = df_p2.drop(columns=['GEN_ALU', 'FEC_NAC_ALU', 'RBD', 'DGV_RBD', 'NOM_RBD'])
df_p2 = df_p2.drop(columns=['NOM_REG_RBD_A', 'COD_REG_RBD', 'COD_PRO_RBD'])
df_p2 = df_p2.drop(columns=['COD_COM_RBD', 'NOM_COM_RBD', 'COD_DEPROV_RBD']) 
df_p2 = df_p2.drop(columns=['NOM_DEPROV_RBD', 'COD_DEPE', 'COD_DEPE2'])
df_p2 = df_p2.drop(columns=['ESTADO_ESTAB', 'NOMBRE_SLEP', 'COD_ENSE', 'COD_ENSE2']) 
df_p2 = df_p2.drop(columns=['COD_GRADO', 'LET_CUR', 'COD_JOR', 'RURAL_RBD'])

del df1, df2 , df3, df4, df5, df6, df7, df8, duplicated_mruns

df = pd.merge(df_p1, df_p2, on=['MRUN', 'AGNO'], how='inner')

del df_p1, df_p2

df.to_csv('Basefinal.csv', index=False)

""" ################ Pre procesamiento ####################### """
#Descripción de cada columna (tipo de dato y missings)
df.head()

"""
AGNO: Año de los datos
RBD: Rol del establecimiento
DGV_RBD: Dígito verificador del establecimiento
NOM_RBD: Nombre establecimiento
COD_REG_RBD: Código región del establecimiento
NOM_REG_RBD_A: Nombre región del establecimiento
COD_PRO_RBD: Código provincia del establecimiento
COD_COM_RBD: Código comuna del establecimiento
NOM_COM_RBD: Nombre de la comuna
COD_DEPROV_RBD: Código departamento provincial del establecimiento
NOM_DEPROV_RBD: Nombre departamento provincial del establecimiento
COD_DEPE: Dependencia
COD_DEPE2: Dependecia recodificado
RURAL_RBD: Área (urbana o rural)
ESTADO_ESTAB: Estado del establecimiento
COD_ENSE: Código de tipo de enseñanza
COD_ENSE2: Código de tipo de enseñanza por niveles
COD_GRADO: Código de grado
LET_CUR: Letra del curso
COD_JOR: Código jornada
COD_TIP_CUR: Índice de tipo de curso
COD_DES_CUR: Descripción de curso
MRUN: Máscara del RUN del estudiante
GEN_ALU: Género
FEC_NAC_ALU: Fecha de nacimiento
EDAD_ALU: Edad al 30 de junio
COD_REG_ALU: Región residencia alumno
COD_COM_ALU: Comuna residencia alumno
NOM_COM_ALU: Nombre comuna residencia alumno
COD_RAMA: Código de rama del curso (TP)
COD_SEC: Código de sector económico (TP)
COD_ESPE: Código de especialidad (TP)
PROM_GRAL: Promedio del año
ASISTENCIA: Porcentaje asistencia en el año
SIT_FIN: Situación final de promoción
SIT_FIN_R: Situación final de promoción (con traslado)
COD_MEN: Mención
NOMBRE_SLEP:
CRITERIO_SEP:
CONVENIO_SEP: Establecimiento tiene convenio SEP
AÑO_INGRESO_SEP: Año inicio convenio SEP
CLASIFICACION_SEP: Clasificación de convenio SEP
EE_GRATUITO: Indicador de gratuidad de establecimiento
COD_ENSE3:
COD_GRADO2: 
GRADO_SEP: Nivel de SEP
PRIORITARIO_ALU: Indicador de si alumno es prioritario
PREFERENTE_ALU: Indicador de si alumno es preferente
BEN_SEP: Indicador de si alumno es beneficiario de SEP
FEC_DEFUN_ALU: 
"""
df.isnull().sum().sort_values(ascending=False) #Total de missings

#Outliers

df = df[df['SIT_FIN_R'] != ' '] #Se dropea porque son valores vacíos

df['DESERTAR'] = (df['SIT_FIN_R'] == 'Y').astype(int) #Crear variable target

df = df[df['COD_DEPE'] == 4] #Dropear particulares pagados porque no estan obligador a reportar 

df['ASISTENCIA'] = df['ASISTENCIA'].astype(int) #Ajustar para que todas sean numericas
df['PROM_GRAL'] = pd.to_numeric(df['PROM_GRAL'], errors='coerce')
df['EDAD_ALU'] = pd.to_numeric(df['EDAD_ALU'], errors='coerce')

""" ################ Análisis exploratorio de datos ####################### """
#Distribución de variables continuas
continuas = [['ASISTENCIA', 'PROM_GRAL','EDAD_ALU']]

fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(17,5))  # Una columna, tres filas

for i, (col, xlabel, title) in enumerate(continuas):
    data = df[col]
    axes[i].hist(data, color='blue', edgecolor='black')
    axes[i].set_xlabel(xlabel)
    axes[i].set_ylabel('Frecuencia')
    axes[i].set_title(title)

plt.tight_layout()
plt.show()

#Conteo de cada estado de var categoricas
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

#Correlaciones y distribuciones por clase
numericos = df[['ASISTENCIA', 'PROM_GRAL', 'EDAD_ALU']]

corr = numericos.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=False, cmap='coolwarm', fmt=".2f", square=True)
plt.title("Heatmap de correlaciones")
plt.tight_layout()
plt.show()

""" ################ Feature Engineering ####################### """
#Imputar outliers


#Estandarizar/Normalizar variables


#Reeemplazar variables string por númericas (one hot encoding)


#Balancear set de entrenamiento 


""" ##################### Modelo 1 ####################### """

""" ##################### Modelo 2 ####################### """

""" ##################### Modelo 3 ####################### """

""" ################# Muestra aleatoria ################## """
