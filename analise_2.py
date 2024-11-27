import numpy as np
from main import df_aluno_turma_t

"""
Análise 2: criação de clusters de turmas a partir da quantidade de alunos.

Cluster 1: mais de 500 alunos.
Cluster 2: mais de 200 alunos.
Cluster 3: mais de 100 alunos.
Cluster 4: mais de 50 alunos.
Cluster 5: mais de 20 alunos.
Cluster 6: 20 ou menos alunos.

Será necessário calcular o número de alunos a partir da tabela df_aluno_turma.
Isso será feito a partir da contagem de linhas para cada NUM_SEQ_TURMA.
"""

df_target = (
    df_aluno_turma_t.groupby("NUM_SEQ_TURMA").size().reset_index(name="QTD_ALUNO")
)
df_target["CLUSTER"] = np.where(
    df_target["QTD_ALUNO"] > 500,
    "Cluster 1",
    np.where(
        df_target["QTD_ALUNO"] > 200,
        "Cluster 2",
        np.where(
            df_target["QTD_ALUNO"] > 100,
            "Cluster 3",
            np.where(
                df_target["QTD_ALUNO"] > 50,
                "Cluster 4",
                np.where(df_target["QTD_ALUNO"] > 20, "Cluster 5", "Cluster 6"),
            ),
        ),
    ),
)
