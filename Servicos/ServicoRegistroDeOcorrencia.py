from Repositorio.BancoDeDados import Session
from Modelo.RegistroDeOcorrencia import RegistroDeOcorrencia

session = Session()


class ServicoRegistroDeOcorrencia:
    def inserir(self):
        session.add(self)
        session.commit()
        session.close()

    def editar(self):
        RegistroDeOcorrencia.data = self.data
        session.commit()
        session.close()
        print('Editado com sucesso!')

    def apagar(self):
        session.delete(self)
        session.commit()
        session.close()

    def buscar_por_numero(self):
        __registro = session.query(RegistroDeOcorrencia) \
            .filter(RegistroDeOcorrencia.numero == self) \
            .first()
        session.close()
        return __registro
