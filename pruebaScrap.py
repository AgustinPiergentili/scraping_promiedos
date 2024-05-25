from bs4 import BeautifulSoup
import requests

#obtener HTML
URL_BASE = "https://www.promiedos.com.ar/mundial"
pedido_obtenido = requests.get(URL_BASE)
html_obtenido = pedido_obtenido.text


#Parsear HTML
soup = BeautifulSoup(html_obtenido, "html.parser")

class Argentina():
    
    def __init__(self):
        self.soup = soup


class Argentina:
    def __init__(self):
        self.soup = soup
        self.divs = soup.find_all("div", id="py2restotal")

    def impirmir_info(self):
        return self.divs

    def listar_divs(self):
        for div in self.divs:
            print(div)
            print("\n" + "-"*50 + "\n")  # Separador para mayor legibilidad

    def resultado_octavos(self):
        """Busca el resultado en la pagina"""
        if len(self.divs) >= 2:
            resultado = self.divs[1].get_text(strip=True)
            return resultado

    def imprimir_octavos(self):
        """Imprime el resultado de octavos"""
        resultado = self.resultado_octavos()
        return f"Argentina {resultado} Australia"

    def resultado_cuartos(self):
        if len(self.divs) >= 9:
            return self.divs[8].get_text(strip=True)

    def imprimir_cuartos(self):
        resultado = self.resultado_cuartos()
        if resultado == "23-42":
            return f"Argentina 2 (4) - (3) 2  Paises Bajos"



argentina = Argentina()

print(argentina.imprimir_cuartos())


#print(argentina_octavos)

#src_todos = soup.find_all(src=True)



#for i, imagen in enumerate(src_todos):
    #if imagen ["src"].endswith("png"):
        #print(imagen["src"])
        #r = requests.get(f"https://scrapepark.org/courses/spanish/{imagen['src']}")
        
        #with open(f"imagen_{i}.png", "wb") as f:
            #f.write(r.content)
