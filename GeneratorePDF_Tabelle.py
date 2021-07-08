import pdfkit
from datetime import datetime

from PyQt5.QtWidgets import QMessageBox

from cliente.model.ClienteModel import ClienteModel
from dipendente.model.DipendenteModel import DipendenteModel
from fornitore.model.FornitoreModel import FornitoreModel

class GeneratorePDF_Tabelle(object):
    def __init__(self):
        pass

    def stampa(self,lista, path):
        path_wkhtmltopdf = r'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
        Html_file = open(path, "r")
        html= Html_file.read()

        #per ogni cliente della lista richiama il metodo string dell'oggetto cliente
        for elemento in lista:
            html +=  str(elemento)

        #chiude la stringa html
        html += "</table></body></html>"

        options = {
            'page-size': 'A2',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'zoom': '1.2',
            'encoding': "UTF-8",
        }

        if isinstance(lista[0], ClienteModel):
            title = "PDF/RiepilogoClienti/"
        elif isinstance(lista[0], DipendenteModel):
            title = "PDF/RiepilogoDipendenti/"
        elif isinstance(lista[0], FornitoreModel):
            title = "PDF/RiepilogoFornitori/"
        title += str(datetime.now().strftime("%d-%m-%Y_%H-%M-%S")) + ".pdf"
        pdfkit.from_string(html, title, configuration=config, options=options)