"""Inicio do projeto."""
from Repositorio.RegistroDeOcorenciaWord import RegistroDeOcorrenciaWord
from Repositorio.BancoDeDados import session_scope
from Servicos.ServicoContrato import ServicoContrato
from Servicos.ServicoRegistroDeOcorrencia import ServicoRegistroDeOcorrencia
from Modelo.Contrato import Contrato
from Modelo.RegistroDeOcorrencia import RegistroDeOcorrencia


def inserir():
    """Inserir."""
    with session_scope() as session:
        word = RegistroDeOcorrenciaWord('./RO.docx')

        contrato_modelo = Contrato(word)
        contrato = ServicoContrato().buscar_por_instrumento_contratual(
            session, word
        )

        if contrato is None:
            contrato = ServicoContrato().inserir(session, contrato_modelo)

        rdo = RegistroDeOcorrencia(word, contrato)
        ServicoRegistroDeOcorrencia().inserir(session, rdo)


if __name__ == '__main__':
    inserir()
