from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from Repositorio.BancoDeDados import Base, session


class Contrato(Base):

    __tablename__ = 'contratos'

    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    instrumento_contratual = Column(Integer)
    contrato_sap = Column(Integer)
    orgao = Column(String)
    contratada = Column(String)
    autorizacao_servico = Column(String)
    prazo_contratual = Column(Integer)
    obj_contrato = Column(String)
    inicio = Column(Date)
    termino = Column(Date)
    local_execucao = Column(String)
    registro_de_ocorrencia = relationship('RegistroDeOcorrencia', back_populates='contratos')

    def __init__(self, titulo, instrumento_contratual, contrato_sap, orgao, contratada, autorizacao_servico,
                 prazo_contratual, obj_contrato, inicio, termino, local_execucao):
        self.titulo = titulo
        self.instrumento_contratual = instrumento_contratual
        self.contrato_sap = contrato_sap
        self.orgao = orgao
        self.contratada = contratada
        self.autorizacao_servico = autorizacao_servico
        self.prazo_contratual = prazo_contratual
        self.obj_contrato = obj_contrato
        self.inicio = inicio
        self.termino = termino
        self.local_execucao = local_execucao

    def adicionar(self):
        session.add(self)
        session.commit()

    @classmethod
    def encontrar_pelo_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def encontrar_pelo_instrumento_contratual(cls, instrumento_contratual):
        return cls.query.filter_by(instrumento_contratual=instrumento_contratual).first()

    @classmethod
    def listar(cls):
        return cls.query.all()

    def remover(self):
        session.delete(self)
        session.commit()
