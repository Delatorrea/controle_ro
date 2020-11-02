from Repositorio.RegistroDeOcorenciaWord import RegistroDeOcorrenciaWord
from Repositorio.BancoDeDados import Session, engine, Base
from Modelo.RegistroDeOcorrencia import RegistroDeOcorrencia
from Modelo.Contrato import Contrato


def inserir():
    w = RegistroDeOcorrenciaWord(r'C:\tmp\PythonWord\RO.docx')
    w.carrega_arquivo()

    Base.metadata.create_all(engine)

    session = Session()

    c = session.query(Contrato) \
        .filter(Contrato.instrumento_contratual == w.instrumento_contratual) \
        .first()

    if c is None:
        c = Contrato(w.instrumento_contratual, w.contrato_sap, w.orgao, w.contratada, w.autorizacao_servico,
                     w.prazo_contratual, w.obj_contrato, w.inicio, w.termino, w.local_execucao)

        session.add(c)

    r = session.query(RegistroDeOcorrencia) \
        .filter(RegistroDeOcorrencia.numero == w.numero) \
        .first()

    if r is None:
        r = RegistroDeOcorrencia(w.numero, w.tipo.value, w.data, w.corpo_fiscalizacao, w.corpo_contratada,
                                 w.assinatura_fiscalizacao, w.corpo_contratada, c)

        session.add(r)

        session.commit()
        session.close()
    else:
        print('Já Existe')


def select():
    session = Session()

    # 3 - extract all movies
    registros = session.query(RegistroDeOcorrencia).all()

    # 4 - print movies' details
    print('\n### All movies:')
    for registro in registros:
        print(f'Instrumento Contratual: {registro.contrato.instrumento_contratual}')
    print('')


if __name__ == '__main__':
    select()
