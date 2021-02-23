from Modelo.Contrato import Contrato


class ServicoContrato:

    @staticmethod
    def inserir(session, obj) -> object:
        session.add(obj)
        session.commit()
        session.refresh(obj)
        return obj

    @staticmethod
    def buscar_por_instrumento_contratual(session, obj) -> object:
        return session.query(Contrato) \
            .filter(
                Contrato.instrumento_contratual == obj.instrumento_contratual
            ).first()
