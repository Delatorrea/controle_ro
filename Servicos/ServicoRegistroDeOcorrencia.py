from Repositorio.BancoDeDados import Session
from Modelo.RegistroDeOcorrencia import RegistroDeOcorrencia


class ServicoRegistroDeOcorrencia:
    def __init__(self) -> None:
        pass

    def inserir(self, obj):
        self.session = Session()
        self.session.add(obj)
        self.session.commit()
        self.session.close()

    def editar(self, obj1, obj2):
        self.session = Session()
        self.result = self.session.query(
            RegistroDeOcorrencia
            ).filter(
                RegistroDeOcorrencia.id == obj1.id
            ).update(
                {
                    RegistroDeOcorrencia.data: obj2.data
                }, synchronize_session=False
            )
        self.session.commit()
        self.session.close()

        if self.result == 1:
            print('Editado com sucesso!')
        else:
            print('Não foi editado!')
        return self.result

    def apagar(self, obj):
        self.session = Session()
        self.session.query(
            RegistroDeOcorrencia
        ).filter(
            RegistroDeOcorrencia.id == obj.id
        ).delete()
        self.session.commit()
        self.session.close()

    def buscar_por_numero(self, obj) -> object:
        self.session = Session()
        self.__rdo = self.session.query(
            RegistroDeOcorrencia
        ).filter(
            RegistroDeOcorrencia.numero == obj.numero
        ).first()
        self.session.close()
        return self.__rdo

    def buscar_por_id(self, obj) -> object:
        self.session = Session()
        self.__rdo = self.session.query(
            RegistroDeOcorrencia
        ).filter(
            RegistroDeOcorrencia.id == obj.id
        ).first()
        self.session.close()
        return self.__rdo
