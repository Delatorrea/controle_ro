from sqlalchemy import Sequence, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from Repositorio.BancoDeDados import Base, Session


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
    contrato_id = Column(Integer, ForeignKey('contratos.id'))
    contrato = relationship("Contrato", backref="registro_de_ocorrencia")

    def __init__(
        self, _numero, _tipo, _data, _corpo_fiscalizacao, _corpo_contratada,
        _assinatura_fiscalizacao, _assinatura_contratada, _contrato
    ):

        self.numero = _numero
        self.tipo = _tipo
        self.data = _data
        self.corpo_fiscalizacao = _corpo_fiscalizacao
        self.corpo_contratada = _corpo_contratada
        self.assinatura_fiscalizacao = _assinatura_fiscalizacao
        self.assinatura_contratada = _assinatura_contratada
        self.contrato = _contrato
        self.session = Session()

    def inserir(self):
        self.session.add(self)
        self.session.commit()
        self.session.close()
        print('Inserido com sucesso!')

    def editar(self, value):
        self.data = value.data
        self.session.commit()
        self.session.close()
        print('Editado com sucesso!')

    def apagar(self):
        self.session.delete(self)
        self.session.commit()
        self.session.close()

    def buscar_por_numero(self, value):
        self.__registro = self.session.query(self.__class__) \
            .filter(self.numero == value) \
            .first()
        self.session.close()

        print(self.__registro)
        return self.__registro
