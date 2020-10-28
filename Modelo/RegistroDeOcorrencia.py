from sqlalchemy import Sequence, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship
from Repositorio.BancoDeDados import Base, session


class RegistroDeOcorrencia(Base):

    __tablename__ = 'registro_de_ocorrencia'

    id = Column(Integer, Sequence('ro_id_seq'),  primary_key=True)
    numero = Column(Integer)
    tipo = Column(Integer)
    data = Column(Date)
    corpo_fiscalizacao = Column(String)
    corpo_contratada = Column(String)
    assinatura_fiscalizacao = Column(String)
    assinatura_contratada = Column(String)
    id_contrato = Column(Integer, ForeignKey('contratos.id'))
    contrato = relationship("Contrato")

    def __init__(self, _numero, _tipo, _data, _corpo_fiscalizacao, _corpo_contratada, _assinatura_fiscalizacao,
                 _assinatura_contratada, _contrato):

        self.numero = _numero
        self.tipo = _tipo
        self.data = _data
        self.corpo_fiscalizacao = _corpo_fiscalizacao
        self.corpo_contratada = _corpo_contratada
        self.assinatura_fiscalizacao = _assinatura_fiscalizacao
        self.assinatura_contratada = _assinatura_contratada
        self.contrato = _contrato

    def adicionar(self):
        session.add(self)
        session.commit()

    @classmethod
    def encontrar_pelo_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def encontrar_pelo_nome(cls, _numero):
        return cls.query.filter_by(numero=_numero).first()

    @classmethod
    def listar(cls):
        return cls.query.all()

    def remover(self):
        session.delete(self)
        session.commit()
