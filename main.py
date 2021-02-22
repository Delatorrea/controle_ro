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
        for i in range(100):
            word = RegistroDeOcorrenciaWord('./RO.docx')

            contratoModelo = Contrato(word)

            servicoContrato = ServicoContrato()

            contrato = servicoContrato.buscar_por_instrumento_contratual(
                session, word
            )

            if contrato is None:
                contrato = servicoContrato.inserir(session, contratoModelo)

            servicoRegistroDeOcorrencia = ServicoRegistroDeOcorrencia()

            rdo = RegistroDeOcorrencia(word, contrato)
            # rdo_existente = servicoRegistroDeOcorrencia.buscar_por_numero(
            #     session, rdo
            # )

            # if rdo_existente is None:
            servicoRegistroDeOcorrencia.inserir(session, rdo)
            # else:
            #     print(
            #         servicoRegistroDeOcorrencia.editar(
            #             session, rdo_existente, rdo
            #         )
            #     )


if __name__ == '__main__':
    inserir()
