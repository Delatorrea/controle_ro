from sqlalchemy import Sequence, Column, Integer, String, Date
from Modelo.RegistroDeOcorrencia import RegistroDeOcorrencia
from sqlalchemy.orm import relationship
from Repositorio.BancoDeDados import Base


class Contrato (Base):
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
    registros = relationship(
        RegistroDeOcorrencia, backref='contratos'
    )

    def __init__(self, obj):

        self.instrumento_contratual = obj.instrumento_contratual
        self.contrato_sap = obj.contrato_sap
        self.orgao = obj.orgao
        self.contratada = obj.contratada
        self.autorizacao_servico = obj.autorizacao_servico
        self.prazo_contratual = obj.prazo_contratual
        self.obj_contrato = obj.obj_contrato
        self.inicio = obj.inicio
        self.termino = obj.termino
        self.local_execucao = obj.local_execucao
