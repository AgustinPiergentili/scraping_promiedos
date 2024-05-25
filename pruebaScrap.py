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
    """Clase para vizualizar los resultados de Argentina en el mata-mata"""
    def __init__(self):
        self.soup = soup
        self.divs = soup.find_all("div", id="py2restotal")

    def impirmir_info(self):
        """Metodo para ver los divs"""
        return self.divs

    def listar_divs(self):
        """Metodo para ver los divs en una lista"""
        for div in self.divs:
            print(div)
            print("\n" + "-"*50 + "\n")  # Separador para mayor legibilidad

    def resultado_octavos(self):
        """Metodo para buscar el resultado de octavos"""
        if len(self.divs) >= 2:
            resultado = self.divs[1].get_text(strip=True)
            return resultado

    def imprimir_octavos(self):
        """Metodo que imprime el resultado de octavos"""
        resultado = self.resultado_octavos()
        return f"Argentina {resultado} Australia"

    def resultado_cuartos(self):
        """Metodo para buscar el resultado de cuartos"""
        if len(self.divs) >= 9:
            return self.divs[8].get_text(strip=True)

    def imprimir_cuartos(self):
        """Metodo que imprime el resultado de cuartos"""
        resultado = self.resultado_cuartos()
        if resultado == "23-42":
            return f"Argentina 2 (4) - (3) 2  Paises Bajos"

    def resultado_semifinal(self):
        """Metodo para buscar el resultado de semis"""
        if len(self.divs) >= 13:
            return self.divs[12].get_text(strip=True)
        
    def imprimir_semis(self):
        resultado = self.resultado_semifinal()
        return f"Argentina {resultado} Croacia"

    def resultado_final(self):
        if len(self.divs) >= 15:
            return self.divs[14].get_text(strip=True)
        
    def imprimir_final(self):
        resultado = self.resultado_final()
        if resultado == "34-23":
            return f"Argentina 3 (4) - (2) 3 Francia"
    
    
    
    
    
argentina = Argentina()

print(argentina.imprimir_final())

