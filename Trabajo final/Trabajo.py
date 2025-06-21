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
Rendimiento 2017, Rendimiento 2016, PPB 2024, PPB 2023, PPB 2022, PPB 2021, PPB 2020, PPB 2019,
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
df8 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2017_Rendimiento_filtrado.csv')
df9 = pd.read_csv('https://raw.githubusercontent.com/luijolo/Machine-Learning/refs/heads/main/Trabajo%20final/2016_Rendimiento_filtrado.csv')

df8.columns = df8.columns.str.upper()
df9.columns = df9.columns.str.upper()

# Lista de DataFrames
dfs = [df1, df2, df3, df4, df5, df6, df7, df8, df9]

# Procesar cada DataFrame para eliminar duplicados en MRUN
for i in range(len(dfs)):
    # Convertir MRUN a string y eliminar espacios
    dfs[i]['MRUN'] = dfs[i]['MRUN'].astype(str).str.strip()
    
    # Reemplazar comas por puntos en PROM_GRAL y convertir a float
    if dfs[i]['PROM_GRAL'].dtype == 'object':
        dfs[i]['PROM_GRAL'] = dfs[i]['PROM_GRAL'].str.replace(',', '.', regex=False)
    dfs[i]['PROM_GRAL'] = pd.to_numeric(dfs[i]['PROM_GRAL'], errors='coerce')
    
    # Verificar valores no numéricos en PROM_GRAL
    if dfs[i]['PROM_GRAL'].isna().sum() > 0:
        print(f"Valores no numéricos en PROM_GRAL en df{i+1}: {dfs[i]['PROM_GRAL'].isna().sum()}")
    
    # Eliminar duplicados en MRUN
    duplicated_mruns = dfs[i]['MRUN'].value_counts()
    duplicated_mruns = duplicated_mruns[duplicated_mruns > 1].index
    dfs[i] = dfs[i][~dfs[i]['MRUN'].isin(duplicated_mruns)]

# Asignar los DataFrames modificados de vuelta
df1, df2, df3, df4, df5, df6, df7, df8, df9 = dfs

df_p1 = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9], ignore_index=True) 

df_p1['AGNO'] = df_p1['AGNO'].astype(int)
df_p1['MRUN'] = df_p1['MRUN'].astype(int)
df_p1['PROM_GRAL'] = df_p1['PROM_GRAL'].astype(float)  # Asegurar que PROM_GRAL sea float

del df1, df2 , df3, df4, df5, df6, df7, df8, df9, duplicated_mruns

# Crear variable PROM_GRAL_ANTERIOR
# Ordenar por MRUN y AGNO para asegurar que shift funcione correctamente
df_p1 = df_p1.sort_values(['MRUN', 'AGNO'])

# Crear PROM_GRAL_ANTERIOR usando groupby y shift
df_p1['PROM_GRAL_ANTERIOR'] = df_p1.groupby('MRUN')['PROM_GRAL'].shift(1)

# Opcional: Manejar valores nulos (si no hay dato del año anterior)
df_p1['PROM_GRAL_ANTERIOR'] = df_p1['PROM_GRAL_ANTERIOR'].fillna(np.nan)

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

df_p2 = df_p2.drop(columns=['GEN_ALU', 'FEC_NAC_ALU', 'RBD', 'DGV_RBD', 'NOM_RBD',
                            'NOM_REG_RBD_A', 'COD_REG_RBD', 'COD_PRO_RBD',
                            'COD_COM_RBD', 'NOM_COM_RBD', 'COD_DEPROV_RBD',
                            'NOM_DEPROV_RBD', 'COD_DEPE', 'COD_DEPE2',
                            'ESTADO_ESTAB', 'NOMBRE_SLEP', 'COD_ENSE', 'COD_ENSE2',
                            'COD_GRADO', 'LET_CUR', 'COD_JOR', 'RURAL_RBD'])

del df1, df2 , df3, df4, df5, df6, df7, df8, duplicated_mruns

df = pd.merge(df_p1, df_p2, on=['MRUN', 'AGNO'], how='inner')

print(f"Observaciones después del merge: {len(df):,}") # 2,486,512 obs

del df_p1, df_p2

# Información detallada sobre cada variable obtenida
print(f"\nInformación detallada del dataset:")
df.info()


# Variables a eliminar (lista completa y corregida)
variables_eliminar = [
    'RBD', 'DGV_RBD', 'NOM_RBD', 'COD_REG_RBD', 'NOM_REG_RBD_A',
    'COD_PRO_RBD', 'NOM_COM_RBD', 'COD_DEPROV_RBD', 'NOM_DEPROV_RBD',
    'COD_DEPE', 'ESTADO_ESTAB', 'COD_ENSE2', 'LET_CUR', 'COD_JOR',
    'COD_TIP_CUR', 'COD_DES_CUR', 'FEC_NAC_ALU', 'COD_REG_ALU',
    'NOM_COM_ALU', 'COD_RAMA', 'COD_SEC', 'SIT_FIN', 'COD_ESPE',
    'COD_MEN', 'NOMBRE_SLEP', 'CRITERIO_SEP', 'CONVENIO_SEP',
    'AÑO_INGRESO_SEP', 'CLASIFICACION_SEP', 'COD_ENSE3', 'COD_GRADO2',
    'GRADO_SEP', 'FEC_DEFUN_ALU'
]

# Eliminar las variables que existen
variables_existentes = [var for var in variables_eliminar if var in df.columns]
df = df.drop(columns=variables_existentes)

# Información detallada sobre cada variable obtenida
print(f"\nInformación detallada del dataset:")
df.info()

df.to_csv('df_merged.csv', index=False)


""" ################ Pre procesamiento ####################### """
# Descripción de cada columna (tipo de dato y missings)
df.head()
"""
AGNO: Año de los datos
COD_COM_RBD: Código comuna del establecimiento
COD_DEPE2: Dependencia recodificado
RURAL_RBD: Área (urbana o rural)
COD_ENSE: Código de tipo de enseñanza
COD_GRADO: Código de grado
MRUN: Máscara del RUN del estudiante
GEN_ALU: Género (1 = masculino)
EDAD_ALU: Edad al 30 de junio
COD_COM_ALU: Comuna residencia alumno
PROM_GRAL: Promedio del año
ASISTENCIA: Porcentaje asistencia en el año
SIT_FIN_R: Situación final de promoción (con traslado)
EE_GRATUITO: Indicador de gratuidad de establecimiento (1 = si)
PRIORITARIO_ALU: Indicador de si alumno es prioritario (1 = si)
PREFERENTE_ALU: Indicador de si alumno es preferente (1 = si)
BEN_SEP: Indicador de si alumno es beneficiario de SEP (1 = si)
"""

df.isnull().sum().sort_values(ascending=False) # Total de missings

df['ASISTENCIA'] = pd.to_numeric(df['ASISTENCIA'], errors='coerce') #Ajustar para que todas sean numericas
df['PROM_GRAL'] = (df['PROM_GRAL'].astype(str).str.replace(',', '.', regex=False).astype(float))
df['EDAD_ALU']   = pd.to_numeric(df['EDAD_ALU'], errors='coerce')

df = df[df['SIT_FIN_R'] != ' '] #Se dropea porque son valores vacíos

df['DESERTAR'] = (df['SIT_FIN_R'] == 'Y').astype(int) #Crear variable target

df = df[df['COD_DEPE2'] != 3] #Dropear particulares pagados porque no estan obligados a reportar asistencia


""" ################ Análisis exploratorio de datos ####################### """
#Outliers
df['X_bin'] = pd.qcut(df['PROM_GRAL_ANTERIOR'], q=20, duplicates='drop')  # 20 quantile bins

binned = df.groupby('X_bin', observed=True).agg({'PROM_GRAL_ANTERIOR': 'mean','ASISTENCIA': 'mean'}).reset_index()

plt.figure(figsize=(8,6))
sns.scatterplot(data=binned, x='PROM_GRAL_ANTERIOR', y='ASISTENCIA')  # Use numeric PROM_GRAL
plt.xlabel('PROM_GRAL_ANTERIOR (Binned Means)')
plt.ylabel('ASISTENCIA (Mean)')
plt.title('Binscatter: ASISTENCIA vs PROM_GRAL_ANTERIOR')
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
variables = ['ASISTENCIA', 'PROM_GRAL_ANTERIOR', 'EDAD_ALU']

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
numericos = df[['ASISTENCIA', 'PROM_GRAL_ANTERIOR', 'EDAD_ALU']]

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

# Boxplot de edad
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, y='EDAD_ALU')
plt.title('Boxplot de Edad de los Alumnos')
plt.ylabel('Edad (años)')
plt.grid(True, alpha=0.3)
plt.show()


# GUARDANDO LO CORRIDO 
# df.to_csv("1era_parte.csv", index=False)



""" ################ Decisiones de imputación de missings y depuración de outliers ####################### """

# PARA RECUPERAR LO YA CORRIDO
# import pandas as pd
# df = pd.read_csv("1era_parte.csv")


# A. VERIFICANDO MISSING VALUES POR VARIABLE
missing_analysis = df.isnull().sum()
missing_percentage = (df.isnull().sum() / len(df)) * 100

missing_df = pd.DataFrame({
    'Variable': missing_analysis.index,
    'Missing_Count': missing_analysis.values,
    'Missing_Percentage': missing_percentage.values
})

# Mostrar solo variables con missings
variables_con_missing = missing_df[missing_df['Missing_Count'] > 0].sort_values('Missing_Count', ascending=False)
print(variables_con_missing)


# TRATAMIENTO DE MISSING VALUES
# Al ser pocos decidimos eliminar los missing

# Eliminando filas con missing en EDAD_ALU
df = df.dropna(subset=['EDAD_ALU'])
# Eliminando filas con missing en A_bin
df = df.dropna(subset=['A_bin'])


# B.VERIFICANDO OUTLIERS POR VARIABLE 
variables_categoricas = ['COD_COM_RBD', 'COD_DEPE2', 'COD_ENSE', 'COD_GRADO', 'COD_COM_ALU']
variables_binarias = ['RURAL_RBD', 'GEN_ALU', 'EE_GRATUITO', 'PRIORITARIO_ALU', 'PREFERENTE_ALU', 'BEN_SEP', 'DESERTAR']
variables_identificadores = ['MRUN']
variables_temporales = ['AGNO']
variables_continuas = ['EDAD_ALU', 'PROM_GRAL_ANTERIOR', 'ASISTENCIA']

# Para nuestras variables categóricas, códigos identificadores y binarias no requieren 
# tratamiento de outliers porque sus valores extremos son normales y esperados.

# Revisando variables continuas
for var in variables_continuas:
    if var in df.columns:
        print(f"\n{var}:")
        
        if var == 'EDAD_ALU':
            print(f"  Rango: {df[var].min()}-{df[var].max()} años")
            print(f"  Edades < 12: {len(df[df[var] < 12])}")
            print(f"  Edades > 25: {len(df[df[var] > 25])}")
            
        elif var == 'PROM_GRAL_ANTERIOR':
            print(f"  Rango: {df[var].min()}-{df[var].max()}")
            print(f"  Notas = 0: {len(df[df[var] == 0])}")
            print(f"  Notas > 7: {len(df[df[var] > 7])}")
            
        elif var == 'ASISTENCIA':
            print(f"  Rango: {df[var].min()}-{df[var].max()}%")
            print(f"  Valores < 0: {len(df[df[var] < 0])}")
            print(f"  Valores > 100: {len(df[df[var] > 100])}")

# Se mantendra sin cambios a ASISTENCIA (rango 0-100% es normal) y 
# a PROM_GRAL_ANTERIOR (0=retirado, 1-7=escala de notas) 

# TRATAMIENTO DE OUTLIERS 

# Para EDAD_ALU se elimina menores de 12 años
df = df[df['EDAD_ALU'] >= 12]  # Se elimino a 2 estudiantes


""" ################ Feature Engineering ####################### """
# LIMPIEZA Y TRANSFORMACIONES NECESARIAS (no por missing, ni outlayer)

# Limpieza de la variable GEN_ALU
# Mostrando distribucion actual
df['GEN_ALU'].value_counts().sort_index()
# Eliminar observaciones con GEN_ALU = 0
filas_antes = len(df)
df = df[df['GEN_ALU'] != 0]
filas_despues = len(df)
print(f"Eliminadas {filas_antes - filas_despues} observaciones con genero indeterminado")


# CREACION DE NUEVAS VARIABLES 

# Creando variables de sobredad
# a. Sobredad binaria (19-20 años)
df['SOBREDAD'] = ((df['EDAD_ALU'] >= 19) & (df['EDAD_ALU'] <= 20)).astype(int)
sobredad_count = df['SOBREDAD'].sum()

# b. Sobredad severa (21+ años)
df['SOBREDAD_SEVERA'] = (df['EDAD_ALU'] >= 21).astype(int)
sobredad_severa_count = df['SOBREDAD_SEVERA'].sum()

# Nuestra distribucion final de edades es:
print(f"\nDISTRIBUCION FINAL DE EDADES:")
print(f"   12-18 años (edad normal): {len(df[(df['EDAD_ALU'] >= 12) & (df['EDAD_ALU'] <= 18)]):,}")
print(f"   19-20 años (sobredad): {sobredad_count:,}")
print(f"   21+ años (sobredad severa): {sobredad_severa_count:,}")


# Creando variable dummy: 1 = Mujer, 0 = Varon
df['MUJER'] = (df['GEN_ALU'] == 1).astype(int)

# Creando variable dummy: 1 si alumno estudia en misma comuna que reside, 0 si no
df['MISMA_COMUNA'] = (df['COD_COM_RBD'] == df['COD_COM_ALU']).astype(int)

# Creando dummy pandemia: 1 si fue 2020 o 2021, 0 si no
df['DUMMY_PANDEMIA'] = ((df['AGNO'] == 2020) | (df['AGNO'] == 2021)).astype(int)

# Creando dummy estallido: 1 si fue 2019, 0 si no
df['DUMMY_ESTALLIDO'] = (df['AGNO'] == 2019).astype(int)




# ONE-HOT ENCODING PARA COD_DEPE2

# Verificando la distribución actual
print(df['COD_DEPE2'].value_counts().sort_index())

# Creando las dummies usando pandas get_dummies
dependencia_dummies = pd.get_dummies(df['COD_DEPE2'], prefix='DEPE')

# Nuevas variables creadas
print(f"\nVariables dummy creadas:")
for col in dependencia_dummies.columns:
   print(f"  {col}")

# Agregando las dummies al dataset principal
df = pd.concat([df, dependencia_dummies], axis=1)

# Verificando
print(f"\nVerificacion de creacion:")
for col in dependencia_dummies.columns:
   count_ones = df[col].sum()
   print(f"  {col}: {count_ones:,} casos con valor 1")



# TARGET ENCODING PARA COD_COM_RBD

# Variable objetivo 
target_var = 'DESERTAR'

# Viendo cuantas comunas diferentes existen
n_comunas = df['COD_COM_RBD'].nunique()
print(f"Numero de comunas diferentes: {n_comunas:,}")

# Calculando target encoding
target_encoding = df.groupby('COD_COM_RBD')[target_var].agg(['mean', 'count']).reset_index()
target_encoding.columns = ['COD_COM_RBD', 'COMUNA_TARGET_RATE', 'COMUNA_COUNT']

# Aplicando suavizado (smoothing) para comunas con pocos casos
# Formula: (count * target_rate + alpha * global_rate) / (count + alpha)
global_rate = df[target_var].mean()
alpha = 10  # Factor de suavizado

target_encoding['COMUNA_TARGET_SMOOTH'] = (
   (target_encoding['COMUNA_COUNT'] * target_encoding['COMUNA_TARGET_RATE'] + 
    alpha * global_rate) / 
   (target_encoding['COMUNA_COUNT'] + alpha)
)

# Haciendo merge con el dataset principal
df = df.merge(target_encoding[['COD_COM_RBD', 'COMUNA_TARGET_SMOOTH']], 
             on='COD_COM_RBD', how='left')

# Verificar resultados
print(f"Variable creada: COMUNA_TARGET_SMOOTH")
print(f"Rango de valores: {df['COMUNA_TARGET_SMOOTH'].min():.4f} - {df['COMUNA_TARGET_SMOOTH'].max():.4f}")
print(f"Promedio global: {global_rate:.4f}")
print(f"Comunas procesadas: {len(target_encoding)}")


# Bucketización de COD_ENSE en tres categorías
def map_cod_ense(cod_ense):
    # Mapeo basado en el sistema educativo chileno
    cientifico_humanista = [310, 363]
    tecnico_profesional = [410, 463, 510, 563, 610, 663, 710, 763, 810, 863, 910]

    if cod_ense in cientifico_humanista:
        return 'Científico Humanista'
    elif cod_ense in tecnico_profesional:
        return 'Técnico Profesional'
    else:
        return np.nan  # Para valores no mapeados

# Aplicar el mapeo
df['TIPO_ENSENANZA'] = df['COD_ENSE'].apply(map_cod_ense)

# Verificar valores únicos en TIPO_ENSENANZA
print("Valores únicos en TIPO_ENSENANZA:", df['TIPO_ENSENANZA'].unique())
print("Valores nulos en TIPO_ENSENANZA:", df['TIPO_ENSENANZA'].isna().sum())

# One-hot encoding de TIPO_ENSENANZA
df = pd.get_dummies(df, columns=['TIPO_ENSENANZA'], prefix='ENSE', dtype=int)

# Mostrar las primeras filas para verificar
print(df[['MRUN', 'AGNO', 'COD_ENSE', 'PROM_GRAL', 'PROM_GRAL_ANTERIOR', 
          'ENSE_Científico Humanista', 'ENSE_Técnico Profesional']].head(10))

# Imprimir número de filas para depuración
print(f"Filas en df después del merge y one-hot encoding: {len(df)}")


# Realizar one-hot encoding de COD_GRADO
df = pd.get_dummies(df, columns=['COD_GRADO'], prefix='GRADO', dtype=int)

# Mostrar las primeras filas para verificar las nuevas columnas
print(df[['MRUN', 'AGNO', 'PROM_GRAL', 'GRADO_3', 'GRADO_4']].head(10))


""" ##################### Modelo 1 ####################### """

""" ##################### Modelo 2 ####################### """

""" ##################### Modelo 3 ####################### """

""" ################# Muestra aleatoria ################## """
