import pdfkit
from datetime import datetime

class GeneratorePDF_Clienti(object):
    def stampa(self,lista):
        path_wkhtmltopdf = r'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
        Html_file = open("../../tabella.html", "r")
        html= Html_file.read()
        for cliente in lista:
            html +=  str(cliente)
        html += "</table></body></html>"
        print(html)
        file = open("../../test.html","w")
        file.write(html)
        file.close()
        title = "PDF/RiepilogoClienti/"+str(datetime.now().strftime("%d-%m-%Y_%H-%M-%S"))+".pdf"
        pdfkit.from_string(html, title, configuration=config)



