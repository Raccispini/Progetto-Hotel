import pdfkit
from datetime import datetime
class Scontrini(object):
    #formato lista : (oggetto,quantita,prezzo)
    def generaScontrino(self,lista,tot):
        html = "<html><head><style>.leftColumn{float:left;}.rightColumn{float:right;}</style></head><body><h1 align = Center>Scontrino</h1><table style=\"width: 100%;\">"
        for i in lista:
            html += "<tr><td class = \"leftColumn\">"+str(i[0]+" x"+i[1])+"</td>"
            html += "<td class = \"rightColumn\">"+str(i[2])+"</td></tr>"
        html += "<tr><td class = \"rightColumn\"><b>Totale</b></td><td class = \"rightColumn\">"+str(tot)+"</td></tr></table></body></html>"
        file = open("test.html")
        file.write(html)
        file.close()
        now = datetime.now()
        pdfkit.from_file("test.html",now.strftime("%D/%M/%Y %H:%M:%S")+".pdf")