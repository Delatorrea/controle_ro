from sqlalchemy import Sequence, Column, Integer, String, Date
from sqlalchemy.orm import relationship
from Repositorio.BancoDeDados import Base, session


class Contrato(Base):

    __tablename__ = 'contratos'

    id = Column(Integer, Sequence('contrato_id_seq'), primary_key=True)
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

    def __init__(self, _instrumento_contratual, _contrato_sap, _orgao, _contratada, _autorizacao_servico,
                 _prazo_contratual, _obj_contrato, _inicio, _termino, _local_execucao):

        self.instrumento_contratual = _instrumento_contratual
        self.contrato_sap = _contrato_sap
        self.orgao = _orgao
        self.contratada = _contratada
        self.autorizacao_servico = _autorizacao_servico
        self.prazo_contratual = _prazo_contratual
        self.obj_contrato = _obj_contrato
        self.inicio = _inicio
        self.termino = _termino
        self.local_execucao = _local_execucao

    def adicionar(self):
        session.add(self)
        session.commit()

    @classmethod
    def encontrar_pelo_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def encontrar_pelo_instrumento_contratual(cls, _instrumento_contratual):
        return cls.query.filter_by(instrumento_contratual=_instrumento_contratual).first()

    @classmethod
    def listar(cls):
        return cls.query.all()

    def remover(self):
        session.delete(self)
        session.commit()
