#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 21 13:51:19 2025

@author: xiomarakuwae
"""

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

df1 = pd.read_csv('/Users/xiomarakuwae/Documents/GitHub/Machine-Learning/Trabajo final/2020_Rendimiento_filtrado.csv')
df2 = pd.read_csv('/Users/xiomarakuwae/Documents/GitHub/Machine-Learning/Trabajo final/2021_Rendimiento_filtrado.csv')
df3 = pd.read_csv('/Users/xiomarakuwae/Documents/GitHub/Machine-Learning/Trabajo final/2022_Rendimiento_filtrado.csv')
df4 = pd.read_csv('/Users/xiomarakuwae/Documents/GitHub/Machine-Learning/Trabajo final/2023_Rendimiento_filtrado.csv') 
df5 = pd.read_csv('/Users/xiomarakuwae/Documents/GitHub/Machine-Learning/Trabajo final/2024_Rendimiento_filtrado.csv')
df6 = pd.read_csv('/Users/xiomarakuwae/Documents/GitHub/Machine-Learning/Trabajo final/2019_Rendimiento_filtrado.csv')
df7 = pd.read_csv('/Users/xiomarakuwae/Documents/GitHub/Machine-Learning/Trabajo final/2018_Rendimiento_filtrado.csv')
df8 = pd.read_csv('/Users/xiomarakuwae/Documents/GitHub/Machine-Learning/Trabajo final/2017_Rendimiento_filtrado.csv')
df9 = pd.read_csv('/Users/xiomarakuwae/Documents/GitHub/Machine-Learning/Trabajo final/2016_Rendimiento_filtrado.csv')

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
df_p1 = df_p1.sort_values(['MRUN', 'AGNO']).reset_index(drop=True)

# Crear PROM_GRAL_ANTERIOR usando groupby y shift
df_p1['PROM_GRAL_ANTERIOR'] = df_p1.groupby('MRUN')['PROM_GRAL'].shift(1)

# Manejar valores nulos (si no hay dato del año anterior)
df_p1['PROM_GRAL_ANTERIOR'] = df_p1['PROM_GRAL_ANTERIOR'].fillna(np.nan)

# Eliminar los datos de 2016 y los que tienen COD_GRADO = 2
df_p1 = df_p1[(df_p1['AGNO'] != 2016) & (df_p1['COD_GRADO'] != 2)]

# Mostrar las primeras filas para verificar
print(df_p1[['MRUN', 'AGNO', 'PROM_GRAL', 'PROM_GRAL_ANTERIOR']].head(10))



df1 = pd.read_csv('/Users/xiomarakuwae/Documents/GitHub/Machine-Learning/Trabajo final/2020_SEP_filtrado.csv')
df2 = pd.read_csv('/Users/xiomarakuwae/Documents/GitHub/Machine-Learning/Trabajo final/2021_SEP_filtrado.csv')
df3 = pd.read_csv('/Users/xiomarakuwae/Documents/GitHub/Machine-Learning/Trabajo final/2022_SEP_filtrado.csv')
df4 = pd.read_csv('/Users/xiomarakuwae/Documents/GitHub/Machine-Learning/Trabajo final/2023_SEP_filtrado.csv') 
df5 = pd.read_csv('/Users/xiomarakuwae/Documents/GitHub/Machine-Learning/Trabajo final/2024_SEP_filtrado.csv')
df6 = pd.read_csv('/Users/xiomarakuwae/Documents/GitHub/Machine-Learning/Trabajo final/2019_SEP_filtrado.csv')
df7 = pd.read_csv('/Users/xiomarakuwae/Documents/GitHub/Machine-Learning/Trabajo final/2018_SEP_filtrado.csv')
df8 = pd.read_csv('/Users/xiomarakuwae/Documents/GitHub/Machine-Learning/Trabajo final/2017_SEP_filtrado.csv')

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

missing_count = df['PROM_GRAL_ANTERIOR'].isna().sum()
print(f"Valores missing en PROM_GRAL_ANTERIOR: {missing_count}")
