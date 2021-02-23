from Modelo.RegistroDeOcorrencia import RegistroDeOcorrencia


class ServicoRegistroDeOcorrencia:

    @staticmethod
    def inserir(session, obj):
        session.add(obj)
        session.commit()

    @staticmethod
    def editar(session, obj1, obj2):
        result = session.query(
            RegistroDeOcorrencia
            ).filter(
                RegistroDeOcorrencia.id == obj1.id
            ).update(
                {
                    RegistroDeOcorrencia.data: obj2.data
                }, synchronize_session=False
            )
        session.commit()

        if result == 1:
            print('Editado com sucesso!')
        else:
            print('Não foi editado!')
        return result

    @staticmethod
    def apagar(session, obj):
        result = session.query(
            RegistroDeOcorrencia
        ).filter(
            RegistroDeOcorrencia.id == obj.id
        ).delete()
        session.commit()
        return result

    @staticmethod
    def buscar_por_numero(session, obj) -> object:
        return session.query(
            RegistroDeOcorrencia
        ).filter(
            RegistroDeOcorrencia.numero == obj.numero
        ).first()

    @staticmethod
    def buscar_por_id(session, obj) -> object:
        return session.query(
            RegistroDeOcorrencia
        ).filter(
            RegistroDeOcorrencia.id == obj.id
        ).first()
