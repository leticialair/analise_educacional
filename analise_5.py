from main import df_aluno_turma_t, df_turma_t

"""
Análise 5: segmentar dados pelos seguintes critérios:
    1. REGIONAL (REGIONAL em df_turma e NOM_REGIONAL em df_unidade);
    2. NOME CAMPUS (NOM_CAMPUS em df_turma e df_unidade);
    3. PRODUTO (calculada a partir de NOM_FANTASIA, que por sua vez está presente em df_aluno_turma e df_turma);
    4. CURSO (COD_CURSO_ALUNO em df_aluno_turma);
    5. TURNO (COD_TURNO_ALUNO) em df_aluno_turma).
"""

list_valores_possiveis = ["AO VIVO", "SEMI", "EAD", "FLEX"]
df_turma_t = df_turma_t[["NUM_SEQ_TURMA", "REGIONAL", "NOM_CAMPUS"]]

df_target = df_aluno_turma_t[
    [
        "COD_MATRICULA",
        "NOM_FANTASIA",
        "COD_CURSO_ALUNO",
        "COD_TURNO_ALUNO",
        "NUM_SEQ_TURMA",
    ]
]
df_target = df_target.merge(df_turma_t, how="left", on="NUM_SEQ_TURMA")
df_target["PRODUTO"] = df_target["NOM_FANTASIA"].apply(
    lambda x: (
        "PRESENCIAL"
        if not isinstance(x, str) or not any(v in x for v in list_valores_possiveis)
        else next(v for v in list_valores_possiveis if v in x)
    )
)

# 1. Segmentação dos alunos pelo critério REGIONAL
df_target_1 = df_target[["COD_MATRICULA", "REGIONAL"]].drop_duplicates()
df_target_1 = df_target_1.groupby("REGIONAL").size().reset_index(name="QTD_ALUNO")

# 2. Segmentação dos alunos pelo critério NOME CAMPUS
df_target_2 = df_target[["COD_MATRICULA", "NOM_CAMPUS"]].drop_duplicates()
df_target_2 = df_target_2.groupby("NOM_CAMPUS").size().reset_index(name="QTD_ALUNO")

# 3. Segmentação dos alunos pelo critério PRODUTO
df_target_3 = df_target[["COD_MATRICULA", "PRODUTO"]].drop_duplicates()
df_target_3 = df_target_3.groupby("PRODUTO").size().reset_index(name="QTD_ALUNO")

# 4. Segmentação dos alunos pelo critério CURSO
df_target_4 = df_target[["COD_MATRICULA", "COD_CURSO_ALUNO"]].drop_duplicates()
df_target_4 = (
    df_target_4.groupby("COD_CURSO_ALUNO").size().reset_index(name="QTD_ALUNO")
)

# 5. Segmentação dos alunos pelo critério TURNO
df_target_5 = df_target[["COD_MATRICULA", "COD_TURNO_ALUNO"]].drop_duplicates()
df_target_5 = (
    df_target_5.groupby("COD_TURNO_ALUNO").size().reset_index(name="QTD_ALUNO")
)
