from Modelo.Enums.TipoRO import Tipo
import datetime
import os.path
import docx
import re


class RegistroDeOcorrenciaWord:

    def __init__(self, arquivo):
        self.id = None
        self.instrumento_contratual = None
        self.numero = None
        self.tipo = None
        self.data = None
        self.corpo_fiscalizacao = None
        self.corpo_contratada = None
        self.assinatura_fiscalizacao = None
        self.assinatura_contratada = None
        self.app_word = None
        self.endereco_arquivo = arquivo

    @property
    def instrumento_contratual(self):
        return self.__instrumento_contratual

    @instrumento_contratual.setter
    def instrumento_contratual(self, value):
        if value:
            try:
                valor = value.split('\n')
                value = int(valor[1].replace('.', ''))
                self.__instrumento_contratual = value
            except Exception as e:
                raise Exception("Instrumento Contratual inválido\n"
                                "Erro: {}.".format(e))

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, value):
        if value:
            value = int(value.replace('NÚMERO\n', ''))
            self.__numero = value

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, value):
        if value:
            value = re.sub(r"\s+", "", value.upper())
            if value[-1] == 'X':
                self.__tipo = Tipo.Outros
            elif value[6] == 'X':
                self.__tipo = Tipo.Diario
            else:
                self.__tipo = Tipo.Semanal

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if value:
            value = datetime.datetime.strptime(value.replace('DATA\n', ''), '%d/%m/%Y')
            self.__data = value.date()

    @property
    def corpo_fiscalizacao(self):
        return self.__corpo_fiscalizacao

    @corpo_fiscalizacao.setter
    def corpo_fiscalizacao(self, value):
        self.__corpo_fiscalizacao = value

    @property
    def corpo_contratada(self):
        return self.__corpo_contratada

    @corpo_contratada.setter
    def corpo_contratada(self, value):
        self.__corpo_contratada = value

    @property
    def assinatura_fiscalizacao(self):
        return self.__assinatura_fiscalizacao

    @assinatura_fiscalizacao.setter
    def assinatura_fiscalizacao(self, value):
        self.__assinatura_fiscalizacao = value

    @property
    def assinatura_contratada(self):
        return self.__assinatura_contratada

    @assinatura_contratada.setter
    def assinatura_contratada(self, value):
        self.__assinatura_contratada = value

    @property
    def endereco_arquivo(self):
        return self.__endereco_arquivo

    @endereco_arquivo.setter
    def endereco_arquivo(self, value):
        if value:
            if os.path.exists(value):
                self.__endereco_arquivo = value
            else:
                raise Exception("O Arquivo não foi encontrado!\n"
                                "Arquivo: {}.".format(value))

    @property
    def app_word(self):
        return self.__app_word

    @app_word.setter
    def app_word(self, value):
        self.__app_word = value

    def carrega_arquivo(self):
        try:
            self.app_word = docx.Document(self.endereco_arquivo)
            self.instrumento_contratual = self.app_word.tables[0].cell(1, 3).text
            self.numero = self.app_word.tables[0].cell(0, 3).text
            self.data = self.app_word.tables[0].cell(0, 4).text
            self.tipo = self.app_word.tables[0].cell(1, 0).text
            self.corpo_fiscalizacao = self.app_word.tables[0].cell(6, 0).text
            self.corpo_contratada = self.app_word.tables[0].cell(6, 3).text
            self.assinatura_fiscalizacao = self.app_word.tables[0].cell(8, 0).text
            self.assinatura_contratada = self.app_word.tables[0].cell(8, 3).text
        except Exception as e:
            raise Exception(e)

    def __str__(self):
        obj = "Número: {0} \n" + \
              "Instrumento Contratual: {1}"
        return obj.format(self.numero, self.instrumento_contratual)
