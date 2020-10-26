from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship
from Modelo.Contrato import Contrato
from Repositorio.RegistroDeOcorenciaWord import RegistroDeOcorrenciaWord
from Repositorio.BancoDeDados import Base, session


class RegistroDeOcorrencia(Base):

    __tablename__ = 'registro_de_ocorrencia'

    id = Column(Integer, primary_key=True)
    numero = Column(Integer)
    tipo = Column(Integer)
    data = Column(Date)
    corpo_fiscalizacao = Column(String)
    corpo_contratada = Column(String)
    assinatura_fiscalizacao = Column(String)
    assinatura_contratada = Column(String)
    id_contrato = Column(Integer, ForeignKey('contratos.id'))
    contrato = relationship("Contrato", back_populates="registro_de_ocorrencia")

    def __init__(self, arquivo):
        self.endereco_arquivo = arquivo

    def carrega_contrato(self, instrumento_contratual):
        if Contrato.encontrar_pelo_instrumento_contratual(instrumento_contratual):
            self.contrato - Contrato

    def adicionar(self):
        session.add(self)
        session.commit()

    @classmethod
    def encontrar_pelo_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def encontrar_pelo_nome(cls, nome):
        return cls.query.filter_by(nome=nome).first()

    @classmethod
    def listar(cls):
        return cls.query.all()

    def remover(self):
        session.delete(self)
        session.commit()

    def carrega_word(self):
        try:
            w = RegistroDeOcorrenciaWord(self.endereco_arquivo)
            w.carrega_arquivo()
            self.numero = w.numero
            self.data = w.data
            self.tipo = w.tipo
            self.corpo_fiscalizacao = w.corpo_fiscalizacao
            self.corpo_contratada = w.corpo_contratada
            self.assinatura_fiscalizacao = w.assinatura_fiscalizacao
            self.assinatura_contratada = w.assinatura_contratada
            self.adicionar()
        except Exception as e:
            raise Exception(e)

    def __str__(self):
        obj = 'Numero:................... {0} \n' + \
              'Data:..................... {1} \n' + \
              'Tipo:..................... {2} \n' + \
              'Corpo Fiscalização:....... {3} \n' + \
              'Corpo Contratada:......... {4} \n' + \
              'Assinatura Fiscalização:.. {5} \n' + \
              'Assinatura Contratada:.... {6} \n' + \
              'Titulo:................................................... {7} \n' + \
              'Instrumento Contratual:................................... {8} \n' + \
              'Contrato SAP:............................................. {9} \n' + \
              'Órgão:.................................................... {10} \n' + \
              'Contratada:............................................... {11} \n' + \
              'Autorização de Serviço (AS):.............................. {12} \n' + \
              'Prazo Contratual:......................................... {13} Dias \n' + \
              'Objeto do Contrato / Instalação / Natureza dos Serviços:.. {14} \n' + \
              'Início:................................................... {15} \n' + \
              'Término:.................................................. {16} \n' + \
              'Local de Execução dos Serviços:........................... {17} \n'
        return obj.format(
          self.numero, self.data, self.tipo.name, self.corpo_fiscalizacao,
          self.corpo_contratada, self.assinatura_fiscalizacao, self.assinatura_contratada,
          self.contrato.titulo, self.instrumento_contratual, self.contrato.contrato_sap,
          self.contrato.orgao, self.contrato.contratada, self.contrato.autorizacao_servico,
          self.contrato.prazo_contratual, self.contrato.obj_contrato, self.contrato.inicio,
          self.contrato.termino, self.contrato.local_execucao
        )
