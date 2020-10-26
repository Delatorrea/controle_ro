from Modelo.RegistroDeOcorrencia import RegistroDeOcorrencia


r = RegistroDeOcorrencia(r'C:\tmp\PythonWord\RO_PETROBRAS.docx')
r.carrega_word()
print(r)
