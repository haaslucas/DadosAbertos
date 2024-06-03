import pandas as pd
import numpy as np
import os
#read all csv files in this folder

#energiavertida = pd.read_excel('energiavertida.xlsx')
#energiavertida.index = energiavertida.din_instante
geracao = pd.read_csv('geracao.csv',sep=';',index_col='din_instante',parse_dates=True)
geracao = geracao[['id_estado','nom_usina','id_ons','val_geracao']]
geracao = geracao[geracao.id_estado=='PB']

intercambio = pd.read_csv('intercambio.csv',sep=';',index_col='din_instante',parse_dates=True)
intercambio = intercambio[['id_subsistema_origem','id_subsistema_destino','val_intercambiomwmed']]

linhas = pd.read_csv('linhas.csv',sep=';')

restr_eolica = pd.read_csv('restr_eolica.csv',sep=';',index_col='din_instante',parse_dates=True)
restr_eolica = restr_eolica[['id_estado','nom_usina','id_ons','val_geracao','val_geracaolimitada','val_disponibilidade','val_geracaoreferencia','val_geracaoreferenciafinal','cod_razaorestricao','cod_origemrestricao']]
restr_eolica = restr_eolica[restr_eolica.id_estado=='PB']
restr_fotovoltaica = pd.read_csv('restr_fotovoltaica.csv',sep=';',index_col='din_instante',parse_dates=True)
restr_fotovoltaica = restr_fotovoltaica[['id_estado','nom_usina','id_ons','val_geracao','val_geracaolimitada','val_disponibilidade','val_geracaoreferencia','val_geracaoreferenciafinal','cod_razaorestricao','cod_origemrestricao']]
restr_fotovoltaica = restr_fotovoltaica[restr_fotovoltaica.id_estado=='PB']
a=1