from Repositorio.RegistroDeOcorenciaWord import RegistroDeOcorrenciaWord
from Modelo.RegistroDeOcorrencia import RegistroDeOcorrencia
from Modelo.Contrato import Contrato


w = RegistroDeOcorrenciaWord(r'C:\tmp\PythonWord\RO.docx')
w.carrega_arquivo()

c = Contrato(w.instrumento_contratual, w.contrato_sap, w.orgao, w.contratada, w.autorizacao_servico,
             w.prazo_contratual, w.obj_contrato, w.inicio, w.termino, w.local_execucao)

c.adicionar()




