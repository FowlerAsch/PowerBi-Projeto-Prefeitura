# -*- coding: utf-8 -*-
"""ProjetoPrefeitura.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1L6FIeS89Tnm5hW1fRuU7ZwkyaltGj3Ec

PROJETO POWER BI DA PREFEITURA DE RECIFE
"""

import numpy as np
import pandas as pd
from google.colab import files

dataSet = pd.read_csv('/content/situacaofinal2018.csv', sep=";")

"""# **READ**"""

dataSet.head(1-2)

dataSet.isnull().sum()

"""# ***DROP***"""

dataSet = dataSet.drop(columns=["serie"])

"""# **ALTER**

### **Alterando os tipos**
"""

dataSet.dtypes

dataSet["ano"] = dataSet["ano"].astype(str)
dataSet["codigo_escola"] = pd.to_numeric(dataSet["codigo_escola"])
dataSet["escola"] = dataSet["escola"].astype(str)
dataSet["endereco_bairro"] = dataSet["endereco_bairro"].astype(str)
dataSet["endereco_logradouro"] = dataSet["endereco_logradouro"].astype(str)
dataSet["endereco_numero"] = dataSet["endereco_numero"].astype(str)
dataSet["rpa"] = dataSet["rpa"].astype(str)
dataSet["ano_ensino"] = dataSet["ano_ensino"].astype(str)
dataSet["modalidade_ensino_codigo"] = pd.to_numeric(dataSet["modalidade_ensino_codigo"])
dataSet["serie_codigo"] = pd.to_numeric(dataSet["serie_codigo"], errors='coerce')
dataSet["modalidade_ensino"] = dataSet["modalidade_ensino"].astype(str)
dataSet["turma"] = dataSet["turma"].astype(str)
dataSet["turno"] = dataSet["turno"].astype(str)
dataSet["matricula"] = pd.to_numeric(dataSet["matricula"])
dataSet["sexo"] = dataSet["sexo"].astype(str)
dataSet["situacao_codigo"] = dataSet["situacao_codigo"].astype(str)
dataSet["situacao_nome"] = dataSet["situacao_nome"].astype(str)

"""### **Alterando valores**

alterando valor de sexo
"""

dataSet['sexo'].unique()

dataSet.loc[dataSet['sexo'] == "3", 'sexo'] = "2"
dataSet.loc[dataSet['sexo'] == "1", 'sexo'] = "Masculino"
dataSet.loc[dataSet['sexo'] == "2", 'sexo'] = "Feminino"

"""Alterando valor de modalidade_ensino

"""

dataSet['modalidade_ensino'].unique()

dataSet.loc[dataSet['modalidade_ensino'] == "EDUCACAO JOVENS E ADULTOS", 'modalidade_ensino'] = "EDUCACAO JOVENS E ADULTOS"

dataSet.loc[dataSet['modalidade_ensino'] == "EDUCACAO  JOVENS E ADULTOS", 'modalidade_ensino'] = "EDUCACAO JOVENS E ADULTOS"

dataSet.loc[dataSet['modalidade_ensino'] == "PROJOVEM", 'modalidade_ensino'] = "EDUCACAO JOVENS E ADULTOS"

"""Alterando endereco_numero"""

dataSet['endereco_numero'].unique()

dataSet.loc[dataSet['endereco_numero'] == "S/N", 'endereco_numero'] = "SN"

"""Alterando RPA (Região Político Administrativa)"""

dataSet['rpa'].unique()

dataSet.loc[dataSet['rpa'] == "1", 'rpa'] = "CENTRO"
dataSet.loc[dataSet['rpa'] == "2", 'rpa'] = "NORTE"
dataSet.loc[dataSet['rpa'] == "3", 'rpa'] = "NOROESTE"
dataSet.loc[dataSet['rpa'] == "4", 'rpa'] = "OESTE"
dataSet.loc[dataSet['rpa'] == "5", 'rpa'] = "SUDOESTE"
dataSet.loc[dataSet['rpa'] == "6", 'rpa'] = "SUL"

"""# **SAVE**"""

# files.download('/content/situacaofinal2018.csv')