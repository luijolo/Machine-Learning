#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 21 13:51:00 2025

@author: xiomarakuwae
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

df5 = df5[df5['COD_GRADO'].isin([2, 3, 4])]

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
df2 = df2[df2['COD_GRADO'].isin([2, 3, 4])]
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

df4 = df4[df4['COD_GRADO'].isin([2, 3, 4])]

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
df2 = df2[df2['COD_GRADO'].isin([2, 3, 4])]
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

df3 = df3[df3['COD_GRADO'].isin([2, 3, 4])]

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
df2 = df2[df2['COD_GRADO'].isin([2, 3, 4])]
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

df2 = df2[df2['COD_GRADO'].isin([2, 3, 4])]

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
df2 = df2[df2['COD_GRADO'].isin([2, 3, 4])]
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

df1 = df1[df1['COD_GRADO'].isin([2, 3, 4])]

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
df2 = df2[df2['COD_GRADO'].isin([2, 3, 4])]
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

df1 = df1[df1['COD_GRADO'].isin([2, 3, 4])]

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
df2 = df2[df2['COD_GRADO'].isin([2, 3, 4])]
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

df1 = df1[df1['COD_GRADO'].isin([2, 3, 4])]

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
df2 = df2[df2['COD_GRADO'].isin([2, 3, 4])]
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
df1 = df1[df1['cod_grado'].isin([2, 3, 4])]

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
df2 = df2[df2['COD_GRADO'].isin([2, 3, 4])]
df2['COD_GRADO'].value_counts()

df2.to_csv('2017_SEP_filtrado.csv', index=False)

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

