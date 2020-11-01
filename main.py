from Repositorio.RegistroDeOcorenciaWord import RegistroDeOcorrenciaWord
from Repositorio.BancoDeDados import Session, engine, Base
from Modelo.RegistroDeOcorrencia import RegistroDeOcorrencia
from Modelo.Contrato import Contrato

w = RegistroDeOcorrenciaWord(r'C:\tmp\PythonWord\RO.docx')
w.carrega_arquivo()

Base.metadata.create_all(engine)

session = Session()

c = Contrato(w.instrumento_contratual, w.contrato_sap, w.orgao, w.contratada, w.autorizacao_servico,
             w.prazo_contratual, w.obj_contrato, w.inicio, w.termino, w.local_execucao)

r = RegistroDeOcorrencia(w.numero, w.tipo.value, w.data, w.corpo_fiscalizacao, w.corpo_contratada,
                         w.assinatura_fiscalizacao, w.corpo_contratada, c)

session.add(c)
session.add(r)

session.commit()
session.close()


