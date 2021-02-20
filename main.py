from Repositorio.RegistroDeOcorenciaWord import RegistroDeOcorrenciaWord
from Servicos.ServicoContrato import ServicoContrato
from Servicos.ServicoRegistroDeOcorrencia import ServicoRegistroDeOcorrencia
#from Repositorio.BancoDeDados import Base, engine
from Modelo.Contrato import Contrato
from Modelo.RegistroDeOcorrencia import RegistroDeOcorrencia


def inserir():
    word = RegistroDeOcorrenciaWord('./RO.docx')
    word.carrega_arquivo()

    contrato = Contrato(word)

    servicoContrato = ServicoContrato()

    if servicoContrato.buscar_por_instrumento_contratual(
        word
    ) is None:
        servicoContrato.inserir(contrato)

    servicoRegistroDeOcorrencia = ServicoRegistroDeOcorrencia()

    rdo = RegistroDeOcorrencia(word, contrato)
    rdo_existente = servicoRegistroDeOcorrencia.buscar_por_numero(rdo)

    if rdo_existente is None:
        servicoRegistroDeOcorrencia.inserir(rdo)
    else:
        print(servicoRegistroDeOcorrencia.editar(rdo_existente, rdo))


if __name__ == '__main__':
    #Base.metadata.create_all(engine)
    inserir()
