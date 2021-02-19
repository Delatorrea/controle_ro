from Repositorio.RegistroDeOcorenciaWord import RegistroDeOcorrenciaWord
from Servicos.ServicoContrato import ServicoContrato
from Servicos.ServicoRegistroDeOcorrencia import ServicoRegistroDeOcorrencia
from Modelo.Contrato import Contrato
from Modelo.RegistroDeOcorrencia import RegistroDeOcorrencia


def inserir():
    word = RegistroDeOcorrenciaWord('./RO.docx')
    word.carrega_arquivo()

    contrato = ServicoContrato.buscar_por_instrumento_contratual(
        word.instrumento_contratual
    )

    if contrato is None:
        contrato = Contrato(
            word.instrumento_contratual, word.contrato_sap, word.orgao,
            word.contratada, word.autorizacao_servico,
            word.prazo_contratual, word.obj_contrato, word.inicio,
            word.termino, word.local_execucao
        )

        contrato.inserir()

    rdo = ServicoRegistroDeOcorrencia.buscar_por_numero(word.numero)

    rdo_novo = RegistroDeOcorrencia(
        word.numero, word.tipo.value, word.data, word.corpo_fiscalizacao,
        word.corpo_contratada, word.assinatura_fiscalizacao,
        word.corpo_contratada, contrato)

    if rdo is None:
        rdo.inserir(rdo_novo)
    else:
        rdo.editar(rdo_novo)


if __name__ == '__main__':
    inserir()
