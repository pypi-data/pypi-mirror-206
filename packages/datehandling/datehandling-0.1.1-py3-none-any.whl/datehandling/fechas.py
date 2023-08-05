# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 13:08:20 2020

@author: Daniel
"""

import datetime as dt

#%%
def Mes_atras(Fecha_0):
    """
    Devuelve la fecha un mes atras, se manejan fechas en formato 'aaaamm' como strings    
    """
    f_0 = dt.date(int( Fecha_0[0:4] ), int( Fecha_0[4:6] ) ,1)
    t = dt.timedelta(days=1)
    f_1 = f_0 - t
    Fecha_1 = f_1.strftime("%Y%m")
    
    return Fecha_1





#%%
def Year_atras(Fecha_0):
    """
    Devuelve la fecha un mes atras, se manejan fechas en formato 'aaaamm' como strings    
    """
    for i in range(12):
        Fecha_0 = Mes_atras(Fecha_0)

    
    return Fecha_0





#%%
def Ultimos_doce_meses(Fecha_0):
    """
    Devuelve una lista con los ultimos doce meses hacia atras de una fecha 'Fecha_0',
    cada fecha se maneja en el formato 'aaaamm' como string
    """
    Fechas = [Fecha_0]
    
    for i in range(11):
        a = Mes_atras( Fechas[i] )
        Fechas.append(a)

    return Fechas





#%%
def Mes_adelante(Fecha_0):
    """
    Devuelve la fecha un mes atras, se manejan fechas en formato 'aaaamm' como strings    
    """
    f_0 = dt.date(int( Fecha_0[0:4] ), int( Fecha_0[4:6] ) ,15)
    t = dt.timedelta(days=30)
    f_1 = f_0 + t
    Fecha_1 = f_1.strftime("%Y%m")
    
    return Fecha_1





#%%
def Fecha_comparacion(Fecha_0, Fecha_1):
    """
    Realiza una comparacion entre dos fechas:
        devuevle 1 si la Fecha_0 es estrictametne mayor a la Fecha_1
        devuelve -1 si la Fecha_0 es estrictametne menor a la Fecha_1
        devuelve 0 en otro caso (cuando son iguales)
    """
    f_0 = dt.date(int( Fecha_0[0:4] ), int( Fecha_0[4:6] ) ,1)
    f_1 = dt.date(int( Fecha_1[0:4] ), int( Fecha_1[4:6] ) ,1)
    
    if f_0 > f_1:
        return 1
    elif f_0 < f_1:
        return -1
    else:
        return 0





#%%
def Lista_Fechas(Fecha_0, Fecha_1):
    """
    Devuelve una lista de fechas comenzando en la Fecha_0 y aumentando mes a mes
    hasta llegar al a Fecha_1.
    Las Fecha_0 tiene que ser estrictamente menor a la Fecha_1 o botara un aviso
    """
    if Fecha_comparacion(Fecha_0, Fecha_1) >= 0:
        return print('  La fecha incial debe ser menor a la fecha final !')
    
    else:        
        FECHAS = [Fecha_0]; i = 0
        while Fecha_comparacion(FECHAS[-1], Fecha_1) == -1:
            FECHAS.append( Mes_adelante(FECHAS[i]) )
            i += 1
        return FECHAS




 
#%%
