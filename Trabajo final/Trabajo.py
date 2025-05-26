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

os.chdir(r'/Users/xiomarakuwae/Documents/GitHub/Machine-Learning/Trabajo final')
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
df5 = pd.read_csv(r'/Users/xiomarakuwae/Downloads/Proyecto AMLE/20250212_Rendimiento_2024_20250131_WEB.csv', sep=';')

df5 = df5[~df5['COD_ENSE'].isin([110, 165, 167, 211, 212, 213, 214, 215, 216, 217, 218, 219, 299])]

df5['COD_ENSE'].value_counts()

df5 = df5[df5['COD_GRADO'].isin([3, 4])]

df5['COD_GRADO'].value_counts()

df5.to_csv('2024_Rendimiento_filtrado.csv', index=False)

#Preferenciales
df2 = pd.read_csv(r'/Users/xiomarakuwae/Downloads/Proyecto AMLE/20241122_Preferentes_Prioritarios_y_Beneficiarios_2024_20241130_PUBL_MRUN.csv' , sep=';')

df2 = df2[df2['COD_ENSE'] != ' ']
df2['COD_ENSE'] = df2['COD_ENSE'].astype(int)
df2 = df2[df2['COD_ENSE'].isin([310, 410, 510, 610, 710, 810, 910])]
df2['COD_ENSE'].value_counts()

df2 = df2[df2['COD_GRADO'] != ' ']
df2['COD_GRADO'] = df2['COD_GRADO'].astype(int)
df2 = df2[df2['COD_GRADO'].isin([3, 4])]
df2['COD_GRADO'].value_counts()

df2.to_csv('2024_SEP_filtrado.csv', index=False)

""" 2023 """
%clear
%reset -f
!cls 
import pandas as pd
import os
os.chdir(r'/Users/xiomarakuwae/Documents/GitHub/Machine-Learning/Trabajo final')
df4 = pd.read_csv(r'/Users/xiomarakuwae/Downloads/Proyecto AMLE/20240209_Rendimiento_2023_20240131_WEB.csv', sep=';')

df4 = df4[~df4['COD_ENSE'].isin([110, 165, 167, 211, 212, 213, 214, 215, 216, 217, 218, 219, 299])]

df4['COD_ENSE'].value_counts()

df4 = df4[df4['COD_GRADO'].isin([3, 4])]

df4['COD_GRADO'].value_counts()

df4.to_csv('2023_Rendimiento_filtrado.csv', index=False)

#Preferenciales
df2 = pd.read_csv(r'/Users/xiomarakuwae/Downloads/Proyecto AMLE/20231211_Preferentes_Prioritarios_y_Beneficiarios_2023_20231130_WEB.csv' , sep=';')

df2 = df2[df2['COD_ENSE'] != ' ']
df2['COD_ENSE'] = df2['COD_ENSE'].astype(int)
df2 = df2[df2['COD_ENSE'].isin([310, 410, 510, 610, 710, 810, 910])]
df2['COD_ENSE'].value_counts()

df2 = df2[df2['COD_GRADO'] != ' ']
df2['COD_GRADO'] = df2['COD_GRADO'].astype(int)
df2 = df2[df2['COD_GRADO'].isin([3, 4])]
df2['COD_GRADO'].value_counts()

df2.to_csv('2023_SEP_filtrado.csv', index=False)

""" 2022 """
%clear
%reset -f
!cls 
import pandas as pd
import os
os.chdir(r'/Users/xiomarakuwae/Documents/GitHub/Machine-Learning/Trabajo final')
df3 = pd.read_csv(r'/Users/xiomarakuwae/Downloads/Proyecto AMLE/20230209_Rendimiento_2022_20230131_WEB.csv', sep=';')

df3 = df3[~df3['COD_ENSE'].isin([110, 165, 167, 211, 212, 213, 214, 215, 216, 217, 218, 219, 299])]

df3['COD_ENSE'].value_counts()

df3 = df3[df3['COD_GRADO'].isin([3, 4])]

df3['COD_GRADO'].value_counts()

df3.to_csv('2022_Rendimiento_filtrado.csv', index=False)

#Preferenciales
df2 = pd.read_csv(r'/Users/xiomarakuwae/Downloads/Proyecto AMLE/20221216_Preferentes_Prioritarios_y_Beneficiarios_2022_20221130_WEB.csv', sep=';')

df2 = df2[df2['COD_ENSE'] != ' ']
df2['COD_ENSE'] = df2['COD_ENSE'].astype(int)
df2 = df2[df2['COD_ENSE'].isin([310, 410, 510, 610, 710, 810, 910])]
df2['COD_ENSE'].value_counts()

df2 = df2[df2['COD_GRADO'] != ' ']
df2['COD_GRADO'] = df2['COD_GRADO'].astype(int)
df2 = df2[df2['COD_GRADO'].isin([3, 4])]
df2['COD_GRADO'].value_counts()

df2.to_csv('2022_SEP_filtrado.csv', index=False)

""" 2021 """
%clear
%reset -f
!cls 
import pandas as pd
import os
os.chdir(r'/Users/xiomarakuwae/Documents/GitHub/Machine-Learning/Trabajo final')
df2 = pd.read_csv(r'/Users/xiomarakuwae/Downloads/Proyecto AMLE/20220302_Rendimiento_2021_20220131_WEB.csv', sep=';')

df2 = df2[~df2['COD_ENSE'].isin([110, 165, 167, 211, 212, 213, 214, 215, 216, 217, 218, 219, 299])]

df2['COD_ENSE'].value_counts()

df2 = df2[df2['COD_GRADO'].isin([3, 4])]

df2['COD_GRADO'].value_counts()

df2.to_csv('2021_Rendimiento_filtrado.csv', index=False)

#Preferenciales
df2 = pd.read_csv(r'/Users/xiomarakuwae/Downloads/Proyecto AMLE/20211229_Preferentes_Prioritarios_y_Beneficiarios_2021_20211126_WEB.csv', sep=';')

df2 = df2[df2['COD_ENSE'] != ' ']
df2['COD_ENSE'] = df2['COD_ENSE'].astype(int)
df2 = df2[df2['COD_ENSE'].isin([310, 410, 510, 610, 710, 810, 910])]
df2['COD_ENSE'].value_counts()

df2 = df2[df2['COD_GRADO'] != ' ']
df2['COD_GRADO'] = df2['COD_GRADO'].astype(int)
df2 = df2[df2['COD_GRADO'].isin([3, 4])]
df2['COD_GRADO'].value_counts()

df2.to_csv('2021_SEP_filtrado.csv', index=False)

""" 2020 """
%clear
%reset -f
!cls 
import pandas as pd
import os
os.chdir(r'/Users/xiomarakuwae/Documents/GitHub/Machine-Learning/Trabajo final')
df1 = pd.read_csv(r'/Users/xiomarakuwae/Downloads/Proyecto AMLE/20210223_Rendimiento_2020_20210131_WEB.csv', sep=';')

df1 = df1[~df1['COD_ENSE'].isin([110, 165, 167, 211, 212, 213, 214, 215, 216, 217, 218, 219, 299])]

df1['COD_ENSE'].value_counts()

df1 = df1[df1['COD_GRADO'].isin([3, 4])]

df1['COD_GRADO'].value_counts()

df1.to_csv('2020_Rendimiento_filtrado.csv', index=False)

#Preferenciales
df2 = pd.read_csv(r'/Users/xiomarakuwae/Downloads/Proyecto AMLE/20201209_Preferentes_Prioritarios_y_Beneficiarios_2020_20201126_WEB.csv', sep=';')

df2 = df2[df2['COD_ENSE'] != ' ']
df2['COD_ENSE'] = df2['COD_ENSE'].astype(int)
df2 = df2[df2['COD_ENSE'].isin([310, 410, 510, 610, 710, 810, 910])]
df2['COD_ENSE'].value_counts()

df2 = df2[df2['COD_GRADO'] != ' ']
df2['COD_GRADO'] = df2['COD_GRADO'].astype(int)
df2 = df2[df2['COD_GRADO'].isin([3, 4])]
df2['COD_GRADO'].value_counts()

df2.to_csv('2020_SEP_filtrado.csv', index=False)

""" 2019 """
%clear
%reset -f
!cls 
import pandas as pd
import os
os.chdir(r'/Users/xiomarakuwae/Documents/GitHub/Machine-Learning/Trabajo final')
df1 = pd.read_csv(r'/Users/xiomarakuwae/Downloads/Proyecto AMLE/20200220_Rendimiento_2019_20200131_PUBL.csv', sep=';')

df1 = df1[~df1['COD_ENSE'].isin([110, 165, 167, 211, 212, 213, 214, 215, 216, 217, 218, 219, 299])]

df1['COD_ENSE'].value_counts()

df1 = df1[df1['COD_GRADO'].isin([3, 4])]

df1['COD_GRADO'].value_counts()

df1.to_csv('2019_Rendimiento_filtrado.csv', index=False)

#Preferenciales
df2 = pd.read_csv(r'/Users/xiomarakuwae/Downloads/Proyecto AMLE/20191122_Preferentes_Prioritarios_y_Beneficiarios_2019_20191106_PUBL.csv', sep=';')

df2 = df2[df2['COD_ENSE'] != ' ']
df2['COD_ENSE'] = df2['COD_ENSE'].astype(int)
df2 = df2[df2['COD_ENSE'].isin([310, 410, 510, 610, 710, 810, 910])]
df2['COD_ENSE'].value_counts()

df2 = df2[df2['COD_GRADO'] != ' ']
df2['COD_GRADO'] = df2['COD_GRADO'].astype(int)
df2 = df2[df2['COD_GRADO'].isin([3, 4])]
df2['COD_GRADO'].value_counts()

df2.to_csv('2019_SEP_filtrado.csv', index=False)

""" 2018 """
%clear
%reset -f
!cls 
import pandas as pd
import os
os.chdir(r'/Users/xiomarakuwae/Documents/GitHub/Machine-Learning/Trabajo final')
df1 = pd.read_csv(r'/Users/xiomarakuwae/Downloads/Proyecto AMLE/20190220_Rendimiento_2018_20190131_PUBL.csv', sep=';')

df1 = df1[~df1['COD_ENSE'].isin([110, 165, 167, 211, 212, 213, 214, 215, 216, 217, 218, 219, 299])]

df1['COD_ENSE'].value_counts()

df1 = df1[df1['COD_GRADO'].isin([3, 4])]

df1['COD_GRADO'].value_counts()

df1.to_csv('2018_Rendimiento_filtrado.csv', index=False)

#Preferenciales
df2 = pd.read_csv(r'/Users/xiomarakuwae/Downloads/Proyecto AMLE/20181211_Preferentes_Prioritarios_y_Beneficiarios_2018_20181106_PUBL.csv', sep=';')

df2 = df2[df2['COD_ENSE'] != ' ']
df2['COD_ENSE'] = df2['COD_ENSE'].astype(int)
df2 = df2[df2['COD_ENSE'].isin([310, 410, 510, 610, 710, 810, 910])]
df2['COD_ENSE'].value_counts()

df2 = df2[df2['COD_GRADO'] != ' ']
df2['COD_GRADO'] = df2['COD_GRADO'].astype(int)
df2 = df2[df2['COD_GRADO'].isin([3, 4])]
df2['COD_GRADO'].value_counts()

df2.to_csv('2018_SEP_filtrado.csv', index=False)

""" 2017 """
%clear
%reset -f
!cls 
import pandas as pd
import os
os.chdir(r'/Users/xiomarakuwae/Documents/GitHub/Machine-Learning/Trabajo final')
df1 = pd.read_csv(r'/Users/xiomarakuwae/Downloads/Proyecto AMLE/20180213_Rendimiento_2017_20180131_PUBL.csv', sep=';')

df1 = df1[~df1['cod_ense'].isin([110, 165, 167, 211, 212, 213, 214, 215, 216, 217, 218, 219, 299])]

df1['cod_ense'].value_counts()

df1['cod_ense'] = df1['cod_ense'].astype(int)
df1 = df1[df1['cod_grado'].isin([3, 4])]

df1['cod_grado'].value_counts()

df1.to_csv('2017_Rendimiento_filtrado.csv', index=False)

#Preferenciales
df2 = pd.read_csv(r'/Users/xiomarakuwae/Downloads/Proyecto AMLE/Preferentes_Prioritarios_y_Beneficiarios_2017_20171030_PUBL.csv', sep=';')

df2 = df2[df2['COD_ENSE'] != ' ']
df2['COD_ENSE'] = df2['COD_ENSE'].astype(int)
df2 = df2[df2['COD_ENSE'].isin([310, 410, 510, 610, 710, 810, 910])]
df2['COD_ENSE'].value_counts()

df2 = df2[df2['COD_GRADO'] != ' ']
df2['COD_GRADO'] = df2['COD_GRADO'].astype(int)
df2 = df2[df2['COD_GRADO'].isin([3, 4])]
df2['COD_GRADO'].value_counts()

df2.to_csv('2017_SEP_filtrado_filtrado.csv', index=False)

# Agregamos la base "Rendimiento" de 2016, para extraer el dato de promedio general anual.
""" 2016 """
%clear
%reset -f
!cls 
import pandas as pd
import os
os.chdir(r'/Users/xiomarakuwae/Documents/GitHub/Machine-Learning/Trabajo final')
df1 = pd.read_csv(r'/Users/xiomarakuwae/Downloads/Proyecto AMLE/20170216_Rendimiento_2016_20170131_PUBL.csv', sep=';')

df1 = df1[~df1['cod_ense'].isin([110, 165, 167, 211, 212, 213, 214, 215, 216, 217, 218, 219, 299])]

df1['cod_ense'].value_counts()

df1['cod_ense'] = df1['cod_ense'].astype(int)
df1 = df1[df1['cod_grado'].isin([3, 4])]

df1['cod_grado'].value_counts()

df1.to_csv('2016_Rendimiento_filtrado.csv', index=False)

""" ######################### Cargar bases ########################## """
%clear
%reset -f
!cls 
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
os.chdir(r'/Users/xiomarakuwae/Documents/GitHub/Machine-Learning/Trabajo final')

df1 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2020_Rendimiento_filtrado.csv')
df2 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2021_Rendimiento_filtrado.csv')
df3 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2022_Rendimiento_filtrado.csv')
df4 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2023_Rendimiento_filtrado.csv') 
df5 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2024_Rendimiento_filtrado.csv')
df6 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2019_Rendimiento_filtrado.csv')
df7 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2018_Rendimiento_filtrado.csv')
df8 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2018_Rendimiento_filtrado.csv')
df9 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2016_Rendimiento_filtrado.csv')

df8.columns = df8.columns.str.upper()
df9.columns = df9.columns.str.upper()

# Lista de DataFrames
dfs = [df1, df2, df3, df4, df5, df6, df7, df8, df9]

# Procesar cada DataFrame para eliminar duplicados en MRUN
for i in range(len(dfs)):
    dfs[i]['MRUN'] = dfs[i]['MRUN'].astype(str).str.strip()
    duplicated_mruns = dfs[i]['MRUN'].value_counts()
    duplicated_mruns = duplicated_mruns[duplicated_mruns > 1].index
    dfs[i] = dfs[i][~dfs[i]['MRUN'].isin(duplicated_mruns)]

# Asignar los DataFrames modificados de vuelta
df1, df2, df3, df4, df5, df6, df7, df8, df9 = dfs

df_p1 = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9], ignore_index=True) 

df_p1['AGNO'] = df_p1['AGNO'].astype(int)
df_p1['MRUN'] = df_p1['MRUN'].astype(int)

del df1, df2 , df3, df4, df5, df6, df7, df8, df9, duplicated_mruns


# Crear variable PROM_GRAL_ANTERIOR
# Ordenar por MRUN y AGNO para asegurar que shift funcione correctamente
df_p1 = df_p1.sort_values(['MRUN', 'AGNO'])

# Crear PROM_GRAL_ANTERIOR usando groupby y shift
df_p1['PROM_GRAL_ANTERIOR'] = df_p1.groupby('MRUN')['PROM_GRAL'].shift(1)

# Opcional: Manejar valores nulos (si no hay dato del año anterior)
df_p1['PROM_GRAL_ANTERIOR'] = df_p1['PROM_GRAL_ANTERIOR'].fillna(np.nan)  # O usa otro valor, como np.nan

# Eliminar los datos de 2016
df_p1 = df_p1[df_p1['AGNO'] != 2016]

# Mostrar las primeras filas para verificar
print(df_p1[['MRUN', 'AGNO', 'PROM_GRAL', 'PROM_GRAL_ANTERIOR']].head(10))

df1 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2020_SEP_filtrado.csv')
df2 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2021_SEP_filtrado.csv')
df3 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2022_SEP_filtrado.csv')
df4 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2023_SEP_filtrado.csv') 
df5 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2024_SEP_filtrado.csv')
df6 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2019_SEP_filtrado.csv')
df7 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2018_SEP_filtrado.csv')
df8 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2017_SEP_filtrado.csv')

df8.columns = df8.columns.str.upper()

# Lista de DataFrames
dfs = [df1, df2, df3, df4, df5, df6, df7, df8]

# Procesar cada DataFrame para eliminar duplicados en MRUN
for i in range(len(dfs)):
    dfs[i]['MRUN'] = dfs[i]['MRUN'].astype(str).str.strip()
    duplicated_mruns = dfs[i]['MRUN'].value_counts()
    duplicated_mruns = duplicated_mruns[duplicated_mruns > 1].index
    dfs[i] = dfs[i][~dfs[i]['MRUN'].isin(duplicated_mruns)]

# Asignar los DataFrames modificados de vuelta
df1, df2, df3, df4, df5, df6, df7, df8 = dfs

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

print(f"Observaciones después del merge: {len(df):,}") # 2,486,512 obs

del df_p1, df_p2

df.to_csv('df_merged.csv', index=False)

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
GEN_ALU: Género (1 =  masculino)
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
CONVENIO_SEP: Establecimiento tiene convenio SEP (1 =  si)
AÑO_INGRESO_SEP: Año inicio convenio SEP
CLASIFICACION_SEP: Clasificación de convenio SEP
EE_GRATUITO: Indicador de gratuidad de establecimiento (1 =  si)
GRADO_SEP: Nivel de SEP
PRIORITARIO_ALU: Indicador de si alumno es prioritario (1 =  si)
PREFERENTE_ALU: Indicador de si alumno es preferente (1 =  si)
BEN_SEP: Indicador de si alumno es beneficiario de SEP (1 =  si)
FEC_DEFUN_ALU: 
"""
df.isnull().sum().sort_values(ascending=False) #Total de missings

df['ASISTENCIA'] = pd.to_numeric(df['ASISTENCIA'], errors='coerce') #Ajustar para que todas sean numericas
df['PROM_GRAL'] = (df['PROM_GRAL'].astype(str).str.replace(',', '.', regex=False).astype(float))
df['EDAD_ALU']   = pd.to_numeric(df['EDAD_ALU'], errors='coerce')

df = df[df['SIT_FIN_R'] != ' '] #Se dropea porque son valores vacíos

df['DESERTAR'] = (df['SIT_FIN_R'] == 'Y').astype(int) #Crear variable target

df = df[df['COD_DEPE2'] != 3] #Dropear particulares pagados porque no estan obligados a reportar asistencia

""" ################ Análisis exploratorio de datos ####################### """
#Outliers
df['X_bin'] = pd.qcut(df['PROM_GRAL'], q=20, duplicates='drop')  # 20 quantile bins

binned = df.groupby('X_bin', observed=True).agg({'PROM_GRAL': 'mean','ASISTENCIA': 'mean'}).reset_index()

plt.figure(figsize=(8,6))
sns.scatterplot(data=binned, x='PROM_GRAL', y='ASISTENCIA')  # Use numeric PROM_GRAL
plt.xlabel('PROM_GRAL (Binned Means)')
plt.ylabel('ASISTENCIA (Mean)')
plt.title('Binscatter: ASISTENCIA vs PROM_GRAL')
plt.tight_layout()
plt.show()

df['A_bin'] = pd.qcut(df['EDAD_ALU'], q=20, duplicates='drop')  # 20 quantile bins

binned = df.groupby('A_bin', observed=True).agg({'EDAD_ALU': 'mean','ASISTENCIA': 'mean'}).reset_index()

plt.figure(figsize=(8,6))
sns.scatterplot(data=binned, x='EDAD_ALU', y='ASISTENCIA')  # Use numeric PROM_GRAL
plt.xlabel('Edad (Binned Means)')
plt.ylabel('ASISTENCIA (Mean)')
plt.title('Binscatter: ASISTENCIA vs Edad')
plt.tight_layout()
plt.show()

#Distribución de variables numericas
variables = ['ASISTENCIA', 'PROM_GRAL', 'EDAD_ALU']

plt.figure(figsize=(15, 4))

for i, var in enumerate(variables):
    plt.subplot(1, 3, i + 1)
    plt.hist(df[var].dropna(), bins=30, color='skyblue', edgecolor='black')
    plt.title(f'Histogram of {var}')
    plt.xlabel(var)
    plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

#Correlaciones y distribuciones por clase
numericos = df[['ASISTENCIA', 'PROM_GRAL', 'EDAD_ALU']]

corr = numericos.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=False, cmap='coolwarm', fmt=".2f", square=True)
plt.title("Heatmap de correlaciones")
plt.tight_layout()
plt.show()

#Conteo de cada estado de variables categoricas
categorias = ['GEN_ALU','SIT_FIN_R','PRIORITARIO_ALU', 'PREFERENTE_ALU',
              'BEN_SEP', 'RURAL_RBD', 'COD_DEPE2', 'EE_GRATUITO']

df_graph = df[df['SIT_FIN_R'].isin(['P', 'Y'])]

plt.figure(figsize=(20, 25))

for i, var in enumerate(categorias):
    ax = plt.subplot(5, 2, i + 1)
    sns.countplot(data=df_graph, x=var, palette='pastel', ax=ax)
    ax.set_title(f'Distribucion de {var} para aprobados y desertores')
    ax.set_xlabel(var)
    ax.set_ylabel("Cantidad")
    ax.tick_params(axis='x', rotation=45)

    total = df_graph[var].notna().sum()

    # Annotate each bar with % of total
    for patch in ax.patches:
        count = patch.get_height()
        if count > 0:
            pct = 100 * count / total
            ax.annotate(f'{pct:.1f}%', 
                        (patch.get_x() + patch.get_width() / 2, count),
                        ha='center', va='bottom', fontsize=9)

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
