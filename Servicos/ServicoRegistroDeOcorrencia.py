from Modelo.RegistroDeOcorrencia import RegistroDeOcorrencia


class ServicoRegistroDeOcorrencia:
    def __init__(self) -> None:
        pass

    def inserir(self, session, obj):
        session.add(obj)
        session.commit()

    def editar(self, session, obj1, obj2):
        self.result = session.query(
            RegistroDeOcorrencia
            ).filter(
                RegistroDeOcorrencia.id == obj1.id
            ).update(
                {
                    RegistroDeOcorrencia.data: obj2.data
                }, synchronize_session=False
            )
        session.commit()

        if self.result == 1:
            print('Editado com sucesso!')
        else:
            print('Não foi editado!')
        return self.result

    def apagar(self, session, obj):
        session.query(
            RegistroDeOcorrencia
        ).filter(
            RegistroDeOcorrencia.id == obj.id
        ).delete()
        session.commit()

    def buscar_por_numero(self, session, obj) -> object:
        self.__rdo = session.query(
            RegistroDeOcorrencia
        ).filter(
            RegistroDeOcorrencia.numero == obj.numero
        ).first()
        return self.__rdo

    def buscar_por_id(self, session, obj) -> object:
        self.__rdo = session.query(
            RegistroDeOcorrencia
        ).filter(
            RegistroDeOcorrencia.id == obj.id
        ).first()
        return self.__rdo
