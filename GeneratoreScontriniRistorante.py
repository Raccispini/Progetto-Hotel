import pdfkit
from datetime import datetime
class GeneratoreScontriniRistorante(object):
    def __init__(self):
        pass

    def stampa(self, lista, totale, metodo):
        current_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        path_wkhtmltopdf = r'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
        Html_file = open("HTML/Scontrini/scontrino_ristorante.html", "r")
        html = Html_file.read()
        for elemento in lista:
            html += f"<tr><td> {elemento[0]} X {elemento[1]}</td><td><p>10%</p></td><td><p>{elemento[3]} €</p></td></tr>"

        html+=f"</table><br> <table style=\"border: transparent\"><tr><td style=\"font-size: 20px; font-weight: bold;\">" \
              f"TOTALE COMPLESSIVO</td><td style=\"font-size: 20px; font-weight: bold; text-align: right\">{totale} €</td></tr>" \
              f"<tr><td style=\"font-size: 20px; font-weight: bold;\">di cui IVA</td>" \
              f"<td style=\"font-size: 20px; font-weight: bold; text-align: right\">{(9*totale)/100} €</td></tr></table>" \
              f"<p>{current_date}<br></p><p>Metodo di Pagamento: {metodo}<br></p><p style=\"font-weight: bold\">ARRIVEDERCI E GRAZIE</p>"

        options = {
            'page-size': 'A5',
            'margin-top': '0.75in',
            'margin-right': '0.30in',
            'margin-bottom': '0.75in',
            'margin-left': '0.30in',
            'zoom': '1.2',
            'encoding': "UTF-8",
        }

        title = ("PDF/ScontriniRistorante/"+datetime.now().strftime("%d-%m-%Y_%H-%M-%S")+".pdf")
        pdfkit.from_string(html, title, configuration=config, options=options)




