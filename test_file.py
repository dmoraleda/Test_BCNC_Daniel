import unittest

from wireshark import buscar_coincidencias

class TestBuscarCoincidencias(unittest.TestCase):
    def test_buscar_coincidencias(self):
        archivo_captura = 'captura_de_red/evidencia.pcap'
        protocolo_buscado = 'TCP'
        puerto_destino_buscado = 80
        ip_destino_buscada = '192.168.240.2'


        resultado = buscar_coincidencias(archivo_captura, protocolo_buscado, puerto_destino_buscado, ip_destino_buscada)
        
        # Pinta por pantalla los Resultado de manera enumerada más la información de los resultados.
        print("Resultados:")
        for idx, informacion in enumerate(resultado, start=1):
            print(f"Resultado {idx}: {informacion}")

        # Resultado en formato lista
        self.assertIsInstance(resultado, list)

        # Cada elemento de la lista será in diccionario.
        for informacion in resultado:
            self.assertIsInstance(informacion, dict)

if __name__ == '__main__':
    unittest.main()
