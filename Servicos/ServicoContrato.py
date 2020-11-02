from Repositorio.BancoDeDados import Session, engine, Base
from Modelo.Contrato import Contrato

session = Session()
Base.metadata.create_all(engine)


class ServicoContrato:
    def inserir(self):
        session.add(self)
        session.commit()
        session.close()

    def buscar_por_instrumento_contratual(self):
        __contrato = session.query(Contrato) \
            .filter(Contrato.instrumento_contratual == self) \
            .first()
        session.close()
        return __contrato
