from Repositorio.BancoDeDados import Session, engine, Base
from Modelo.RegistroDeOcorrencia import RegistroDeOcorrencia

session = Session()
Base.metadata.create_all(engine)


class ServicoRegistroDeOcorrencia:
    def inserir(self):
        session.add(self)
        session.commit()
        session.close()

    def buscar_por_numero(self):
        __registro = session.query(RegistroDeOcorrencia) \
            .filter(RegistroDeOcorrencia.numero == self) \
            .first()
        session.close()
        return __registro

    if __name__ == '__main__':
        inserir(RegistroDeOcorrencia)
