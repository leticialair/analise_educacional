from main import df_aluno_turma_t

"""
Análise 3: filtrar produto por PRESENCIAL e SEMI e calcular a contagem de alunos por turma.

Como a coluna de PRODUTO não existe, ela será calculada, assim como foi feito na análise 1.
Após o cálculo, o dataframe será filtrado e será feita uma contagem dos alunos por NUM_SEQ_TURMA.
"""

list_valores_possiveis = ["AO VIVO", "SEMI", "EAD", "FLEX"]

df_aluno_turma_t = df_aluno_turma_t[["NOM_FANTASIA", "NUM_SEQ_TURMA", "COD_MATRICULA"]]
df_aluno_turma_t["PRODUTO"] = df_aluno_turma_t["NOM_FANTASIA"].apply(
    lambda x: (
        "PRESENCIAL"
        if not isinstance(x, str) or not any(v in x for v in list_valores_possiveis)
        else next(v for v in list_valores_possiveis if v in x)
    )
)
df_aluno_turma_t = df_aluno_turma_t[
    df_aluno_turma_t["PRODUTO"].isin(["PRESENCIAL", "SEMI"])
]
df_aluno_turma_t = df_aluno_turma_t[
    ["COD_MATRICULA", "NUM_SEQ_TURMA"]
].drop_duplicates()
df_target = (
    df_aluno_turma_t.groupby("NUM_SEQ_TURMA").size().reset_index(name="QTD_ALUNO")
)
