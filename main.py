from Repositorio.RegistroDeOcorenciaWord import RegistroDeOcorrenciaWord
from Servicos.ServicoContrato import ServicoContrato
from Servicos.ServicoRegistroDeOcorrencia import ServicoRegistroDeOcorrencia
from Modelo.Contrato import Contrato
from Modelo.RegistroDeOcorrencia import RegistroDeOcorrencia


def inserir():
    w = RegistroDeOcorrenciaWord('/home/emerson/PycharmProjects/controle_ro/RO.docx')
    w.carrega_arquivo()

    c = ServicoContrato.buscar_por_instrumento_contratual(w.instrumento_contratual)

    if c is None:
        c = Contrato(w.instrumento_contratual, w.contrato_sap, w.orgao, w.contratada, w.autorizacao_servico,
                     w.prazo_contratual, w.obj_contrato, w.inicio, w.termino, w.local_execucao)

        ServicoContrato.inserir(c)

    if ServicoRegistroDeOcorrencia.buscar_por_numero(w.numero) is None:
        r = RegistroDeOcorrencia(w.numero, w.tipo.value, w.data, w.corpo_fiscalizacao, w.corpo_contratada,
                                 w.assinatura_fiscalizacao, w.corpo_contratada, c)

        ServicoRegistroDeOcorrencia.inserir(r)
    else:
        print('Já existe')


if __name__ == '__main__':
    inserir()
