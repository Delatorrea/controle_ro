from sqlalchemy import Sequence, Column, Integer, String, Date
from Repositorio.BancoDeDados import Base, Session


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

    def __init__(
        self, _instrumento_contratual, _contrato_sap,
        _orgao, _contratada, _autorizacao_servico, _prazo_contratual,
        _obj_contrato, _inicio, _termino, _local_execucao
    ):

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
        self.session = Session()

    def inserir(self):
        self.session.add(self)
        self.session.commit()
        self.session.close()

    def buscar_por_instrumento_contratual(self, value):
        self.__contrato = self.session.query(self.__class__) \
            .filter(
            self.instrumento_contratual == value
            ) \
            .first()
        self.session.close()
        return self.__contrato
