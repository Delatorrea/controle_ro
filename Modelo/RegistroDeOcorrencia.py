from sqlalchemy import Sequence, Column, Integer, String, Date, ForeignKey, Enum
from sqlalchemy.orm import relationship
from Modelo.Enums.TipoRO import Tipo
from Repositorio.BancoDeDados import Base


class RegistroDeOcorrencia(Base):

    __tablename__ = 'registro_de_ocorrencia'

    id = Column(Integer, Sequence('ro_id_seq'),  primary_key=True)
    numero = Column(Integer)
    tipo = Column(Enum(Tipo))
    data = Column(Date)
    corpo_fiscalizacao = Column(String)
    corpo_contratada = Column(String)
    assinatura_fiscalizacao = Column(String)
    assinatura_contratada = Column(String)
    contrato_id = Column(Integer, ForeignKey('contratos.id'))
    contrato = relationship("Contrato")

    def __init__(self, obj, _contrato):

        self.numero = obj.numero
        self.tipo = obj.tipo
        self.data = obj.data
        self.corpo_fiscalizacao = obj.corpo_fiscalizacao
        self.corpo_contratada = obj.corpo_contratada
        self.assinatura_fiscalizacao = obj.assinatura_fiscalizacao
        self.assinatura_contratada = obj.assinatura_contratada
        self.contrato = _contrato
