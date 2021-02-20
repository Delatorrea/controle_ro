from Repositorio.BancoDeDados import Session
from Modelo.Contrato import Contrato

session = Session()


class ServicoContrato:
    def inserir(self, obj):
        if self.buscar_por_instrumento_contratual(obj) is not None:
            session.add(obj)
            session.commit()
            session.close()

    def buscar_por_instrumento_contratual(self, obj):
        self.__contrato = session.query(Contrato) \
            .filter(
                Contrato.instrumento_contratual == obj.instrumento_contratual
            ).first()
        session.close()
        return self.__contrato
