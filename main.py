from Repositorio.RegistroDeOcorenciaWord import RegistroDeOcorrenciaWord
'from Repositorio.BancoDeDados import Base, engine'
from Modelo.Contrato import Contrato
from Modelo.RegistroDeOcorrencia import RegistroDeOcorrencia


def inserir():
    word = RegistroDeOcorrenciaWord('./RO.docx')
    word.carrega_arquivo()

    contrato = Contrato(
        word.instrumento_contratual, word.contrato_sap, word.orgao,
        word.contratada, word.autorizacao_servico,
        word.prazo_contratual, word.obj_contrato, word.inicio,
        word.termino, word.local_execucao
    )
    if contrato.buscar_por_instrumento_contratual(
        word.instrumento_contratual
    ) is None:
        contrato.inserir()

    rdo = RegistroDeOcorrencia(
        word.numero, word.tipo.value, word.data, word.corpo_fiscalizacao,
        word.corpo_contratada, word.assinatura_fiscalizacao,
        word.assinatura_contratada, contrato
    )

    rdo_existe = rdo.buscar_por_numero(word.numero)

    if rdo_existe is None:
        rdo.inserir()
    else:
        rdo_existe.editar(rdo)


if __name__ == '__main__':
    'Base.metadata.create_all(engine)'
    inserir()
