from ServicoEmail import baixa_anexos
from Repositorio.RegistroDeOcorenciaWord import RegistroDeOcorrenciaWord
from ServicoContrato import ServicoContrato
from ServicoRegistroDeOcorrencia import ServicoRegistroDeOcorrencia
from Modelo.Contrato import Contrato
from Modelo.RegistroDeOcorrencia import RegistroDeOcorrencia
from Repositorio.BancoDeDados import session_scope
import glob


class ServicoAtualiza:
    @staticmethod
    def teste():
        baixa_anexos('xx', 'xx', '../auxiliar/')
        for filepath in glob.iglob('../auxiliar/*.docx'):
            print(filepath)
            with session_scope() as session:
                word = RegistroDeOcorrenciaWord(filepath)

                contrato_modelo = Contrato(word)
                contrato = ServicoContrato().buscar_por_instrumento_contratual(
                    session, word
                )

                if contrato is None:
                    contrato = ServicoContrato().inserir(session, contrato_modelo)

                rdo = RegistroDeOcorrencia(word, contrato)
                ServicoRegistroDeOcorrencia().inserir(session, rdo)


if __name__ == '__main__':
    ServicoAtualiza.teste()
