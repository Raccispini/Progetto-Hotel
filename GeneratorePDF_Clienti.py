import pdfkit
from datetime import datetime

class GeneratorePDF_Clienti(object):
    def __init__(self):
        pass

    def stampa(self,lista):
        path_wkhtmltopdf = r'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
        Html_file = open("tabella_clienti.html", "r")
        html= Html_file.read()

        #per ogni cliente della lista richiama il metodo string dell'oggetto cliente
        for cliente in lista:
            html +=  str(cliente)

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

        title = "PDF/RiepilogoClienti/" + str(datetime.now().strftime("%d-%m-%Y_%H-%M-%S")) + ".pdf"
        pdfkit.from_string(html, title, configuration=config, options=options)