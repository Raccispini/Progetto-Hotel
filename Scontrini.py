import pdfkit
from datetime import datetime
class Scontrini(object):
    def stampa(self,lista,tot):
        path_wkhtmltopdf = r'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
        html = "<html><head><meta charset=\"utf-8\"><style>.leftColumn{float:left;}.rightColumn{float:right;}</style></head><body><h1 align = Center>Scontrino</h1><table style=\"width: 100%;\">"
        for i in lista:
            html += "<tr><td class = \"leftColumn\">"+ str(i[0])+"x"+str(i[1])+"</td>"
            html += "<td class = \"rightColumn\">"+str(i[2])+" €</td></tr>"
        html += "<tr><td class = \"rightColumn\"><b>Totale</b></td><td class = \"rightColumn\">"+str(tot)+"</td></tr></table></body></html>"
        file = open("test.html","w")
        file.write(html)
        file.close()
        title = "PDF/Scontrini/"+str(datetime.now().strftime("%d-%m-%Y_%H-%M-%S"))+".pdf"
        pdfkit.from_string(html, title, configuration=config)



