import pandas as pd


class Consumo:

    def __init__(self):
        self.path = "arquivos/"

    def get_df_aluno_turma(self) -> pd.DataFrame:
        return pd.read_csv(
            rf"{self.path}AEA_TB_BD_ALUNO_TURMA_24_MODIFICADO.txt", sep=";", dtype=str
        )

    def get_df_turma(self) -> pd.DataFrame:
        return pd.read_csv(
            rf"{self.path}AEA_TB_BD_REL_TURMA_24_MODIFICADO.txt", sep=";", dtype=str
        )

    def get_df_unidade(self) -> pd.DataFrame:
        return pd.read_csv(
            rf"{self.path}AEA_TB_BD_UNIDADES.csv",
            sep=";",
            dtype=str,
            encoding="latin-1",
        )
