

from datetime import datetime, timedelta


def lista_fechas_dt(inicio, fin, periodo, festivos = [], habil = False):
    """
    Genera una lista de fechas en formato datetime para un rango dado.

    Parameters
    ----------
    inicio : datetime
        Fecha inicial de la lista. Debe ser anterior a la fecha 'fin'.
    fin : datetime
        Fecha final de la lista. Debe ser posterior a la fecha 'inicio'.
    periodo : int
        Periodo en dias entre cada fecha de la lista.
    festivos : list of datetime, optional
        Lista de fechas para festivos. Estas fechas se excluyen de la lista.
        El valor por defecto es [].
    habil : bool
        Indica si se desean solo dias habiles, en caso que se deseen excluir
        sabados y domingo el valor debe ser 'True'. El valor por defecto
        es 'False'.

    Returns
    -------
    fechas : list
        Lista de fechas en formatos datetime.

    """
    
    dif = fin - inicio
    
    fechas = []
    for d in range(0, dif.days+1, periodo):
        
        fecha_nueva = inicio + timedelta(days=d)
        if (habil) & (fecha_nueva.isoweekday() in [6, 7]): #validar dia habil
            continue
        
        if fecha_nueva in festivos:
            continue
        else:
            fechas += [fecha_nueva]
    
    return fechas


def lista_fechas_str(inicio, fin, periodo, festivos = [],
                     formato = '%Y-%m-%d', habil = False):
    """
    Genera una lista de fechas en formato texto para un rango dado.

    Parameters
    ----------
    inicio : datetime
        Fecha inicial de la lista. Debe ser anterior a la fecha 'fin'.
    fin : datetime
        Fecha final de la lista. Debe ser posterior a la fecha 'inicio'.
    periodo : int
        Periodo en dias entre cada fecha de la lista.
    festivos : list of str, optional
        Lista de fechas para festivos. Estas fechas se excluyen de la lista.
        El valor por defecto es [].
    formato : str, optional
        Formato en texto de la fecha ingresada. El valor por defecto
        es '%Y-%m-%d'.
    habil : bool
        Indica si se desean solo dias habiles, en caso que se deseen excluir
        sabados y domingo el valor debe ser 'True'. El valor por defecto
        es 'False'.

    Returns
    -------
    fechas : list
        Lista de fechas en formato str.

    """
    
    inicio = datetime.strptime(inicio, formato)
    fin = datetime.strptime(fin, formato)
    dif = fin - inicio
    
    fechas = []
    for d in range(0, dif.days+1, periodo):
        
        fecha_nueva = inicio + timedelta(days=d)
        if (habil) & (fecha_nueva.isoweekday() in [6, 7]): #validar dia habil
            continue
        
        fecha_nueva = fecha_nueva.strftime(formato)
        if fecha_nueva in festivos: #validar si es festivo a excluir
            continue
        else:
            fechas += [fecha_nueva]
            
    return fechas


#%% Test
if __name__ == '__main__':
    
    festivos = [datetime(2021, 1, 8)]
    
    fechas_dt1 = lista_fechas_dt(datetime(2021, 1, 1),
                                 datetime(2021, 1, 31),
                                 1,
                                 festivos)
    
    fechas_dt2 = lista_fechas_dt(datetime(2021, 1, 1),
                                 datetime(2021, 1, 31),
                                 7,
                                 festivos)
    
    fechas_str1 = lista_fechas_str('2021-01-01',
                                   '2021-01-31',
                                   1,
                                   ['2021-01-08'])
    
    fechas_str2 = lista_fechas_str('2021-01-01',
                                   '2021-01-31',
                                   7,
                                   ['2021-01-08'])