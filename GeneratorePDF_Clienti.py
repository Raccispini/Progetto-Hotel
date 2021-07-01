import pdfkit

from datetime import datetime
class GeneratorePDF_Clienti(object):
    def stampa(self,lista):
        path_wkhtmltopdf = r'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
        Html_file = open("tabella.html", "r")
        html = Html_file.read()
        print (html)
        '''html = "<html><head><meta charset=\"utf-8\"><style>.leftColumn{float:left;}.rightColumn{float:right;}</style></head><body><h1 align = Center>Scontrino</h1><table style=\"width: 100%;\">"
        for i in lista:
            html += "<tr><td class = \"leftColumn\">"+str(i[0])+" x"+str(i[1])+"</td>"
            html += "<td class = \"rightColumn\">"+str(i[2])+" €</td></tr>"
        html += "<tr><td class = \"rightColumn\"><b>Totale</b></td><td class = \"rightColumn\">"+str(tot)+"</td></tr></table></body></html>"
        file = open("test.html","w")
        file.write(html)
        file.close()
        now = datetime.now()
        options = {
            'page-size': 'Letter',
            'margin-top': '0.75in',
            'margin-right': '1in',
            'margin-bottom': '1in',
            'margin-left': '0.75in',
            'encoding': "UTF-8",
            'custom-header': [
                ('Accept-Encoding', 'utf8')
            ],
            'cookie': [
                ('cookie-name1', 'cookie-value1'),
                ('cookie-name2', 'cookie-value2'),
            ],
            'no-outline': None
        }
        title = "Scontrini\\"+str(datetime.now().strftime("%d-%m-%Y_%H-%M-%S"))+".pdf"
        #print(title)
        pdfkit.from_string(html, title, configuration=config)'''



