import pandas as pd


class Tratamento:

    def __init__(self):
        pass

    def get_dict_correcao_cod_campus(self) -> dict:
        return {str(i): str((i % 9) + 1) for i in range(1, 10)}

    def get_dict_padronizacao_bool(self) -> dict:
        return {"S": True, "N": False, "1": True, "0": False}

    def get_dict_types_aluno_turma(self) -> dict:
        return {
            "DATA_EXTRACAO": "datetime64[ns]",
            "NUM_SEQ_TURMA": int,
            "NOM_FANTASIA": str,
            "COD_MATRICULA": str,
            "COD_CAMPUS_ALUNO": int,
            "COD_CURSO_ALUNO": int,
            "NOM_CURSO_ALUNO": str,
            "COD_TURNO_ALUNO": int,
            "ID_PERIODO_ALUNO": int,
            "COD_DISCIPLINA": str,
            "QTD_CREDITOS_FINANCEIRO": int,
            "DT_INCLUSAO_DISCIPLINA": "datetime64[ns]",
            "ID_CURRICULO_CURSO": int,
            "COD_CAMPUS_TURMA": int,
            "COD_CURSO_TURMA": int,
            "COD_TURNO_TURMA": int,
            "COD_DISCIPLINA_CURRICULO_ALUNO": str,
            "COD_SALA": int,
            "SAFRA": str,
            "COD_FORMA_INGRESSO": int,
            "NOM_FANTASIA_ALUNO": str,
            "NOM_SITUACAO_PERIODO": str,
        }

    def get_dict_types_turma(self) -> dict:
        return {
            "DT_EXTRACAO": "datetime64[ns]",
            "REGIONAL": str,
            "NUM_SEQ_TURMA": int,
            "NOM_INSTITUICAO": str,
            "COD_TIPO_CURSO": int,
            "NOM_FANTASIA": str,
            "COD_CAMPUS": int,
            "NOM_CAMPUS": str,
            "NUM_SEQ_PERIODO_ACADEMICO": int,
            "COD_CURSO": int,
            "NOM_CURSO": str,
            "ID_CURRICULO_CURSO": int,
            "NUM_HABILITACAO": int,
            "COD_TURNO": int,
            "NOM_TURNO": str,
            "ID_PERIODO": int,
            "COD_DISCIPLINA": str,
            "NOM_DISCIPLINA": str,
            "COD_TURMA": int,
            "COD_GRUPO_TURMA": str,
            "QTD_TOTAL_VAGAS": int,
            "QTD_MATRICULADOS": int,
            "QTD_VAGAS_RESERVADAS": int,
            "QTD_VAGAS_DISPONIVEIS": int,
            "CREDITOS_TEORICO": int,
            "CREDITOS_PRATICO": int,
            "CREDITOS_CAMPO": int,
            "POSSUI_SALA": bool,
            "NUM_SEQ_MODALIDADE_ENSINO": int,
            "POSSUI_SALA_PCP": bool,
            "POSSUI_HORARIO": bool,
            "POSSUI_HORÁRIO_PCP": bool,
            "POSSUI_DOCENTE": bool,
            "POSSUI_DOCENTE_PCP": bool,
            "CARGA_PAGA": int,
            "IND_PAGAMENTO": str,
            "TIPO_AULA": str,
            "SITUACAO": str,
            "DT_CRIACAO_TURMA": "datetime64[ns]",
            "COD_SALA": str,
            "TURMA_PAI": str,
            "TURMA_FILHO": str,
            "NUM_SEQ_PAI": int,
            "IND_DEPEND_TOTAL_EAD": str,
            "TEMPOS_DOM": int,
            "TEMPOS_SEG": int,
            "TEMPOS_TER": int,
            "TEMPOS_QUA": int,
            "TEMPOS_QUI": int,
            "TEMPOS_SEX": int,
            "TEMPOS_SAB": int,
            "COD_PROFESSOR": int,
            "COD_TIPO_AULA_EAD": int,
            "NUM_MATRICULA_EAD": int,
            "NOM_TIPO_AULA_EAD": str,
            "IND_TURMA_INTEGRADA": str,
            "IND_TURMA_TEAMS": str,
            "IND_POSSUI_AGENDA_INTELIGENTE": str,
            "IND_TURMA_COMPARTILHADA": str,
            "NUM_SEQ_TURMA_COMPARTILHADA": int,
            "IND_TIPO_INGRESSO": str,
            "DT_INICIO": "datetime64[ns]",
            "DT_FIM": "datetime64[ns]",
            "IND_UPSELL": str,
        }

    def get_dict_types_unidade(self) -> dict:
        return {
            "NOM_GRUPO_MARCA": str,
            "NOM_REGIONAL": str,
            "NOM_NUCLEO": str,
            "SGL_INSTITUICAO": str,
            "COD_INSTITUICAO": int,
            "NOM_INSTITUICAO": str,
            "COD_CAMPUS": int,
            "NOM_CAMPUS": str,
            "MOD_OFERTA_CAMPUS": str,
            "COD_CAMPUS_PAI": int,
            "CAMPUS_PAI": str,
            "COD_CAMPUS_SAP": str,
            "SGL_UF": str,
            "IND_SITUACAO": str,
            "MARCA_CONSOLIDADA": str,
        }

    def get_list_columns(self, dict_types: dict, dtype_target: type) -> list:
        return [col for col, dtype in dict_types.items() if dtype == dtype_target]

    def treat_different_datetime(self, coluna: pd.Series):
        list_fmt = ["%Y-%m-%d %H:%M:%S", "%d/%m/%Y", "%Y-%m-%d", "%d/%m/%Y %H:%M:%S"]

        try:
            coluna = pd.to_datetime(coluna, format=list_fmt[0])
        except:
            try:
                coluna = pd.to_datetime(coluna, format=list_fmt[1])
            except:
                try:
                    coluna = pd.to_datetime(coluna, format=list_fmt[2])
                except:
                    coluna = pd.to_datetime(coluna, format=list_fmt[3])

        return coluna

    def treat_cod_campus(self, x: str, dict_correcao_cod_campus: dict):
        return "".join(dict_correcao_cod_campus.get(char, char) for char in str(x))
