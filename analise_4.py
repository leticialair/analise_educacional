from main import df_aluno_turma_t, df_turma_t

"""
Análise 4: calcular por quantos tempos cada aluno está presente na semana presencialmente.

Para isso, será utilizado o df_aluno_turma e as colunas de TEMPOS_DOM, TEMPOS_SEG, TEMPOS_TER, etc, existentes na tabela df_turma.

Será necessário fazer um group by por COD_MATRICULA (e realizando uma soma) para alcançar o resultado desejado.
"""

list_colunas_tempos = [
    "TEMPOS_DOM",
    "TEMPOS_SEG",
    "TEMPOS_TER",
    "TEMPOS_QUA",
    "TEMPOS_QUI",
    "TEMPOS_SEX",
    "TEMPOS_SAB",
]

list_colunas = list_colunas_tempos.copy()
list_colunas.append("NUM_SEQ_TURMA")
df_turma_t = df_turma_t[list_colunas]
for coluna in list_colunas_tempos:
    df_turma_t[coluna] = df_turma_t[coluna].astype(float).fillna(0).round(0).astype(int)

df_target = df_aluno_turma_t[["COD_MATRICULA", "NUM_SEQ_TURMA"]]
df_target = df_target.merge(df_turma_t, how="left", on="NUM_SEQ_TURMA")
df_target = df_target.drop(columns={"NUM_SEQ_TURMA"})
df_target = df_target.groupby("COD_MATRICULA", as_index=False).sum()
