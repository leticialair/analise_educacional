from main import df_turma_t

"""
Análise 1: visualização de produto por nome fantasia.

A coluna NOM_FANTASIA existe no df_turma.
Contudo, a coluna PRODUTO não existe em nenhuma das tabelas. 
Logo, será uma coluna calculada.
"""

list_valores_possiveis = ["AO VIVO", "SEMI", "EAD", "FLEX"]

df_target = df_turma_t[["NOM_FANTASIA"]]
df_target["PRODUTO"] = df_target["NOM_FANTASIA"].apply(
    lambda x: (
        "PRESENCIAL"
        if not isinstance(x, str) or not any(v in x for v in list_valores_possiveis)
        else next(v for v in list_valores_possiveis if v in x)
    )
)
df_target = df_target.drop_duplicates()
