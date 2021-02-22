from Modelo.Contrato import Contrato


class ServicoContrato:
    def inserir(self, session, obj) -> object:
        session.add(obj)
        session.commit()
        session.refresh(obj)
        return obj

    def buscar_por_instrumento_contratual(self, session, obj):
        self.__contrato = session.query(Contrato) \
            .filter(
                Contrato.instrumento_contratual == obj.instrumento_contratual
            ).first()
        return self.__contrato
