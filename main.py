import pandas as pd
from class_consumo import Consumo
from class_tratamento import Tratamento

"""
Importando os dataframes com dtype = str para garantir que dados de texto (como por exemplo, códigos que possuam 0 no início) 
não sejam considerados como numéricos.
"""

df_aluno_turma = Consumo().get_df_aluno_turma()
df_turma = Consumo().get_df_turma()
df_unidade = Consumo().get_df_unidade()

"""
Tratando os tipos das colunas dos dataframes importados.
Regras de negócio aplicadas:
    1. Correção do COD_CAMPUS do df_turma a partir de um dicionário.
    2. Colunas do POSSUI_ do df_turma são transformadas em booleanas.
"""

dict_correcao_cod_campus = Tratamento().get_dict_correcao_cod_campus()
dict_padronizacao_bool = Tratamento().get_dict_padronizacao_bool()
dict_types_aluno_turma = Tratamento().get_dict_types_aluno_turma()
dict_types_turma = Tratamento().get_dict_types_turma()
dict_types_unidade = Tratamento().get_dict_types_unidade()

# 1. Tratamento do df_aluno_turma
list_int = Tratamento().get_list_columns(dict_types_aluno_turma, int)
for coluna in list_int:
    df_aluno_turma[coluna] = (
        df_aluno_turma[coluna].astype(float).fillna(0).round(0).astype(int)
    )

df_aluno_turma_t = df_aluno_turma.astype(dict_types_aluno_turma)

# 2. Tratamento do df_turma
df_turma["COD_CAMPUS"] = df_turma["COD_CAMPUS"].apply(
    Tratamento().treat_cod_campus, args=(dict_correcao_cod_campus,)
)

list_bool = Tratamento().get_list_columns(dict_types_turma, bool)
for coluna in list_bool:
    df_turma[coluna] = df_turma[coluna].apply(
        lambda x: None if pd.isna(x) else dict_padronizacao_bool[x]
    )

list_int = Tratamento().get_list_columns(dict_types_turma, int)
for coluna in list_int:
    df_turma[coluna] = df_turma[coluna].astype(float).fillna(0).round(0).astype(int)

list_datetime_mixed = ["DT_INICIO", "DT_FIM"]
for coluna in list_datetime_mixed:
    df_turma[coluna] = pd.to_datetime(
        df_turma[coluna], format="%Y-%m-%d %H:%M:%S", errors="coerce"
    )

list_datetime = Tratamento().get_list_columns(dict_types_turma, "datetime64[ns]")
for coluna in list_datetime:
    df_turma[coluna] = Tratamento().treat_different_datetime(df_turma[coluna])

df_turma_t = df_turma.astype(dict_types_turma)

# 3. Tratamento do df_unidade
list_int = Tratamento().get_list_columns(dict_types_unidade, int)
for coluna in list_int:
    df_unidade[coluna] = df_unidade[coluna].astype(float).fillna(0).round(0).astype(int)

df_unidade_t = df_unidade.astype(dict_types_unidade)
